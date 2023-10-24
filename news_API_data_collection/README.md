This homework covers data collection using web APIs.

Using the News API available at newsapi.org , the goal of this assignemnt was to create a top-level python package containing the following:
	-> newsapi.py : 
        Fetches the latest news with the function 'fetch_latest_news(api_key, news_keywords, lookback_days=10)' which
        which queries the NewsAPI and returns a python list of english news articles (represented as dictionaries) 
        containing those news keywords and published within the last <lookback_days>.

  -> tests.newsapi module :
        Unit tests that test the newsapi module

  -> collector.py :
        CLI tool, when given a json file of the following format '{ “trump_fiasco”: [“trump”, “trial”], “swift”: [“taylor”, “swift”, “movie”] }'
        For each keyword set with name N and keyword list X, the collector will execute a query for the keywords X and write the results to the <output_dir>/N.json.

        collector.py can be called like this: Python -m newscover.collector -k <api_key> [-b <# days to lookback>] -i <input_file> -o <output_dir>
        
