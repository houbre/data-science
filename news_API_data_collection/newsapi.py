import requests
import json
import datetime

def fetch_latest_news(api_key, news_keywords, lookback_days=10):

    if api_key == None:
        raise Exception('Missing api_key argument')
    
    if news_keywords == None:
        raise Exception('Missing new_keywords argument')

    if (len(news_keywords) == 0):
        raise ValueError()
    
    if (news_keywords == ''):
        raise ValueError()
    
    for keyword in news_keywords:
        if not(keyword.isalpha()):
            raise ValueError()


    date_minus_10 = datetime.date.today() - datetime.timedelta(days=lookback_days)

    keywords_querie = " AND ".join(news_keywords)

    SHOW_QUERY_STRING_TEMPLATE = f"https://newsapi.org/v2/everything?q={keywords_querie}&from={date_minus_10}&sortBy=popularity&apiKey={api_key}"


    response = requests.get(SHOW_QUERY_STRING_TEMPLATE)

    if response.status_code != 200:
        raise Exception('Unable to fetch the news articles')
    
    data = response.json()

    list_of_dict = []

    for key in data['articles']:
        list_of_dict.append(key)

    return list_of_dict


def main():
    None
    #fetch_latest_news(API_KEY, keywords, (optional) lookback days)

if __name__ == '__main__':
    main()