import re
from datetime import datetime
import time
from dateutil import parser
import requests
import json



# r = requests.post('http://127.0.0.1:8000/api/apex/filenames/', data=payload)
# print(r.content)

# r = requests.get('http://127.0.0.1:8000api/apex/deployments')
# print(json.loads(r.content))

test = 5
server = 'http://127.0.0.1:8000/api/'

# (DATASERVER) POST DATA
if test == 2:
    data = [{'gps_hhmmss': 30646.29, 'latitude': 38.6018722, 'longitude': 42.123559, 'apex': 'APEX 4', 'deployment_site': 'CROFT', 'filename': 'Apex4_cc__pmqc_DQC_000001_2022132_003.dat', 'uniqueID': '3064600APEX4CROFT', 'deployment': 2}]
    print(data)
    print(json.dumps(data))
    r = requests.post('http://127.0.0.1:8000/api/apex/crud/', json=data)
    print(r.content)

# (FRONTEND) @ apex/frontend/deployments. Returns list of deployments or single deployment if 'deployment' query param is set.
elif test == 3:
    url = server + 'apex/frontend/deployments'
    r = requests.get(url)
    print(json.loads(r.content))

    url = server + 'apex/frontend/deployments/?deployment=2'
    r = requests.get(url)
    print(json.loads(r.content))

# (FRONTEND) @ apex/frontend/rawdata. Returns raw data given 'deployment' query param.
elif test == 4:
    url = server + 'apex/frontend/rawdata/?deployment=3'
    r = requests.get(url)
    print(json.loads(r.content))

# (FRONTEND) @ apex/frontend/stats. Returns statistics given 'deployment' query param.
elif test == 5:
    url = server + 'apex/frontend/stats/?deployment=8'
    r = requests.get(url)
    print(json.loads(r.content))

# (FRONTEND) @ apex/frontend/deployment_sites. Returns deployment sites and associated APEX machines.
elif test == 6:
    url = server + 'apex/frontend/deployment_sites'
    r = requests.get(url)
    print(json.loads(r.content))



