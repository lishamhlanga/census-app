# Project 3 Python

# Employee Management System

  This CLI pthon project is all about the census data of squirrels for 2018 form the Central Park. The main purpose is to help users to analyse data better and easily and maintain their employee details eg like the accounts/finance department to manage to easily create and add and view and update employees from the same screen. check the updated data and print it to the terminal.


# Features

- Users will be able to view the following
   . They will be able to create new employee details
   . Able to view the created employee
   . They will be able to update the employees details
   . be able to get all the employee list
   . Update the details of the employee using the Id as a key
   . Remove the employee from the file as well
   . Error checking and alerts if user inputs wrong data
   
# How it works
   . The app runs from Heroku 
   . The user is greeted with a welcome screen
   . Presented with 5 choice for now 
   . 1 > add new employee
   . 2 > get all employee list
   . 3 > get employee by id
   . 4 > update employee by Id 
   . 5 > remove employee by Id
   . 6 > search employee by id ( feature update )
   
   . To login please create a new registration
         Enter any information on the username and password
         Then register as a new user, type Y to register 
# Code Verification
  
  <http://pep8online.com/>

# Creating google sheet and APIs

 . The project is deployed on github as well on Heroku.
 . This is a backend application
 . The Employee management system uses google sheets and google drive which are enabled on the google console to allow     changes to the worksheet.
 . The application uses API (Application Program Interface ) to enable push and pull of data from the google sheets

## Procedure

  1. import CSV from to goodle drive
  2. Name the google Sheet
  or create a new google sheet
  3. link to google console platform <https://console.cloud.google.com/home/dashboard?project=squirrelcensus>
  4. Steps to get your credentials file for users with the "new" form UI:
From the "Which API are you using?" dropdown menu, choose Google Drive API
For the "What data will you be accessing?" question, select Application Data
For the "Are you planning to use this API with Compute Engine, Kubernetes Engine, App Engine, or Cloud Functions?" question, select No, I'm not using them

Click Next

Enter a Service Account name, you can call it anything you like - I will call mine "squirrielscensus" - then click Create

In the Role Dropdown box choose Basic > Editor then press Continue

These options can be left blank, click Done

On the next page, click on the Service Account that has been created

On the next page, click on the Keys tab

Click on the Add Key dropdown and select Create New Key
Select JSON and then click Create. This will trigger the json file with your API credentials in it to download to your machine.

 Link to gitpod template <https://github.com/Code-Institute-Org/python-essentials-template>

Now we’ll add our credentials file that we downloaded in the previous video, locate
the json file wherever it is within your computer files, mine is in my downloads folder, and
simply drag and drop it into your Gitpod workspace.
And to make our lives a little easier when we
come to access this file in the next video, we’ll rename it to creds.json.
Now let’s open up our json file and take a look at it. The colors here make it look
like we have an error in our code, but this is just Gitpod being unhappy about the length
of our private_key value, the code is actually valid. What we want to do is find our client_email
value here, and copy this email address generated for our credentials. Copy it without the quotes around it.
And then we’ll go back to our spreadsheet and click the share button here,
paste in our client email, make sure “Editor” is selected, untick “Notify People”, and then click "share".
This tells the sheet to allow our project to access and edit it.
Now, as our creds.json file contains sensitive information that should be kept secret,
we need to ensure that this file is never committed or sent to Github. So how do we do that?
Well, you may have noticed this .gitignore file here when you created your workspace
from our template. This file contains a list of files that should not be committed or sent to Github.
For the purposes of our template, it already contains a few files and folders,
and we're going to add one more in here to protect our creds.json file, and then save the file with CTRL-S.

# Deployment

- code must be placed in the `run.py` file
- dependencies must be placed in the `requirements.txt` file
## Creating the Heroku app

When creating the app, added two buildpacks from the _Settings_ tab. T

1. `heroku/python`
2. `heroku/nodejs`

3. created a _Config Var_ called `PORT`. Set this to `8000`

4. Credentials, such as in the Employee Management System project, I created another _Config Var_ called `CREDS` and pasted the JSON into the value field.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.
# Future Updates
. Add ability to search for employees
. The google sheets more rows and columns to be added through the app itself and updated on the google sheet
. To add a user login and pasword to protect the app from being misused and as it contains sensitive information it must adhere to GDPR laws
. The google sheets currently 3 worksheets , empdetails, hours worked,  and weekly salary.
. Also to incorporate emailing to the user details like weekly hours and weekly salary and othe important stuff for the employees.
. More functionality to be added , like start date as well, eg View start date, View next to Kin- in case of emergencies, View employee phone numbers, Request on file from employees, icorporate pdf and create a template for the pay slip as well that to be emailed.
# Difficulties

. I encontered a lot of difficulties especially with Gitpod, Initially i had done a car game project done and dusted working great from vscode and pycharm, I then tested it on Gitpod and it never worked, the tutor assistance they said Gitpod does not support Tkinter as part of the game was graphical. So i was faced with choices of what to do . I then moved to a Employee management system and time was the downside . It connects to google sheets well but there were few issues so I coded for the app to operate independently. Then an issue of not commiting the handler issues pull issues of which it was solved but left me with minimal time. see below >

! [rejected] main -> main (non-fast-forward)
error: failed to push some refs to <https://github.com/lishamhlanga/employeedata.git>
hint: Updates were rejected because the tip of your current branch is behind
hint: its remote counterpart. Integrate the remote changes (e.g.
hint: 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.
gitpod /workspace/employeedatdata (main) $



The commits all I had done never went through only last resort was to just code most of it and then deploy
# Credits 
. Credit goes to the lesson from code institude
. Slack
. Student Support
. stack exhange
. youtube channel <https://www.youtube.com/watch?v=4ssigWmExak>

