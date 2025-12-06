# analysis.py FINAL DRAFT
# ENDG 233 F25
# Safaa Asif 30274206
# A terminal-based program for analyzing home sales records.

import records

# DEFINE FUNCTIONS HERE

def get_region():
    """Prints the prompt to select the region and returns a capitalized valid region name

    Returns:
        user_input (str): a capitalized valid input provided by the user
    """
    
    while True:                                                                                      # While the function is in use
        user_input = input("Enter the region you want to select (e.g. NE) or type '0' to quit: ")    # Prompt user for input
        user_input = user_input.upper()                                                              # Capitalize it
        if (user_input == "0") or (user_input in records.regions):                                   # If it is 0, or found in the records
            return user_input                                                                        # Return it so I can deal with it in main program
        else:                                                                                        # If user input is NOT found in regions list
            print("\nError! Invalid input. Please try again.\n")                                     # Print error message (loop will prompt for another input)
            

def print_options():
    """Prints the inner menu thats prompts the user to select a data analysis option and returns a valid option number

    Returns:
        int: a valid input provided by the user
    """

    while True:                                                                      # While the function is in use
        user_menu_option = int(input(                                                # Printing the menu options (each on a new line, starting with an indent)
            "\nEnter the number of the option you want to select:\n"
            "\t1) Print Average Price\n"
            "\t2) Print Maximum Bedrooms and Bathrooms\n"
            "\t0) Return to Main Menu\n"
            ">> "))

        if (user_menu_option > 2 or user_menu_option < 0):                            # If user's menu option is INVALID
            print("\nError! Invalid input. Please try again.")                        # Print error message
        else:                                                                         # If user's menu option IS valid,
            return user_menu_option                                                   # then return it
    

def get_average_price(region):
    """Takes the selected region and returns the average price of homes in the selected region

    Parameters:
        region (str): a valid region

    Returns:
        (if records in that region exist):
            float: the average price of units in the selected region
        (if no records exist):     
            int: a flag value of -1
    """
    list_of_prices = []                                             # Create an empty list to store the prices for that region
    for element in records.data:                                    # Loop through the sublists in the data list (in records)
        if (element[0] == region):                                  # If the 1st entry of the sublist is the user's region
            list_of_prices += [float(element[1])]                   # Store the 2nd entry of the sublist (i.e. price) as a float in the list created
    if (len(list_of_prices) == 0):                                  # If no data is found for the region
        return -1                                                   # Return a flag value
    else:                                                           # If data is found for the region
        sum_of_prices = 0                                           # Initialize the sum to 0
        for price in list_of_prices:                                # For each entry in the list
            sum_of_prices += price                                  # Add them
        average_price = sum_of_prices / len(list_of_prices)         # Compute avg by dividing by the number of entries in the list
        return average_price


def get_bed_bath_max(region):
    """Takes the selected region and returns the maximum number of rooms and maximum number of bathrooms

    Parameters:
        region (str): a valid region

    Returns:
        (if records in that region exist):
            list: [maximum number of bedrooms, maximum number of bathrooms]
        (if no records exist):     
            int: a flag value of -1
    """
    
    num_of_rooms = []                                               # Create an empty list to store the number of rooms
    num_of_bathrooms = []                                           # Create an empty list to store the number of bathrooms
    for element in records.data:                                    # Loop through the sublists in the data list
        if element[0] == region:                                    # If the region matches the user's region
            num_of_rooms += [int(element[2])]                       # Store the value for # of rooms as an integer in the list created
            num_of_bathrooms += [int(element[3])]                   # Store the value for # of bathrooms as an integer in the list created
    
    if (len(num_of_rooms) == 0):                                    # If NO data is found (this also implies num_of_bathrooms will be empty)
        return -1                                                   # Return a flag value
    else:                                                           # If data IS found for the region
        max_rooms = max(num_of_rooms)                               # Find the maximum of the list containing # of rooms
        max_bathrooms = max(num_of_bathrooms)                       # Find the maximum of the list containing # of bathrooms
        max_bed_and_bath = [max_rooms, max_bathrooms]               # Store the maximum values in a list
        return max_bed_and_bath                                     # Return this list
   

def print_average_price(region, avg_price):
    """Prints the average price of units in a region or calls the no records message

    Parameters:
        region (str): a valid region
        average_price 
            (float): the average price of the units in a region
            (-1): if there are no records
    """
    if (avg_price == -1):                                                                           # If get_average_price did NOT find data
        print(f"\nThere are no records available for the {region} region.")
    else:                                                                                           # If get_average_price DID find data
        print(f"\nThe average unit price for the {region} region is ${avg_price:.2f}")              # Rounded the avg_price to 2 decimal places


def print_bed_bath_max(region, data):
    """Prints the maximum bedrooms and bathrooms in a region or calls the no records message

    Parameters:
        region (str): a valid region
        data 
            (list): [maximum number of bedrooms, maximum number of bathrooms]
            (-1): if there are no records
    """
    if (data == -1):                                                                                # If get_bed_bath_max did NOT find data
        print(f"\nThere are no records available for the {region} region.")                         # If get_bed_bath_max DID find data
    else:                                                                                           
        print(f"\nThe {region} region has a maximum of {data[0]} bedrooms and {data[1]} bathrooms") # Index 0 of data refers to the 1st value stored

# ******************************************************************************************************
# MAIN PROGRAM DEFINED BELOW

print("ENDG 233 Sales Analysis Program\n")

while True:                                                                               # While the program is still in use                                                                                       # Ends the program
                                                                          
        user_region = get_region()                                                        # Call get_regions function to ask for user region
        if (user_region == "0"):
            print("\nThank you for using our program.")
            break                                                                         # Ends the program
        else:
            user_menu_selection = print_options()                                         # Print inner menu     
            if (user_menu_selection == 1):
                average_price = get_average_price(user_region)                            # Use the get_average_price function on the user's region
                print_average_price(user_region, average_price)                           # Use the print_average_price func. on the average price and region 
            elif (user_menu_selection == 2):
                max_bed_bath = get_bed_bath_max(user_region)                              # Use get_bed_bath_max func. on user's region
                print_bed_bath_max(user_region, max_bed_bath)                             # Use print_bed_bath_max on user's region and max_bed_bath
            print(f"{'':=^70s}")                                                          # For any menu selection, print dashed line after