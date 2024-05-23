# FireGuard 
This program is a simple web application that allows users to input an address and recive a calculated FireRisk for the location which indicates time to flashover. It also features login functionality with username and password to access the main functionality.

### Features
Login: The program includes a basic login function that requires a username and password. Upon successful login, users gain access to the main functionality.
Main Page: After logging in, users are redirected to the main page where they can utilize the address to coordinates feature.

Address to Coordinates: Users can input an address into a form, and the program will return the coordinates for the specified address.

### Technologies
- SQlite is used to setup and maintain two databases, one for authentication and one for FireRisk and weather data.
- Flask: The web application is built using Flask, a lightweight web framework for Python.
- Geopy: Geopy library is used to perform geographical searches and retrieve coordinates for a given address.
- Poetry: Used to ensure that all packages are innstalled with correct versions.
- Docker: Containerization and packaging to improve scalabilty.



# Installation
To install and run this program, please follow the step-by-step instructions provided below:
- Install Docker desktop https://www.docker.com/products/docker-desktop/
- Install Postman or another API request tool: https://www.postman.com/downloads/

# Guideline
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

## Step 3: Navigate to the correct path/folder
1. Open terminal and navigate to repositury path folder.
2. Ensure that the terminal is pointing to the correct path/folder. It should be the root of the repository ("dynamic-frcm-group2").

## Step 4: Open Docker desktop on your device.

## Step 5: Build and run Docker container
1. In the terminal, run the following command:
   ```
   docker compose up --build
   ```
   This will build docker image and run the container.

## Step 6: Access the program
1. Open your web browser.
2. Enter the following URL in the address bar: [http://localhost:8000](http://localhost:8000).
3. The program should now be accessible in your web browser.

## Step 7: Login to the program
1. In the login page that appears, enter the username "markus" and password "scrum" in the respective fields.
2. Click the "Login" or "Submit" button to proceed.

## Step 8: Use the program
1. Once logged in, you will be directed to the program's main interface.
2. Enter the desired location/address in the appropriate field.
3. Click the "Get coordinates" button to retrieve the coordinates for the location.

# Using Postman with Docker
If the application is running in Docker, you can also access the API using Postman for GET and POST requests.

## Login
1. Make a POST request to http://localhost:8000/login with the following body parameters:
  -   Username: 'markus'
  -   Password: 'scrum'
2. After a successful login, you can send GET requests to access the main functionality.

## Get Coordinates
1. Use the following GET request http://localhost:8000/coordinates?address=Bergen, replacing 'Bergen' with your desired address.


That's it! You have successfully installed and set up the program on your local machine. You can now use it as per your requirements.
