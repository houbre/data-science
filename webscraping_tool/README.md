Data scraping tool that scrapes the top 5 trending articles from the homepage of the Montreal Gazette (https://montrealgazette.com/category/news/), pulls out the title, publication date, author and blurb and formats these into a json file of the format:

 [
  {
   “title”: “article title”,
 		“publication_date”: “date”,
 		“author”: “author”,
 		“blurb”: “blurb”
  },
  {
  ...
  }
 ]

From the webscraping_tool directory, collect_trending.py is called like so:
 
  $ python collect_trending.py -o out.json 
