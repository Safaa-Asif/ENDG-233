# user_csv.py
# ENDG 233 F25
# Safaa Asif, Doaa Irshad
# Safaa & Doaa
# A terminal-based data analysis and visualization program in Python.

from functions.our_funcs import pick_csv
from functions.our_funcs import option
from functions.our_funcs import sub_options
from functions.our_funcs import deaths
from functions.our_funcs import injuries
from functions.our_funcs import damage

from functions.read_write import write_csv
from functions.read_write import read_csv

import matplotlib as plt
import matplotlib.pyplot as pplt
import matplotlib.image as mpimg

print("\nData on Palestinian Genocide\n")
while True: 
    csv_option = pick_csv()
    if csv_option == "0":
        print("\nThank you for using our program.")
        img = mpimg.imread("final_plots/data_charts.png") # reads the image
        pplt.imshow(img)
        pplt.show() # displays figure
        break
    elif csv_option == "1":
        csv_string = "Gaza.csv" # assign csv filename instead of flag
    elif csv_option == "2":
        csv_string = "West.csv"
    else:
        csv_string = "Infrastructure.csv"
    csv = read_csv(csv_string) # converts csv into 2D list
    option1 = option(csv_option,csv) # prints options
    suboption = sub_options(csv_option,option1) # print suboptions for selected option
    if option1 == "1":
        deaths_num = deaths(csv,suboption,option1,csv_option)
        print(f"\nThere were {deaths_num} deaths.\n") # displays number of deaths
    elif option1 == "2":
        injured = injuries(csv,suboption,option1)
        print(f"\nThere were {injured} injuries.\n") # displays number of injuries
    elif option1 == "3":
        write_csv(csv_string,suboption,2) # 2 indicates appending
        print("Thank you for your contribution\n")
    else:
        damaged = damage(csv,suboption,option1)
        print(f"\nThere were {damaged} buildings destroyed.\n") # displays number of buildings destroyed