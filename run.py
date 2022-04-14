import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('weather')

week = SHEET.worksheet("week1")
data = week.get_all_values()
print(data)

def get_weekly_data():   
    
    print("Please enter missing weekly data for week1: ")
    print("Data should be day, temp, condition separated by commas")
    print("Example : Monday, 10, Cloudy\n")

    data_str = input ("Please enter missing weekly data:\n")
    #print(f"The data provided is\n {data_str}")
    weekly_data = data_str.split(",")
    check_data(weekly_data)
    #print(data_str)

def check_data(values):
    try:
        if len(values) != 3:
            raise ValueError(f"3 values required , you provided {len(values)}")
    except ValueError as e:
        print(f"Invalid data: {e}, please re-try.\n")

get_weekly_data()

