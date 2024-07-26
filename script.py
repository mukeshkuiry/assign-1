import pandas as pd
import requests as req
from logging import *

# Configure logging
LOG_FORMAT = 'Line No.: %(lineno)d || Type: %(levelname)s || Timestamp: %(asctime)s || Entry: %(message)s'
basicConfig(filename='logFile.log', level=INFO, format=LOG_FORMAT)

def download_csv(url, filename):
    """
    Download a CSV file from the given URL and save it with the given filename.

    Args:
        url (str): The URL to download the CSV file from.
        filename (str): The name of the file to save the downloaded content.
    """
    try:
        response = req.get(url)
        response.raise_for_status()  # Check for HTTP errors
        with open(filename, 'wb') as file:
            file.write(response.content)
        info(f"Download successful! Filename: {filename}")
    except Exception as e:
        error(f"Error downloading file: {e}")
        print("Sorry! There was an error in downloading the file...")

def split_csv_by_dob(dob, filename):
    """
    Split the CSV file into two separate files based on the given date of birth.

    Args:
        dob (datetime): The date of birth to split the data on.
        filename (str): The name of the CSV file to read from.
    """
    try:
        df = pd.read_csv(filename)
        df['Date of birth'] = pd.to_datetime(df['Date of birth'], dayfirst=True)  # Convert to datetime object
        
        # Splitting criteria
        df_below_dob = df[df['Date of birth'] < dob]
        df_above_dob = df[df['Date of birth'] >= dob]
        
        # Saving the split dataframes to new CSV files
        df_below_dob.to_csv('dob_below.csv', index=False)
        df_above_dob.to_csv('dob_above.csv', index=False)
        
        info("Split successful! Files created: dob_below.csv and dob_above.csv")
    except Exception as e:
        error(f"Error processing file: {e}")
        print("Sorry! There was an error in processing the file...")

def get_user_dob():
    """
    Prompt the user to enter a date of birth and convert it to a datetime object.

    Returns:
        datetime: The entered date of birth.
    """
    while True:
        try:
            user_input = input("Enter Date Of Birth in the format (DD-MM-YYYY): ")
            dob = pd.to_datetime(user_input, format='mixed', dayfirst=True)
            info("DOB entered in correct format!")
            return dob
        except Exception as e:
            error(f"Invalid input entered: {e}")
            print("Invalid input! Please enter the date in the format DD-MM-YYYY.")

def main():
    """
    Main function to execute the script.
    """
    input_url = "https://drive.google.com/uc?id=1AWPf-pJodJKeHsARQK_RHiNsE8fjPCVK&export=download"  # URL to download the CSV file
    file_name = "people-1000.csv"  # Filename for the downloaded CSV file
    
    # Download the CSV file
    download_csv(input_url, file_name)
    
    # Get the date of birth from the user
    dob = get_user_dob()
    
    # Split the CSV file based on the entered date of birth
    split_csv_by_dob(dob, file_name)

if __name__ == "__main__":
    main()
