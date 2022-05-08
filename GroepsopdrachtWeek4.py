import tweepy as tp
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import itertools
import collections
import textblob
from textblob import TextBlob
import os
import nltk
from nltk.corpus import stopwords
import pycountry
import re
import string
import networkx

import sys
import matplotlib.pyplot as plt
import numpy as np
import json
import requests

import warnings
warnings.filterwarnings("ignore")

sns.set(font_scale=1.5)
sns.set_style("whitegrid")

# consumer_key = "gy8qOgm0gHteI1qXLeVDuDlub"
# consumer_key_private = "bbwhmpswqnBUYCaVY7Ob376fp8JxXZBPoNT04j1GlMZJnrMQFK"

# access_token = "1320072218764840967-MwlsT99Myns1jaV6cxL3kXdAZzBvBa"
# access_token_secret="4FbBu81heV9ysTxCOCTZqqYYcZRIQ9sAuGFfHFl5Fa1bt"

bearer = "AAAAAAAAAAAAAAAAAAAAANiRawEAAAAAfKNPCYMcniELb5kd8juRmgEuuCo%3D2aNn5aDumryhqQVqXtxLeVL3T7v0dJD3p18tRbJtehWIWbzTAF"


# client = tp.Client(
#     consumer_key=consumer_key, consumer_secret=consumer_key_private,
#     access_token=access_token, access_token_secret=access_token_secret
# )

client = tp.Client(bearer)

enList = []
zoekWoord = "#abortion"

response = client.search_recent_tweets(query = zoekWoord, tweet_fields="lang", place_fields="contained_within,country,country_code,full_name,geo,id,name,place_type" ,max_results=25)

for tweet in response.data:

    if(tweet.lang == "en"):
        enList.append(tweet.text)

    
    for tweet in enList:
        print(tweet)

def verwijderLidWoorden(unorderedList):
    for tweet in unorderedList:
        tweet = tweet.lower()
        tweet = tweet.replace(" the ", "")
        tweet = tweet.replace(" a ", "")
        tweet = tweet.replace(" an ", "")
        print(tweet)



def haalWoordFrequentyOp(orderedList):
    all_tweets = orderedList

    all_tweets[:5]

    # definieer de methode om urls uit de tweet te verwijderen
    def remove_url(txt):
        return " ".join(re.sub("([^0-9A-Za-z \t])|(\w+:\/\/\S+)", "", txt).split())

    # verwijder de urls en stop de tweets zonder url in een lijst
    all_tweets_no_urls = [remove_url(tweet) for tweet in all_tweets]
    all_tweets_no_urls[:5]

    # split de woorden van een tweet in unieke elementen en maak deze lowercase
    all_tweets_no_urls[0].lower().split()

    # maak een lijst van lijsten die lowercase woorden bevatten voor elke tweet
    words_in_tweet = [tweet.lower().split() for tweet in all_tweets_no_urls]
    words_in_tweet[:2]

    # maak een lijst van alle woorden uit alle tweets
    all_words_no_urls = list(itertools.chain(*words_in_tweet))

    # maak een counter
    counts_no_urls = collections.Counter(all_words_no_urls)

    print(counts_no_urls.most_common(15))

    # stop de schone tweets zonder urls in een dataframe en toon deze op het scherm
    clean_tweets_no_urls = pd.DataFrame(counts_no_urls.most_common(15),
                                columns=['words', 'count'])

    clean_tweets_no_urls.head()# stop de schone tweets zonder urls in een dataframe en toon deze op het scherm
    clean_tweets_no_urls = pd.DataFrame(counts_no_urls.most_common(15),
                                columns=['words', 'count'])

    print(clean_tweets_no_urls.head())

    # plot de horizontale grafiek
    fig, ax = plt.subplots(figsize=(8, 8))

    clean_tweets_no_urls.sort_values(by='count').plot.barh(x='words',
                        y='count',
                        ax=ax,
                        color="purple")

    ax.set_title("Common Words Found in Tweets (Including All Words)")

    plt.show()


verwijderLidWoorden(enList)
haalWoordFrequentyOp(enList)
