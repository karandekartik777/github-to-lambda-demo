import pandas as pd
import json
import requests

def lambda_handler(event,context):
    print('Event data', " --->",event)
    response = requests.get('https://www.google.com/')
    print(response.text)


    d = {'col1':[1,2],'col2':[3,4]}
    df = pd.read_csv(data =d)
    print(df)
    print('Demo completed successfully')