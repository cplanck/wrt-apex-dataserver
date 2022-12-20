# Script for POST requesting WRT Apex files to the database.
# Note $GPGGA is a an NMEA GOS stamp
# ref. http://aprs.gids.nl/nmea/#gga

# thoughts... in addition to sending the data over network, maybe we should also make a request to the pop over the first and last date found in each  
# thoughts... in addition to POSTING the data on whatever interval we choose, we should also consider grabbing the timestamp off the first
# and last entries in the file and POSTING those to the Apex_data_scans model. This way we always have an exact bound on when the machine was turned on/off

import re
from datetime import datetime
import time
from dateutil import parser
import requests
from read_apex_data_files import *
import json
import os


file = 'APEX014-CampRobinson-1_G06_DAM_000004_2022286_001.dat'
root = '/Users/cameronplanck/Dropbox/Freelance/White River Technlogies/Data/WRT'
full_path = root + file

# GET APEX machines with deployment entries that have "post_data_to_database == True":
# Returns a dictionary with a deployment_site as keys and apex_deployments as values
request = requests.get('http://127.0.0.1:8000/api/apex/deployments')
deployments = json.loads(request.content)

# Loop through each deploment site and scan the files in the associated directory
for deployment in deployments:
    deployment_site = list(deployment.keys())[0]

    # add apexs to list
    apex_list = deployment[deployment_site]
    
    # navigate to deployment_site directory
    data_directory = root + '/' + deployment_site + '/DQC/'
    data_files = os.listdir(data_directory)
    number_of_files = len(data_files)
    print(number_of_files)

    # Loop over each APEX datafile in the deployment_site directory. Call parse_apex_file to return a dictionary of values from the $GPGGA strings
    for filename in data_files:
        # Get the APEX machine name (number) from the datafile name
        apex_name = identify_apex_from_filename(filename)

        # Parse the data ONLY if this APEX is in apex_list, meaning it has "post_data_to_database" checked
        if apex_name in apex_list:
            data_in_each_file = parse_apex_file(data_directory, filename, 50, apex_name, deployment_site) # returns a list of dictionaries which is read to be posted to the API
            post_datafile_to_database(data_in_each_file)