# Functions for reading and parsing APEX datafiles

import re
from datetime import datetime
import time
from dateutil import parser
import requests
from decode_NMEA_strings import parse_RTK, parse_SLAM, discover_gps_format

def parse_apex_file(root, filename, interval, apex_name, deployment_site, utm_zone):

    """
    Open APEX data file, extract and parse the data at a given interval
    """

    # open file
    data = open(root+filename, 'rb').read().decode('utf-8', 'ignore')
    print('\nFILE NAME: {}'.format(filename))

    # make a list of all the GPS strings using REGEX
    gps_regex = 'GPGGA.*|GNGGA.*'
    gps_strings  = re.findall(gps_regex, data)

    # parse out datetime for when the file was created. This is a ISO 8601 UTC string.
    date_regex = 'Created:.*'
    datetime_iso = re.findall(date_regex, data)[0][9:] # ISO 8601 format 
    datetime_py = parser.parse(datetime_iso) # python datetime format

    # total number of GPS strings
    transmission_num = len(gps_strings)
    print('TOTAL NUMBER OF GPS STRINGS FOUND IN FILE: {}'.format(len(gps_strings)))

    # loop over each GPS stirng and parse the values
    flag = True
    i = 0; counter = 0
    data_dict = {}
    total_data = []
    gps_format = ''
    while i<len(gps_strings):

        # using the first string in the file, discover the GPS format (SLAM or RTK) 
        if i == 0:
            gps_format = discover_gps_format(gps_strings[i])
            print('GPS FORMAT: {}'.format(gps_format))

        if gps_format == 'RTK':
            data_dict = parse_RTK(gps_strings[i])

        elif gps_format == 'SLAM':
            print(utm_zone)
            data_dict = parse_SLAM(gps_strings[i], utm_zone)

        # add in a few extra fields for identification
        data_dict['apex'] = apex_name
        data_dict['deployment_site'] = deployment_site
        data_dict['filename'] = filename
        i = i + interval
        counter = counter + 1
        print(data_dict)
        total_data.append(data_dict)

    print('TOTAL GPS STRINGS AFTER DESAMPLING: {}\n'.format(counter))
    return(total_data)


def identify_apex_from_filename(filename):

    """ 
    Function for extracting the APEX number from the APEX datafile name.
    In the future it would be good to standardize these names so this is less
    difficult. 
    """

    print(filename)

    remove_before_apex = re.findall('APEX.*|Apex.*|apex.*', filename)[0]
    strip_apex = remove_before_apex[4:8].lstrip('0')
    apex_number = re.findall('\d*', strip_apex)[0]
    
    return('APEX ' + apex_number)


def post_datafile_to_database(data_dict):

    """
    Make a POST the request backend API with the data dictionary
    """

    r = requests.post('http://127.0.0.1:8000/api/apex/crud/', json=data_dict)
    print(r.content)