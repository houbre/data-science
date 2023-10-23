import argparse
import json
import requests
import datetime




def parseArguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-k", "--APIKEY", required=True, help="API key")
    parser.add_argument("-b", "--lookback", help="Specify the number of days to look back")
    parser.add_argument("-i", "--input", required=True, help="Specify the input file  (a list of dictionaries)")
    parser.add_argument("-o", "--output", required=True, help="specify the output directory for the json file")
    
    args =  parser.parse_args()

    return args

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

    return data
    


def main():

    args = parseArguments()

    API_KEY = args.APIKEY

    with open(args.input, "r") as json_file:
        data = json.load(json_file)
       
    for name in data:

        Keywords = data[name]

        if (args.lookback is not None):
            
            api_call_data = fetch_latest_news(API_KEY, Keywords, args.lookback)

            json_string = json.dumps(api_call_data, indent=4)

            with open(f'output_dir/{name}.json', 'w') as f:
                f.write(json_string)

        else:
            api_call_data = fetch_latest_news(API_KEY, Keywords)

            json_string = json.dumps(api_call_data, indent=4)

            with open(f'output_dir/{name}.json', 'w') as f:
                f.write(json_string)




if __name__ == '__main__':
    main()