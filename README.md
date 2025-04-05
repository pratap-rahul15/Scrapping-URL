# Smarter.Codes Scrapping URL

**Instructions for setting up and running the project locally.**

1 -  Clone the project into your local - git clone https://github.com/pratap-rahul15/Scrapping-URL.git

2 -  After cloning, there will be 2 main folders **client(frontend)** and **server(backend)**

3 - Before installing 

   ***Prerequisite***
   ---
   - Install the dependencies to run the front-end -> client folder
     
   - To install it, open your terminal and run the command - **npm install**, it will install all the necessary libraries & dependencies mentioned in the **package.json**

   - To run the front end use the command - **npm run dev**, the server will start locally -  http://localhost:5173/

   - Now, install the dependencies to run the back-end -> server folder

   - To install it, open your terminal and run the command— **pip install—r requirements.txt**. This will install all the necessary libraries and dependencies mentioned in the **requirements.txt** file.

   - Before running the back end, start the docker as I have installed the vector database *Weaviate* on the *Docker compose*, spin it up using the - **docker-compose -f weaviate-client.yml up --build -d**

   - When you docker spins-up start the backend, as I have used the python *FAST API* for the back-end so to run it use the command - **uvicorn app.main:app --reload**
