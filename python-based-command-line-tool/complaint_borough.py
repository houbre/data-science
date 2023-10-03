import sys
import argparse
from datetime import datetime, date
import csv

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", required=True, help="Input csv file")
    parser.add_argument("-s", "--start_date", required=True, help="Input start date (YYYY-MM-DD)")
    parser.add_argument("-e", "--end_date", required=True, help="Input end date (YYYY-MM-DD)")
    parser.add_argument("-o", "--output", help="Output file (optional)")

    args =  parser.parse_args()

    return args

def complaints_count(input_file, start_date, end_date):

    complaint_count = {}

    start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
    end_date = datetime.strptime(end_date, "%Y-%m-%d").date()

    with open(input_file, "r") as csvfile:
        file = csv.reader(csvfile)

        count = 0

        for row in file:

            creation_date = datetime.strptime(row[1], "%m/%d/%Y %H:%M:%S %p").date()

            if start_date <= creation_date <= end_date:
                complaint_type = row[6]
                borough = row[25]
                complaint_count[(complaint_type, borough)] = complaint_count.get((complaint_type, borough), 0) + 1

    return complaint_count



def main():

    args = parse_arguments()

    complaint_count = complaints_count(args.input, args.start_date, args.end_date)

    if args.output is not None:
        with open(args.output, "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["complaint_type", "borough", "count"])
            for (complaint_type, borough), count in complaint_count.items():
                if complaint_type == '':
                    complaint_type = 'unspecified'
                if borough == '':
                    borough = 'unspecified'
                writer.writerow([complaint_type, borough, count])

    else:

        print("complaint type, ", end="")
        print("borough, ", end="")
        print("count")

        for (complaint_type, borough), count in complaint_count.items():

            if complaint_type == '':
                complaint_type = 'unspecified'
            if borough == '':
                    borough = 'unspecified'

            print(complaint_type, end="")
            print(", ", end="")
            print(borough, end="")
            print(", ", end="")
            print(count)


if __name__ == "__main__":

    main()