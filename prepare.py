import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt

import acquire

def prepare_store(store=pd.read_csv('ts_superstore.csv', index_col=0)):
    store.sale_date = store.sale_date.str.replace(' 00:00:00 GMT', '')
    store.sale_date = pd.to_datetime(store.sale_date, format='%a, %d %b %Y')
    store = store.set_index('sale_date')
    store['month'] = store.index.month_name()
    store['day_of_week'] = store.index.day_name()
    store['sales_total'] = store.sale_amount * store.item_price
    return store

def prepare_energy(energy=acquire.get_energy_data()):
    energy = energy.rename(columns = {'Date' : 'date'
                        ,'Consumption' : 'consumption'
                        , 'Wind': 'wind'
                        , 'Solar': 'solar'
                        , 'Wind+Solar' : 'wind_solar'})
    energy.date = pd.to_datetime(energy.date)
    energy = energy.set_index('date')
    energy['month'] = energy.index.month_name()
    energy['year'] = energy.index.year
    energy = energy.fillna(0)
    return energy