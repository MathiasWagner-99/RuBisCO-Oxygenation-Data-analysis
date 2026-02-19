# RuBisCO-Oxygenation-Data-analysis
This repository is dedicated to the python scripts written to analyze and visualize the data obtained in connection with the published paper.

The scripts made for the purpose of analyzing and visualizing the data obtained in connection to the published paper were made by Mathias Herløv Wagner and were created for this purpose specifically. The scripts are not designed to be run and performed on this repository but the source data for the examples and the code will be available for download.

## Pioreactor data visualization
The scripts from this section of the repository were created for and used to analyze and visualize the raw data output from the Pioreactor software.

### Calculating and plotting ΔT between dilution events
The script written to calculate and plot the time between dilutions events of the turbidostat program of the Pioreactors was made to handle the Pioreactor log file and can loop over a folder with the logs from several Pioreactors at once.

### Visualizing the direct optical density measurements from the Pioreactor output
The script was written to visualize the optical density measurements at 600 nm directly from the Pioreactor OD-log output. The script was written to handle a Pioreactor OD-reading-log (which can include the OD-readings from multiple Pioreactors in the same experiment) at a time and requires the specific names of the Pioreactors. 
