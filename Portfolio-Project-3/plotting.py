import math
import numpy as np
import matplotlib.pyplot as plt

# Import Gaza data as 2D array
gaza_array = np.genfromtxt(f"data_files/Gaza.csv", delimiter = ",", skip_header = True, dtype = str)
gaza_list = gaza_array.tolist() # convert array to 2D list
gaza_deaths = []
gaza_injuries = []
for element in gaza_list: # Make 1D lists for deaths and injuries
    gaza_deaths += [int(element[1])]
    gaza_injuries += [int(element[2])]

gaza_deaths_sum = sum(gaza_deaths) # Sum up everything in those lists
gaza_injuries_sum = sum(gaza_injuries)

#Import West Bank data as 2d array
west_array = np.genfromtxt(f"data_files/West.csv", delimiter = ",", skip_header = True, dtype = str)
west_list = west_array.tolist() # convert to 2D list
west_deaths = []
west_injuries = []
for element in west_list: # Make 1D lists for deaths and injuries
    west_deaths += [int(element[1])]
    west_injuries += [int(element[2])]

west_deaths_sum = sum(west_deaths) # Sum up everything in those lists
west_injuries_sum = sum(west_injuries)

info_gaza = ["Number of Deaths", "Number of Injuries"] # Make into lists for headers
num_gaza = [gaza_deaths_sum, gaza_injuries_sum] # Make summed data into list to put in bar graph
info_west = ["Number of Deaths", "Number of Injuries"]
num_west = [west_deaths_sum, west_injuries_sum]

#Import infrastructure data as 2D array
infra_array = np.genfromtxt(f"data_files/Infrastructure.csv", delimiter = ",", skip_header = True, dtype = str)
infra_list = infra_array.tolist() # convert array to 2D list
infra_ed = infra_list[-1][1] # Take last list in 2D list (data is summmative)
infra_res = infra_list[-1][2]

infra_headers = ["Educational Build.", "Residential Build."] # Make into lists to put in bar graph
num_infra = [infra_ed,infra_res]


## PLOTTING ##

plt.figure(figsize = (20,10))

plt.subplot(1, 3, 1) # For Gaza subplot
plt.bar(info_gaza, num_gaza, color = "pink")
plt.xlabel("Number of Deaths")
plt.ylabel("People")
plt.title("Data on Gaza")

plt.subplot(1, 3, 2) # For West Bank subplot
plt.bar(info_west, num_west, color = "violet")
plt.xlabel("Number of Deaths")
plt.ylabel("People")
plt.title("Data on West Bank")

plt.subplot(1, 3, 3) # For infrastructure subplot
plt.bar(infra_headers,num_infra, color = "skyblue")
plt.xlabel("Buildings")
plt.ylabel("Number of Buildings Destroyed")
plt.title("Data on Infrastructure in Palestine")

plt.subplots_adjust(wspace = 0.5) # adjusts spacing between subplots
plt.savefig("Data_Charts.png")
plt.show()
