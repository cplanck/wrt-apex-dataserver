# Functions for reading and parsing APEX datafiles

import re
from datetime import datetime
import time
from dateutil import parser
import requests

# parse an NMEA GPS string which was pulled out of the datafile (a single line)
# def parse_gps_string(gps_string):

#     time = float(gps_string[6:15])
#     lat = float(gps_string[16:26])
#     lat_dir = gps_string[27]
#     long = float(gps_string[29:38])
#     long_dir = gps_string[39]
#     # uniqueID: time+APEX_name (create this on the data server side)

#     if lat_dir == 'S':
#         lat = -lat
#     if long_dir == 'W':
#         lat = -lat

#     print('LAT: {}, LON: {}, TIMESTAMP: {}'.format(lat/100000, long/10000, time))


# parse an NMEA GPS string which was pulled out of the datafile (a single line)
def parse_gps_string(gps_string):

    gps_hhmmss = float(gps_string[6:15])
    lat = float(gps_string[16:26])
    lat_dir = gps_string[27]
    long = float(gps_string[29:38])
    long_dir = gps_string[39]

    if lat_dir == 'S':
        lat = -lat
    if long_dir == 'W':
        lat = -lat

    return({'gps_hhmmss': gps_hhmmss, 'latitude': round(lat/100000,8), 'longitude': round(long/10000,8)})


# parse_apex_file(path)
def parse_apex_file(root, filename, interval, apex_name, deployment_site):

    """
    Open APEX data file, extract and parse the data at a given interval
     """

    # open file
    data = open(root+filename, 'rb').read().decode('utf-8', 'ignore')
    print('\nFILE NAME: {}'.format(filename))

    # make a list of all the GPS strings using REGEX
    gps_regex = 'GPGGA.*'
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
    while i<len(gps_strings):
        data_dict = parse_gps_string(gps_strings[i])
        data_dict['apex'] = apex_name
        data_dict['deployment_site'] = deployment_site
        data_dict['filename'] = filename
        i = i + interval
        counter = counter + 1
        print(data_dict)
        total_data.append(data_dict)

    print('TOTAL GPS STRINGS AFTER DESAMPLING: {}\n'.format(counter))

    return(total_data)


# post_data_to_database(data)

def identify_apex_from_filename(filename):

    """ 
    Function for extracting the APEX number from the APEX datafile name.
    In the future it would be good to standardize these names so this is less
    difficult. 
    """
    remove_before_apex = re.findall('APEX.*|Apex.*|apex.*', filename)[0]
    strip_apex = remove_before_apex[4:8].lstrip('0')
    apex_number = re.findall('\d*', strip_apex)[0]
    
    print('APEX NUMBER: {}'.format(apex_number))

    return('APEX ' + apex_number)


def post_datafile_to_database(data_dict):
    r = requests.post('http://127.0.0.1:8000/api/apex/crud/', json=data_dict)
    print(r.content)