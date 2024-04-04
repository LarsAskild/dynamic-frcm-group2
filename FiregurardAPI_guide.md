# Program Name
This program is a simple web application that allows users to convert an address to coordinates (latitude and longitude). It also features login functionality with username and password to access the main functionality.

### Features
### Address to Coordinates: Users can input an address into a form, and the program will return the coordinates for the specified address.
### Login: The program includes a basic login function that requires a username and password. Upon successful login, users gain access to the main functionality.
### Main Page: After logging in, users are redirected to the main page where they can utilize the address to coordinates feature.
### Technologies
### Flask: The web application is built using Flask, a lightweight web framework for Python.
### Geopy: Geopy library is used to perform geographical searches and retrieve coordinates for a given address.
### HTML/CSS/JavaScript: The frontend of the application is constructed using these web technologies to create a user-friendly interface.

# Installation
1. Clone the repository to your local machine.
2. Make sure to include your own .env file containing ID and password for MET-access in the main repostiry folder "dynamic-frcm-group2".
3. Open the repository in VS code and make sure that you are in the correct path/folder.
4. Open the terminal in VS code.
5. Run command: "Poetry install"
6. Run command: "Poetry run python src/main.py"
7. Open your web browser and navigate to http://localhost:8000 to use the program.
8. Enter username "markus" and password "scrum"
9. Enter desired location/adress and click "Get coordinates"
