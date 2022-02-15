#importing libraries
import requests
import pandas as pd
from sodapy import Socrata
import time

#Keys
API_KEY = "bsjzernoyx3jz26c4vbro6kjc"

data_url = 'data.sfgov.org' # The Host name for the API Endpoint
data_set = 'nuek-vuh3' # The data set at the API Endpoint
app_token = "L04YPVGSsEDmyE3zJOVknY2ap"
client = Socrata(data_url,app_token) # Pointing the client at the Endpoint
#Timeout
client.timeout = 60

#Pulling first 2000 results as JSON from the API_KEY
#SoDaPY library converts this JSON to Python list of dictionaries

results = client.get(data_set, limit = 2000)

#Convert list of dictonaries to Pandas data frame

df = pd.DataFrame.from_records(results)

#Saving the dataframe to CSV

df.to_csv("my_fire_data.csv")

client.close()
