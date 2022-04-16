# Project 3 Python

# Employee Management System

  This CLI pthon project is all about the census data of squirrels for 2018 form the Central Park. The main purpose is to help users to analyse data better and easily and maintain their employee details. 

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
   .
   .
   .
   .
   .
   .
   .
   .
   .
   .
   .
   .
   .
   .

# Code Verification
  
  <http://pep8online.com/>

# Creating google sheet and APIs

 . The project is deployed on github as well on Heroku.
 . This is a backend application
 . The census uses google sheets and google drive which are enabled on the google console to allow changes to the worksheet.
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
