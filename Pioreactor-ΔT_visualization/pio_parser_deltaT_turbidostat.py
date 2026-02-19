from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os
import glob 

# This loops over every single file that is a .csv inside the folder specified.
# This script is made specifically to handle the Pioreactor logs for a turbidostat dilution automation.

for file_path in glob.glob(r'%%%%'+r'\*.csv'): # %%%% - insert full file path
    csv_file_path1 = file_path
    df = pd.read_csv(csv_file_path1)
    # Convert "timestamp_localtime" to datetime and calculate time in hours
    df['timestamp_localtime'] = pd.to_datetime(df['timestamp_localtime'])
    df['time_in_hours'] = (df['timestamp_localtime'] - df['timestamp_localtime'].min()).dt.total_seconds() / 3600

    experiment = df['experiment'][0][0:10]
    name = df['pioreactor_unit'][0]
    hour = str(int(df.at[df.index[-1], 'time_in_hours']))
    # Sort dataframe based on time passed since experiment start
    df = df.sort_values('time_in_hours')

    # Remove all rows where the message does not contain the "DilutionEvent: Latest OD" string
    df = df[df['message'].str.contains('DilutionEvent: Latest OD',na=False)]

    # Create a list of deltaT values and add it to the dataframe

    deltaT = [0]
    for DilutionTime in df['time_in_hours']:
        if DilutionTime == df['time_in_hours'].values[0]:
            print("first value doesnt get deltaT")
        elif DilutionTime-prior > 14: # To remove outliers, Depends on the growth rate of the strain growing, should be scaled to be bigger than the biggest non-outlier (for visual purposes, do not use this for direct analysis)
            print("Dilution time too large, error happened")
            deltaT.append(0)   
        elif DilutionTime-prior < 6.05: # To remove outliers, Depends on the growth rate of the strain growing, should be scaled to be smaller than the lowest non-outlier (for visual purposes, do not use this for direct analysis)
            print("Dilution time too small, error happened")
            deltaT.append(0)
        else:
            deltaT.append(DilutionTime-prior)
        prior = DilutionTime
    df['deltaT'] = deltaT
    df = df.drop(df[df['deltaT'] == 0].index)

    print(df.head())

    # Plot deltaT values against time since experiment start & save the figure as a file in the given folder
    plt.plot(df['time_in_hours'].values[0:],df['deltaT'].values[0:])
    plt.scatter(df['time_in_hours'].values[0:],df['deltaT'].values[0:],color="red")
    plt.title('Time between dilutions in turbidostat '+name+' - '+hour+'h',family="Arial")
    plt.xlabel('Time [h]',family="Arial")
    plt.ylabel('$\Delta$T between dilutions [h]',family="Arial")
    plt.ylim(bottom=0)
    file_path = os.path.join(r"%%%%",experiment+'_deltaT_'+hour+'h_'+name+'.svg') # %%%% - replace with file path for desired destination folder
    plt.savefig(file_path,bbox_inches='tight',format="svg",dpi=600) # Saves the deltaT plot in above specified folder
    plt.show()


