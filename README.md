# Splitting Dataset Assignment

The project downloads the provided dataset and splits it into two dataset files based on the Date of Birth provided by the user. One dataset file contains the records with Date of Birth below the provided date, and the other contains the records with Date of Birth above the provided date. All logs and errors are logged in the log file for the user. This project is written in Python.

## Setting Up the Project

### Step 1: Create a Virtual Environment
First, navigate to your project's root directory in the terminal. Then create a virtual environment by executing the following command:

```
python -m venv myenv
```

### Step 2: Activate the Virtual Environment
To activate your virtual environment, execute the following command:

- On Windows:
```
.\myenv\Scripts\activate
```
- On macOS/Linux:
```
source myenv/bin/activate
```

### Step 3: Install the Required Packages
For this project, we require the `pandas`, `requests`, and `logging` packages. These packages can be installed by executing the following command:

```
pip install pandas requests
```

### Step 4: Run the Project File
To run the project file, execute the following command:

```
python assgn1.py
```

## Project Description

The project consists of the following main components:

- `download_csv(url, filename)`: Downloads a CSV file from the given URL and saves it with the given filename.
- `split_csv_by_dob(dob, filename)`: Splits the CSV file into two separate files based on the given date of birth.
- `get_user_dob()`: Prompts the user to enter a date of birth and converts it to a datetime object.
- `main()`: The main function to execute the script.

### Logging

All logs and errors are recorded in a log file named `logFile.log` located in the project's root directory.

### CSV File

The project uses a sample CSV file available at the URL:
```
https://drive.google.com/uc?id=1AWPf-pJodJKeHsARQK_RHiNsE8fjPCVK&export=download
```

### Running the Script

When you run the script, it will:

1. Download the CSV file.
2. Prompt you to enter a date of birth in the format (DD-MM-YYYY).
3. Split the CSV file into two files based on the entered date of birth:
    - `dob_below.csv`: Contains records with Date of Birth below the provided date.
    - `dob_above.csv`: Contains records with Date of Birth above the provided date.

## Example Usage

```sh
python assgn1.py
```

You will be prompted to enter a date of birth. After entering the date, the script will create two CSV files: `dob_below.csv` and `dob_above.csv` in the project's root directory.

```
Enter Date Of Birth in the format (DD-MM-YYYY):
```

After entering the date, the script will create two CSV files: `dob_below.csv` and `dob_above.csv` in the project's root directory.

```
Download successful! Filename: people-1000.csv
DOB entered in correct format!
Split successful! Files created: dob_below.csv and dob_above.csv
```
