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



# Installation

To install and run this program, please follow the step-by-step instructions provided below:

## Step 1: Clone the repository to your local machine
1. Open GitHub and navigate to the main page of the repository.
2. Click on the "Code" button.
3. Copy the repository URL.
4. Open your terminal or command prompt on your local machine.
5. Navigate to the directory where you want to clone the repository.
6. Run the following command and replace `<repository-url>` with the URL you copied in step 3:
   ```
   git clone <repository-url>
   ```

## Step 2: Set up `.env` file
1. Inside the cloned repository folder (named "dynamic-frcm-group2"), create a new file named `.env`.
2. Open the `.env` file in a text editor.
3. Add the necessary credentials, such as the ID and password for MET-access, in the following format:
   ```
   MET_ACCESS_ID=your-access-id
   MET_ACCESS_PASSWORD=your-access-password
   ```
   Replace `your-access-id` and `your-access-password` with your own credentials.

## Step 3: Open the repository in VS Code
1. Open Visual Studio Code on your local machine.
2. Go to "File" > "Open Folder".
3. Navigate to the cloned repository folder ("dynamic-frcm-group2") and click "Open".

## Step 4: Navigate to the correct path/folder
1. In Visual Studio Code, open the integrated terminal by going to "View" > "Terminal".
2. Ensure that the terminal is pointing to the correct path/folder. It should be the root of the repository ("dynamic-frcm-group2").

## Step 5: Install project dependencies with Poetry
1. In the terminal, run the following command:
   ```
   poetry install
   ```
   This will install all the necessary dependencies for the project based on the `pyproject.toml` file.

## Step 6: Run the program
1. In the terminal, run the following command:
   ```
   poetry run python src/main.py
   ```
   This will start the program and it will be running on your local machine.

## Step 7: Access the program
1. Open your web browser.
2. Enter the following URL in the address bar: [http://localhost:8000](http://localhost:8000).
3. The program should now be accessible in your web browser.

## Step 8: Login to the program
1. In the login page that appears, enter the username "markus" and password "scrum" in the respective fields.
2. Click the "Login" or "Submit" button to proceed.

## Step 9: Use the program
1. Once logged in, you will be directed to the program's main interface.
2. Enter the desired location/address in the appropriate field.
3. Click the "Get coordinates" button to retrieve the coordinates for the location.

That's it! You have successfully installed and set up the program on your local machine. You can now use it as per your requirements.
