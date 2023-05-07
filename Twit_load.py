from dotenv import dotenv_values
import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt
import requests
import json
import warnings
# warnings.filterwarnings('ignore') # We can suppress the warnings
# my twitter keys are stores in a file outside the git repository for security reasons
config = dotenv_values("/Users/ambrosedesmond/CCT_Projects/Ambrose_MSC_DS_CA2/.env")
bearer_token = config["BEARER_TOKEN"]
# this is the location of the twitter api access , looking for the most recent tweets
search_url = "https://api.twitter.com/2/tweets/search/recent"

# Im using two query_params the first is without the next_token field for the first query 
start_time = "2023-05-02T00:00:00Z"
end_time = "2023-05-05T00:00:00Z"
query_params1 = {f'query':'Russian war -is:retweet',
    'start_time':{start_time},
    'end_time':{end_time},
    'max_results': '100',
    'tweet.fields':'author_id',
    'user.fields':'name',

}
# This second query is for the loop , as it requires a next_token.
query_params2 = {f'query':'Russia war -is:retweet',
    'start_time':{start_time},
    'end_time':{end_time},
    'max_results': '100',
    'tweet.fields':'author_id',
    'user.fields':'name',
    'next_token' : 'abcd',
}

# my authorisation keys are used here for the twitter API
def bearer_oauth(r):
    """ Function for using bearer token"""
    r.headers['Authorization'] = f"Bearer {bearer_token}"
    r.headers['User-Agent'] = "v2RecentSerchPython"
    return r


def connect_to_endpoint(url,params):
    """ Function to connect to twitter API"""
    response = requests.get(url,auth=bearer_oauth, params=params)
    #responce.status_code 200 is good anything else is an error
    
    return response.json()

def append_dict(adict,json_response):
    for i in range(len(json_response['data'])):
        try:
            adict[json_response['data'][i]['author_id']] = json_response['data'][i]['text']

        except IndexError:
            print("We had an index error")
    return(adict)

    
def twit_call():
    twit_dict={}
    loop_count = 0
    json_response = connect_to_endpoint(search_url, query_params1)
    print(json_response)

    append_dict(twit_dict,json_response)
    # while json_response['meta']['next_token']:
    while True:
        # pagenation is taking the next_token and feeding it through to next query
        if 'next_token' in json_response['meta']:
            print("Yes next token")
            next_t = json_response['meta']['next_token']
            query_params2['next_token'] = next_t
        else:
            # this is the last page
            break
        json_response = connect_to_endpoint(search_url, query_params2)
        append_dict(twit_dict,json_response)
           
    return(twit_dict)

my_dict = twit_call()

# convert dictionary to dataframe
df = pd.DataFrame.from_dict(my_dict, orient='index',columns=['tweets'])

df.to_csv('Russia_War_TWEETS_2.csv')
