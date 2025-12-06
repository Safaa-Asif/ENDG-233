import numpy as np
import math
import matplotlib as plt
import matplotlib.pyplot as pplt
import matplotlib.image as mpimg

def read_csv(filename, headers = True):
    """Converts the CSV into a 2D list

    Parameters:
        filename (str): a valid filename
        headers (bool): optional parameter (not for running code)

    Returns:
        data_list (list): an appropriately formatted 2D list [str, int, int]
    """
    data_array = np.genfromtxt(f"data_files/{filename}", delimiter = ",", skip_header = headers, dtype = str) # converts csv into array
    data_list = data_array.tolist() # converts array into 2D list
    if headers == True:
        for i in range(len(data_list)): # Loops 2D list of strings, and makes everything except first column as int
            for j in range(len(data_list[i])-1):
                data_list[i][j+1] = int(data_list[i][j+1])
    else:
        i = 1
        while 1 <= i <= (len(data_list)-1): # Same thing, but leaves in headers
            data_list[i][j+1] = int(data_list[i][j+1])
            i += 1
    
    return data_list

def write_csv(filename, data, overwrite):
    """Overwrites or appends to the chosen file

    Parameters:
        filename (str): a valid filename
        data (list): a 2D list from read_csv()
        overwrite: a flag to indicate appending or overwriting
    
    Returns:
        file: the overwritten or appended file
    """

    file = filename
    if overwrite == 1:
        file = open(f"data_files/{file}", "w") # writing to the file
        
        data_new = ""
        for i in range(len(data)):
            for j in range(len(data[i])): # converts to comma seperated string
                if j < (len(data[i])-1):
                    data_new += (str(data[i][j]) + ",")
                else:
                    data_new += (str(data[i][j]) + "\n") 
        
        file.write(f"{data_new}") # overwrites existing data with new data string
        file.close()

    else:
        file = open(f"data_files/{file}", "a") # appending to the file
        data_str = ""
        for i in range(len(data)):
            for j in range(len(data[i])): # converts to comma seperated string
                if j < (len(data[i])-1):
                    data_str += (str(data[i][j]) + ",")
                else:
                    data_str += (str(data[i][j]) + "\n")
        
        file.write(f"\n{data_str}") # append to existing file
        file.close()
        
    return file 
