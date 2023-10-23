import datetime

def check_dates(some_list : list) -> bool:
    for aList in some_list:
        if (datetime.datetime.strptime(aList['publishedAt'], "%Y-%m-%dT%H:%M:%SZ")).date() < (datetime.date.today() - datetime.timedelta(days=10)):
            return False
        
    return True

        







