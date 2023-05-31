import pandas as pd
import math
import requests
import os

link = os.getcwd()+'/'

def get_starwars_data(target):
    '''Accepts a string of which data from the Star Wars API the user wants to download. Returns said data in a dataframe.'''

    # Checking to see if file exists in local directory. 

    if os.path.exists(link + f'{target}.csv'):
        df = pd.read_csv(f'{target}.csv', index_col=0)
        return df

    # Pings the API and writes data to a local csv file if it doesn't exist. 

    else:

        target_df = pd.DataFrame() #Initialize an empty dataframe

        url = f'https://swapi.dev/api/{target}/' #API URL for the target in question
        response = requests.get(url) #Get response from the API
        data = response.json() #Get data from the response

        num_of_pages = math.ceil(data['count'] / len(data['results']))

        for i in range(num_of_pages):
            response = requests.get(url+f'?page={(i+1)}')
            data = response.json()
            target_df = pd.concat([target_df, pd.DataFrame(data['results'])]) #Concats dataframes for each page of results
        
        target_df = target_df.reset_index(drop=True)

        target_df.to_csv(f'{target}.csv')

        return target_df

def get_energy_data():
    '''Returns data from Open Power Systems on energy consumption from different resources.'''
    
    if os.path.exists(link + 'energy.csv'):
        return pd.read_csv('energy.csv', index_col=0)
    else:
        df = pd.read_csv('https://raw.githubusercontent.com/jenfly/opsd/master/opsd_germany_daily.csv')
        df.to_csv('energy.csv')
        return df