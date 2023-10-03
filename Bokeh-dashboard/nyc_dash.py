from pathlib import Path
import pandas as pd

from bokeh.plotting import curdoc, figure
from bokeh.models import Dropdown, ColumnDataSource
from bokeh.layouts import column


df = None

plot_dataset1 = ColumnDataSource(dict(month=[], time_diff=[]))
plot_dataset2 = ColumnDataSource(dict(month=[], time_diff=[]))
plot_dataset3 = None


def get_path_name(fname):
    return Path(__file__).parent / fname

def load_nyc_dash():

    global df, plot_dataset3

    #Script to calculate the average time difference and group by zipcode and months

    #csv file of the trimmed data containing only the year 2020
    csv_path = get_path_name("nyc_data_top_10000.csv")
    nyc_data_df = pd.read_csv(csv_path)


    #Drop the empty/null end_dates and zipcode
    nyc_data_df.dropna(subset=[nyc_data_df.columns[2]], inplace=True)
    nyc_data_df.dropna(subset=[nyc_data_df.columns[8]], inplace=True)

    #data frame with three columns
    nyc_df2 = nyc_data_df[[nyc_data_df.columns[1], nyc_data_df.columns[2], nyc_data_df.columns[8]]]
    nyc_df2.columns = ['start_time', 'end_time', 'zipcode']

    #convert the start and end time to datetime
    nyc_df2['start_time'] = pd.to_datetime(nyc_df2['start_time'])
    nyc_df2['end_time'] = pd.to_datetime(nyc_df2['end_time'])

    #only keep the months
    nyc_df2['month'] = nyc_df2['start_time'].dt.month

    #calculate the difference in hours
    nyc_df2['time_diff'] = (nyc_df2['end_time'] - nyc_df2['start_time']).dt.total_seconds() / 3600

    #group by months and zipcodes
    df = nyc_df2.groupby(['zipcode', 'month'])['time_diff'].mean().reset_index()

    df2 = df

    df_allzip = df2.groupby(['month'])['time_diff'].mean().reset_index()

    plot_dataset3 = ColumnDataSource(df_allzip)


def update_plot1(event):
    
    #update the data used for the first dropdown

    global plot_dataset1

    new_data = grab_zipcode_data(event.item)
    plot_dataset1.data = new_data

def update_plot2(event):

     #update the data used for the second dropdown

    global plot_dataset2

    new_data = grab_zipcode_data(event.item)
    plot_dataset2.data = new_data


def grab_zipcode_data(some_zipcode):

    global df

    x_range = [1,2,3,4,5,6,7,8,9,10,11,12]

    time_diff_dict = {month: 0 for month in x_range}

    filtered_df = df[df['zipcode'] == float(some_zipcode)]

    for _, row in filtered_df.iterrows():
        time_diff_dict[row['month']] = row['time_diff']

    return {
        "month": x_range,
        "time_diff": [time_diff_dict[month] for month in x_range]
    }


def main():

    global df, plot_dataset1, plot_dataset2, plot_dataset3

    #data prep section
    load_nyc_dash()

    #visualization section
    p = figure(x_axis_label='Months', y_axis_label='Response time (hours)', title='Average monthly Response time by Zipcode')

    p.line(x='month', y='time_diff', color='red', line_width=2, source=plot_dataset1, legend_label='Zipcode 1')
    p.line(x='month', y='time_diff', color='blue', line_width=2, source=plot_dataset2, legend_label='Zipcode 2')
    p.line(x='month', y='time_diff', color='green', line_width=2, source=plot_dataset3, legend_label='All Zipcodes')


    p.legend.location = "top_left"
    

    #create our linechart
    unique_zip = df['zipcode'].astype(str).unique().tolist()
        
    dropdown1 = Dropdown(label="Zipcode1", menu=unique_zip)

    dropdown1.on_event("menu_item_click", update_plot1)

    dropdown2 = Dropdown(label="Zipcode2", menu=unique_zip)
    dropdown2.on_event("menu_item_click", update_plot2)

    curdoc().add_root(column(dropdown1, dropdown2, p))


main()