# Splitting Dataset Assignment
The project simply downloads the provided dataset and splits the given dataset file into two dataset files on the basis of Date of Birth provided by the user. One dataset file contains the records with Date of Birth below the provided date, and the other contains the records with Date of Birth above the provided date. All the logs and errors and logged in the log file for the user as well. 
This project is written in Python.

## Setting Up the Project

### Step 1: Create a Virtual Environment
First, navigate to your project's root directory in the terminal. Then create a virtual environment by executing the following command:

```
python -m venv myenv
```
### Step 2: Activate the Virtual Environment
To activate your virtual environment, execute the following command:

```
.\myenv\Scripts\activate
```
### Step 3: Install the required packages
For this project, we require pandas, requests and logging packages. These packages can be installed by executing the following command:

```
pip install pandas logging requests
```
### Step 4: Run the project file
To activate the project file, execute the following command:

```
python assgn1.py
```