# twitter-scrapper-snscrape
this is a program to scrape data from twitter and store it in mongodb and download it in json,csv files.
Twitter Scraper with snscrape and MongoDB Atlas

This project is a Twitter scraper that uses snscrape to collect tweets based on a user-defined keyword and date range. The scraped tweets are then stored in a MongoDB Atlas database.
Setup
Install dependencies
To install the necessary dependencies, run the following command:

pip install snscrape pymongo streamlit pandas

Create a MongoDB Atlas cluster
To use MongoDB Atlas, you must first create a free account on the MongoDB website. Once you have created 
an account, follow these steps to create a new cluster:

1.Log in to the MongoDB Atlas dashboard.
2.Click the "Create a new cluster" button.
3.Choose your preferred cloud provider, region, and cluster tier.
4.Customize your cluster settings (optional).
5.Click the "Create Cluster" button.
Once your cluster is created, you will need to create a new database and collection to store the scraped tweets.


Configure the script
Before running the script, you will need to update the MongoDB connection string and collection name in the store_mongodb function. To do this, replace the MONGODB_CONNECTION_STRING and COLLECTION_NAME variables with your own values.



Run the script
To run the script, simply run the following command:

streamlit run python twitter_scraper.py

This will start a Streamlit app that allows you to enter your search parameters and scrape tweets based on your input.
