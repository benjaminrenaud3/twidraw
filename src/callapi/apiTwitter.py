
import string
import requests
import json
import os
import sys

sys.path.append('src/')
from generic.files import create_file

from dotenv import load_dotenv
load_dotenv()

BEARER_TOKEN = os.getenv('BEARER_TOKEN')

def get_inital_data(search: string, pages: int):
    """
    Get the 100 x pages recent tweets from twitter
    Call api with the function arg and check return and if we have more than 100 tweet
    Call api with token for each pages
    Stock result in file in json format
    Args:
        search: word to search in tweet
        pages: int to get n x 100 recent tweet
    """

    query = search + " -is:retweet"
    tweet_fields = "tweet.fields=id,text,geo,created_at,lang,public_metrics,source"
    count = 100
    # expansions = "expansions=author_id"
    # user = "user.fields=created_at,description,entities,id,location,name,pinned_tweet_id,profile_image_url,protected,public_metrics,url,username,verified,withheld"

    bearer = BEARER_TOKEN
    headers = {"Authorization": "Bearer {}".format(bearer)}

    # url = f"https://api.twitter.com/2/tweets/search/recent?query={query}&{tweet_fields}&{expansions}&{user}&max_results={count}"
    url = f"https://api.twitter.com/2/tweets/search/recent?query={query}&{tweet_fields}&max_results={count}"
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)

    result = response.json()
    result_count = result["meta"]["result_count"]

    if result_count < 100:
        create_file("src/files/data.json", result)
        return
    else:
        token = result["meta"]["next_token"]

    for i in range(pages):
        url = f"https://api.twitter.com/2/tweets/search/recent?query={query}&{tweet_fields}&next_token={token}&max_results={count}"
        response2 = requests.get(url, headers=headers)
        if response2.status_code != 200:
            raise Exception(response2.status_code, response2.text)

        if "next_token" in response2.json()["meta"]:
            token = response2.json()["meta"]["next_token"]
            result["data"] += response2.json()["data"]
            result_count += 100
        else:
            break

    result["meta"]["result_count"] = result_count
    create_file("src/files/data.json", result)
    return



if __name__ == '__main__':
    get_inital_data("france", 2)



