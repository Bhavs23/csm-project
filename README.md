Article CMS – Flask Web Project

This is my implementation of the Article CMS project for the Udacity Azure Cloud Developer course. The application is built with Python and Flask and allows users to log in, create articles, upload images, and view posts. The article text is stored in Azure SQL Database, and the uploaded images are stored in Azure Blob Storage. I also added Microsoft authentication using MSAL and included logging for successful and failed logins.

Features Implemented

Admin login using the default credentials

“Sign in with Microsoft” authentication

Create and edit articles

Image upload to Azure Blob Storage

Storage of article data in Azure SQL Database

Logging for login success and failed attempts

Application deployed to Azure App Service

Azure Services Used

Azure Resource Group

Azure SQL Database + SQL Server

Azure Storage Account (Blob)

Azure App Service

Microsoft Entra App Registration

Log Stream for monitoring

How to Run the Project Locally

Clone the repository

Install dependencies using:

pip install -r requirements.txt


Set environment variables for SQL and Blob Storage

Run the app:

python application.py


Open the browser at

http://localhost:5000

Deployment

I deployed the project on Azure App Service because it is easier, cheaper, and more beginner-friendly compared to a Virtual Machine. Deployment was done using GitHub integration in the Deployment Center.

Screenshots Included in My Submission

Deployed app with URL

Created article (“Hello World!”)

Azure Resource Group

SQL tables and data

Blob Storage endpoint

Redirect URIs (MSAL)

Log Stream showing successful and failed login attempts

Note

This project was created as part of my learning process, and the goal was to understand Azure App Service, Azure SQL, Blob Storage, and authentication using MSAL.
