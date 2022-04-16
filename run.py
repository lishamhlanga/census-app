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
SHEET = GSPREAD_CLIENT.open('empdata')

week = SHEET.worksheet("empDets")
data = week.get_all_values()

class Employee:
    employeeList = list()
    #count = 0
    def __init__(self, empNo, empName, empDes, empSal):
        self.empNo, self.empName, self.empDes, self.empSal = empNo, empName, empDes, empSal
    def addNewEmployee(self):
        Employee.employeeList.append(self)
    def getEmpList(self):
            return Employee.employeeList
    def getEmpById(self, empNo):
        for emp in Employee.employeeList:
            if(emp.getEmpNo() == empNo):
                return emp
        return False
    def updateEmpById(self, empNo, empName, empDes, empSal):
        for emp in Employee.employeeList:
            if(emp.getEmpNo() == empNo):
                emp.empNo, emp.empName, emp.empDes, emp.empSal = empNo, empName, empDes, empSal
                return True
            return False

    def removeEmpById(self, empNo):
        for emp in Employee.employeeList:
            if(emp.getEmpNo() == empNo):
                Employee.employeeList.remove(emp)
                return True
            return False


    def setEmpNo(self, empNo):
            self.empNo = empNo
    def getEmpNo(self):
            return self.empNo

    def setEmpName(self, empName):
            self.empName = empName
    def getEmpName(self):
            return self.empName

    def setEmpDes(self, empDes):
            self.empDes = empDes
    def getEmpNo(self):
            return self.empDes

    def setEmpSal(self, empSal):
            self.empSal = empSal
    def getEmpSal(self):
            return self.empSal

    def __str__(self):
           return "%d %s %s %d" % (self.empNo, self.empName, self.empDes, self.empSal)

choice = 1
employee = Employee(0, "", "", 0.0)
while choice >= 1 and choice <= 5:
    print("\n\n1. Add New Employee\n2. Get All Employee List\n3. Get Employee By Id\n4. Update Employee By Id\n5. Remove Employee By Id\n\n")
    choice = int(input("Enter Your Choice:" ))
    if(choice == 1):
        empNo =int(input("Enter Employee No : "))
        empName = input("Enter Employee Name : ")
        empDes = input("Enter Employee Designation : ")
        empSal = float(input("Enter Employee Salary : "))
        emp = Employee(empNo, empName, empDes, empSal)
        emp.addNewEmployee()

    elif(choice == 2):
        print("\n")
        for emp in employee.getEmpList():
               print(emp)

    elif(choice == 3):
        empNo = int(input("Enter Emplyee No " ))
        emp = employee.getEmpById(empNo)
        if(emp == False):
            print("\nSorry..! Employee Not Found For ID : ", empNo)
        else:
            print(emp)

    elif(choice == 4):
        empNo = int(input("Enter Employee No : "))
        empName = input("Enter Employee Name : ")
        empDes = input("Enter Employee Designation : ")
        empSal = float(input("Enter Employee Salary : "))
        emp = employee.updateEmpById(empNo, empName, empDes, empSal)
        if (emp == False):
            print("\nSorry..! Update Failed , Employee Not Found for Id : " , empNo)
        else:
            print("Successfully Updated Employee For Id ", empNo)

    elif(choice == 5):
        empNo = int(input("Enter Employee Id : "))
        emp = employee.removeEmpById(empNo)
        if(emp == False):
            print("\nSorry..! Delete Failed , Employee Not Found for Id : ", empNo)
        else:
            print("Successfully Deleted Employee For Id ", empNo)




"""
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
"""
