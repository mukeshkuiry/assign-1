import pandas as pd
import requests as req
from logging import *

LOG_FORMAT='Line No.: %(lineno)d || Type: %(levelname)s || Timestamp: %(asctime)s || Entry: %(message)s'  # format for logging
basicConfig(filename='logFile.log',level=INFO,format=LOG_FORMAT)                                          # configuring logging

def download_csv(url,filename):                                        # function to download the csv file 
    try:
        res=req.get(url)           
        res.raise_for_status()                                          # Check for HTTP errors
        with open(filename, 'wb') as file:
            file.write(res.content)                                     # writes the content of the file into the given filename
        info(f"Download successful!!! Filename: {filename}")            # logs the success information into the log file
    except Exception as obj:
        error(f"Error downloading file: {obj}")                         # logs the error message into the log file
        print("Sorry! There was an error in downloading the file...")
        

def split_csv(dob,filename):                                           # function to split the file into 2 data files
    try:
        df=pd.read_csv(filename)
        df['Date of birth']=pd.to_datetime(df['Date of birth'])         # converting the objects in "Date of birth"column to datetime object
        
        # Splitting criteria
        below_dob=df[df['Date of birth']<dob]                           
        above_dob=df[df['Date of birth']>=dob]
        
        # saving the split dataframe to new csv files
        below_dob.to_csv('dob_below.csv',index=False)                   
        above_dob.to_csv('dob_above.csv',index=False)
        
        info("Split Successful!!! Files created: {dob_below.csv} and {dob_above.csv}")      # logs the success information into the log file
    except Exception as e:
        error(f"Error processing file: {e}")                                                # logs the error message into the log file
        print("Sorry! There was an error in processing the file...")
        

def enter_dob():                                                                    # function to take dob as input from the user
    while True:                                                                     # prompts the user to enter DOB until entered in correct format
        try:
            dob=input("Enter Date Of Birth in the format (DD-MM-YYYY): ")
            dob=pd.to_datetime(dob,format='mixed', dayfirst=True)                   # converting input(string) to datetime object
            info("DOB entered in correct format!!!")                                # logs the success information into the log file
            return dob
        except Exception as e:
            error(f"Invalid input was entered!!! {e}")                              # logs the error message into the log file 
            print("Invalid input!!!")
         

def main():
    input_url="https://drive.google.com/uc?id=1AWPf-pJodJKeHsARQK_RHiNsE8fjPCVK&export=download"  # url to access the required csv file
    file_name="people-1000.csv"                                                                   # filename for the csv file 
    
    download_csv(input_url,file_name)           # function to download the csv
    dob=enter_dob()                             # storing the dob
    split_csv(dob,file_name)                    # splitting the file
    
if __name__=="__main__":
    main()