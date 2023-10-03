Bokeh dashboard to evaluate the difference in response time to complaints filed through the 311 service by zipcode.

The dataset used is from the website "https://data.cityofnewyork.us/Social-Services/311-Service-Requests-from-2010-to-Present/erm2-nwe9" and is trimmed only containg the data from 2020.

The csv file used was trimmed to allow its import on Github.

The dashboard displays:
    - The average monthly response, regardless of the zipcode
    - The average monthly response of Zipcode1 (selected in the dropdown option "Zipcode1")
    - The average monthly response of Zipcode2 (selected in the dropdown option "Zipcode2")


-> $ python -m bokeh serve --show nyc_dash.py