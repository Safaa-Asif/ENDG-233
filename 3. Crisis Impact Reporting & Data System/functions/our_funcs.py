import numpy as np
import math
import matplotlib as plt
import matplotlib.pyplot as pplt
import matplotlib.image as mpimg

def pick_csv():
    """Displays options for available csv/datasets

    Returns:
        csv (str): option number
    """
    while True:
        # Prints initial options
        csv = input("\nWhat would you like to know about: \n\t1: Casualties/Injuries in Gaza\n\t2: Casualties/Injuries in West Bank\n\t3: Damage to Infrastructure\n\t0: End Program & Print Data Plots\n>> ")
        if csv == "1" or csv == "2" or csv == "3" or csv == "0":
           return csv
        else:
            print("Invalid input. Please try again.")
            continue                                    # Prompts user for another input, if invalid

def option(csv,data):
    """Prints option based on selected dataset

    Parameters:
        csv (str): indicates chosen dataset
        data (list): an appropriately formatted 2D list [str, int, int] of the dataset
    
    Returns:
        (if csv was 1 or 2):
            str: user's chosen option
        (if csv was 3):
            str: user's chosen date
    """
    while True:
        if csv == "1": # Prints options for Gaza CSV
            option = input("What would you like to know about Gaza: \n\t1: Deaths\n\t2: Injuries\n\t3: Update Information\n\tType anything else to return\n>> ")
            if option == "1" or option == "2" or option == "3":
                return option    
            else:
                print("Invalid input. Please try again.")
        elif csv == "2": # Prints options for West Bank CSV
            option = input("What would you like to know about the West Bank: \n\t1: Deaths\n\t2: Injuries\n\t3: Update Information\n\tType anything else to return\n>> ")
            if option == "1" or option == "2" or option == "3":
                return option    
            else:
                print("Invalid input. Please try again.")
        elif csv == "3": # Prints prompt for Infrastructure damage CSV on a specific date
            date = input("Which day would you like data on? Select a date between 2023-10-08 and 2025-11-16 (yyyy-mm-dd)\n>> ")
            for i in range(len(data)): # Check if user's date is in the dataset
                if date == data[i][0]:
                    return date
                else: # if date not found in sublist, continue looping
                    continue
            else:     # if date not found in dataset
                print("Invalid input. Please try again.")

            
def sub_options(csv,option):
    """Prints suboptions based on option chosen

    Parameters:
        csv(str): indicates chosen dataset
        option(str): indicates chosen option

    Returns: 
        (if user chose 3 for option):
            list: entered data as an updated 2d list
        (if user chose option 1 or 2):
            str: user's chosen suboption
    """
    if csv == "1": # for Gaza CSV
        if option == "1": # Prints suboptions for deaths for Gaza CSV 
            suboption = input("\nAvailable information on deaths in Gaza:\n\t1: Maximum death toll\n\t2: Minimum death toll\n\t3: Total deaths\n\t4: Death toll for a specific date\n>> ")
        elif option == "2": # Prints suboptions for injuries Gaza CSV
           suboption = input("\nAvailable information on the injuries in Gaza: \n\t1: Maximum injuries\n\t2: Minimum injuries\n\t3: Total injuries\n\t4: Injuries on a specific date\n>> ")
        elif option == "3": # Prints prompt for updating data for Gaza CSV
            num_dates = int(input("How many dates would you like to update: "))
            updated_list = []
            for i in range(num_dates):
                tootielist = []
                new_date = input("Enter the date you would like to update (yyyy-mm-dd): ")
                new_deaths = int(input("Enter the updated number of deaths: "))
                new_injuries = int(input("Enter the updates number of injuries: "))
                tootielist += [new_date, new_deaths, new_injuries] # stores user inputs into list
                updated_list += [tootielist] # creates 2d list
            return updated_list
        else:
            print("Invalid input. Please try again.")
    elif csv == "2": # for West Bank CSV
        if option == "1":   # Prints suboptions for deaths for West Bank CSV
            suboption = input("\nAvailable information on deaths in West Bank:\n\t1: Maximum death toll\n\t2: Minimum death toll\n\t3: Total deaths\n\t4: Death toll for a specific date\n>> ")
        elif option == "2": # Prints suboptions for injuries for West Bank CSV
            suboption = input("\nAvailable information on the injuries in West Bank: \n\t1: Maximum injuries\n\t2: Minimum injuries\n\t3: Total injuries\n\t4: Injuries on a specific date\n>> ")
        elif option == "3": # Prints prompt for updating data for West Bank CSV
            num_dates = int(input("How many dates would you like to update: "))
            updated_list = []
            for i in range(num_dates):
                tootielist = []
                new_date = input("Enter the date you would like to update after 2025-11-16 (yyyy-mm-dd): ")
                new_deaths = int(input("Enter the updated number of deaths: "))
                new_injuries = int(input("Enter the updates number of injuries: "))
                tootielist += [new_date, new_deaths, new_injuries] # stores user inputs into list
                updated_list += [tootielist] # creates 2d list
            return updated_list
        else:
            print("Invalid input. Please try again.")
    else: # for Infrastructure CSV
        suboption = input(f"\nWhat would you like to know about the infrastructure damage on {option}?\n\t1: Educational Buildings Destroyed\n\t2: Residental Buildings Destroyed\n\t3: Combined Destruction\n>> ")
    return suboption


def deaths(data,suboption,option,csv):
    """Calculates the maximum, minimum, and total deaths

    Parameters:
        data (list): an appropriately formatted 2D list [str, int, int] of the dataset
        suboption (str): indicates user's selected suboption
        option (str): indicates user's selected option
        csv (str): indicates chosen dataset
    
    Returns:
        (if suboption was 1):
            int: maximum deaths 
        (if suboption was 2):
            int: minimum deaths
        (if suboption was 3):
            int: total deaths
        (if suboption was 4):
            int: casualties on a specific date
    """
    #while True:
    if option == "1":
        column_2 = [] # Creates 1D list for information on deaths
        for element in data:
            column_2 += [element[1]]
    while True:
        if suboption == "1": # Calculate max deaths
            maximum_deaths = max(column_2)
            return maximum_deaths
        elif suboption == "2": # Calculate min deaths
            minimum_deaths = min(column_2)
            return minimum_deaths
        elif suboption == "3": # Calculate total deaths
            total_deaths = sum(column_2)
            return total_deaths
        else: # displays deaths on a specific date
            if csv == "1":
                date = input("Which day would you like data on? Select a date between 2023-10-07 and 2025-11-16 (yyyy-mm-dd)\n>> ")
            else:
                date = input("Which day would you like data on? Select a date between 2023-10-07 and 2024-11-13 (yyyy-mm-dd)\n>> ") # less data for WestBank CSV

            for i in range(len(data)): 
                if date == data[i][0]: # Checks if date is in dataset, and returns casualties on that day
                    casualties = data[i][1]
                    return casualties
                else: 
                    continue
            else: # If date not found in dataset
                print("Invalid input. Please try again.\n")

def injuries(data,suboption,option):
    """Calculates the maximum, minimum, and total injuries

    Parameters:
        data (list): an appropriately formatted 2D list [str, int, int] of the dataset
        suboption (str): indicates user's selected suboption
        option (str): indicates user's selected option
    
    Returns:
        (if suboption was 1):
            int: maximum injuries
        (if suboption was 2):
            int: minimum injuries
        (if suboption was 3):
            int: total injuries
        (if suboption was 4):
            int: injuries on a specific date
    """
    while True:
        if option == "2": 
            column_3 = [] # creates 1d list for information on injuries
            for element in data:
                column_3 += [element[2]]
            if suboption == "1": # Calculates max injuries
                maximum_injuries = max(column_3)
                return maximum_injuries
            elif suboption == "2": # Calulates min injuries
                minimum_injuries = min(column_3)
                return minimum_injuries
            elif suboption == "3": # Calculates total injuries
                total_injuries = sum(column_3)
                return total_injuries
            else: # injuries on a specific date
                date = input("Which day would you like data on? Select a date between 2023-10-07 and 2025-11-16 (yyyy-mm-dd)\n>> ")
                for i in range(len(data)):
                    if date == data[i][0]: # If date found in dataset, displays number of injuries
                        injured = data[i][2]
                        return injured
                    else:
                        continue
                else: # if date not found in dataset
                    print("Invalid input. Please try again.\n")

def damage(data,suboption,option):
    """Calculates the educational, residential, and combined building destruction per day

    Parameters:
        data (list): an appropriately formatted 2D list [str, int, int] of the dataset
        suboption (str): indicates user's selected suboption
        option (str): indicates user's selected option
    
    Returns:
        (if suboption was 1):
            int: number of educational buildings destroyed 
        (if suboption was 2):
            int: number of residential buildings destroyed
        (if suboption was 3):
            int: number of combined buildings destroyed
    """
    if suboption == "1": # calculates educational buildings destroyed per day
        for i in range(len(data)):
            if option == data[i][0]:
                ed_destroyed = data[i][1] - data[i-1][1] # Infrastructure.csv was summative, (# on prev. day - # on selected day)
                return ed_destroyed
    elif suboption == "2": # calculates residential buildings destroyed per day
        for i in range(len(data)):
            if option == data[i][0]:
                res_destroyed = data[i][2] - data[i-1][2] # Infrastructure.csv was summative, (# on prev. day - # on selected day)
                return res_destroyed
    else: # calculates combines buildings destroyed per day
        for i in range(len(data)):
            if option == data[i][0]:
                ed_destroyed = data[i][1] - data[i-1][1] # Infrastructure.csv was summative, (# on prev. day - # on selected day)
                res_destroyed = data[i][2] - data[i-1][2]
                comb_destroyed = ed_destroyed + res_destroyed
                return comb_destroyed
