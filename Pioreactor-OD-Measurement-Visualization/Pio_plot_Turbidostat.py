import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

# Read CSV file into a DataFrame
csv_file_path4 = r"%%%%"  # %%%% - Replace with the file path of the OD-readings log including all Pioreactors of given experiment file including .csv
df = pd.read_csv(csv_file_path4)

# Convert "timestamp_localtime" to datetime and calculate time in hours
df['timestamp_localtime'] = pd.to_datetime(df['timestamp_localtime'])
df['time_in_hours'] = (df['timestamp_localtime'] - df['timestamp_localtime'].min()).dt.total_seconds() / 3600

# Create a pivot table to format the data as a matrix
# Change names and OD limits to remove outliers depending on the specifics of the individual experiment.
# The outlier removal values are made for visualization purposes.
pt = pd.pivot_table(df, values='od_reading', index=['time_in_hours'], columns=['pioreactor_unit'], aggfunc='first')
pt_highcap = pt[pt["CAPRICORN"]>0.067]
pt_highvir = pt[pt["VIRGO"]>0.08]
pt = pt[pt['CAPRICORN'] < 0.067]
pt = pt[pt['VIRGO'] < 0.08]

# Change according to the amount of pioreactors running in the experiment and depending on how many it is desired to visualize in one plot
figure, axis = plt.subplots(2,layout='constrained') 
figure.set_figwidth(15.6)
figure.set_figheight(6)
mid = (figure.subplotpars.right + figure.subplotpars.left)/2
figure.suptitle("MW_pio_004 - GLY-AUX$\Delta$ pCBB2.1 $\it{R. rubrum}$ rubisco",x=mid,size=30) # Personalize suptitle.

# Include the actual names of each pioreactor in the experiment that is desired to visualize OD-measurements for.
# Change axis subplot [#,#] depending on amount of plots desired.
figure
axis[0].plot(pt["CAPRICORN"],color="b",zorder=0)
axis[0].set_title("Capricorn",size=26,family="Arial")
axis[1].plot(pt["VIRGO"],color="b")
axis[1].set_title("Virgo",size=26,family="Arial")
figure.supxlabel('Time [h]',x=mid,size=26,family="Arial")
figure.supylabel('Cell density',size=26,family="Arial")
figure.legend(["M9S+kan"],loc="upper center",ncol=2,bbox_to_anchor=(0.5,0)) # Personalize legend
figure.savefig('MW_pio_004.svg',dpi=600,format="svg",bbox_inches='tight') # Include the specific file name and format desired for the output figure mark # If it is not desired to save plot

