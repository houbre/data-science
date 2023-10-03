A python command line tool using the following dataset "https://data.cityofnewyork.us/Social-Services/311-Service-Requests-from-2010-to-Present/erm2-nwe9".

-> python complaint_borough.py -i nyc_data.csv -s start_date -e end_date -o ouput_file

The start and end dates have to be of format YYYY-MM-DD.

the output file is optional. No output argument and lines are printed on the terminal.

The output will be printed in the follwing csv format:
    complaint type, borough, count
	derelict vehicles, Queens, 236
	derelict vehicles, Bronx, 421
                .
                .
                .