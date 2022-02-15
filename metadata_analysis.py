#importing libraries
import requests
import pandas as pd
from sodapy import Socrata
import time


data_url = 'data.sfgov.org' # The Host name for the API Endpoint
data_set = 'nuek-vuh3' # The data set at the API Endpoint
app_token = "L04YPVGSsEDmyE3zJOVknY2ap"
client = Socrata(data_url,app_token) # Pointing the client at the Endpoint
#Timeout
client.timeout = 60

metadata = client.get_metadata(data_set)
print([x["fieldName"] for x in metadata['columns']])
