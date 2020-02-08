# imports
import pandas as pd
import numpy as np

# dataset
cancellation_data_path = "resources/Passenger_Cancellations_Nairobi.csv"
dataset = pd.read_csv(cancellation_data_path)

# This function checks for NaN values in a given column
def check_nans(column_name):
    """ this function will take a column  and check for any available NaNs"""
    all_nan_column_results =  dataset[column_name].isnull()
    null_entries = []
    for row in all_nan_column_results:
        if row == True:
            # if there is a nan entry, we append it to null_entries
            null_entries.append(null_entries)
    return null_entries

# check for NaN values in trip_id column 
print(check_nans("trip_id"))