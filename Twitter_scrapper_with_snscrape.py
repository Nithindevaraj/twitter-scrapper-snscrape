import snscrape.modules.twitter as sntwitter
import pandas as pd
from pymongo import MongoClient
from datetime import datetime, timedelta
import streamlit as st

def get_twitter_data(keyword, start_date, end_date, tweet_limit):
    tweet_date = datetime.strptime(end_date, "%Y-%m-%d")
    tweet_range = timedelta(days=tweet_limit)
    tweet_list = []
    while tweet_date > datetime.strptime(start_date, "%Y-%m-%d"):
        since_date = (tweet_date - tweet_range).strftime('%Y-%m-%d')
        until_date = tweet_date.strftime('%Y-%m-%d')
        for i, tweet in enumerate(sntwitter.TwitterSearchScraper(f'{keyword} since:{since_date} until:{until_date}').get_items()):
            if i > tweet_limit:
                break
            tweet_list.append([tweet.date, tweet.id, tweet.url, tweet.content, tweet.user.username, tweet.replyCount,
                               tweet.retweetCount, tweet.lang, tweet.source, tweet.likeCount])
        tweet_date -= tweet_range
    return tweet_list

def store_mongodb(tweet_list, collection_name):
    db_url = 'mongodb+srv://nitindevarg:<password>@cluster0.xrn8ge5.mongodb.net/?retryWrites=true&w=majority'
    client = MongoClient(db_url)
    db = client.get_database('twitter_scrape_db')
    collection = db[collection_name]
    for tweet in tweet_list:
        tweet_data = {"date": tweet[0], "id": tweet[1], "url": tweet[2], "tweet-content": tweet[3],
                      "user": tweet[4], "reply-count": tweet[5], "retweet-count": tweet[6], "language": tweet[7],
                      "source": tweet[8], "like-count": tweet[9]}
        collection.insert_one(tweet_data)
    client.close()

def main():
    st.title("Twitter Scraper with snscrape")

    keyword = st.text_input("Enter a hashtag or keyword to search")
    start_date = st.date_input("Enter the start date of search")
    end_date = st.date_input("Enter the end date of search")
    tweet_limit = st.number_input("Enter the limit of tweets to scrape")

    if st.button("Scrape Data"):
        tweet_list = get_twitter_data(keyword, str(start_date), str(end_date), tweet_limit)
        st.write(pd.DataFrame(tweet_list, columns=["date", "id", "url", "tweet-content", "user", "reply-count",
                                                    "retweet-count", "language", "source", "like-count"]))
        if st.button("Store Data"):
            store_mongodb(tweet_list, keyword)
            st.write("Data stored in MongoDB!")
        if st.button("Download Data"):
            df = pd.DataFrame(tweet_list, columns=["date", "id", "url", "tweet-content", "user", "reply-count",
                                                   "retweet-count", "language", "source", "like-count"])
            st.download_button(
                label="Download as CSV",
                data=df.to_csv(index=False),
                file_name=f"{keyword}.csv",
                mime="text/csv"
            )
            st.download_button(
                label="Download as JSON",
                data=df.to_json(orient='records'),
                file_name=f"{keyword}.json",
                mime="application/json"
            )

if __name__ == '__main__':
    main()