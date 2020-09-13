#!/usr/bin/env python3
"""
This example assumes the JSON data is saved one line per timestamp (message from server).

It shows how to read and process a text file line-by-line in Python, converting JSON fragments
to per-sensor dictionaries indexed by time.
These dictionaries are immediately put into Pandas DataFrames for easier processing.

Feel free to save your data in a better format--I was just showing what one might do quickly.
"""
import pandas 
from pathlib import Path
import argparse
import json
from datetime import datetime
import typing as T
import matplotlib.pyplot as plt
import numpy as np
import math

def load_data(file: Path) -> T.Dict[str, pandas.DataFrame]:

    temperature = {}
    occupancy = {}
    co2 = {}

    """with open('file', "r") as f:"""
    with open('log.txt', "r") as f:
        for line in f:
            r = json.loads(line)
            room = list(r.keys())[0]
            time = datetime.fromisoformat(r[room]["time"])
            #print(room)
            #print(time)

            temperature[time] = {room: r[room]["temperature"][0]}
            occupancy[time] = {room: r[room]["occupancy"][0]}
            co2[time] = {room: r[room]["co2"][0]}

    data = {
        "temperature": pandas.DataFrame.from_dict(temperature, "index").sort_index(),
        "occupancy": pandas.DataFrame.from_dict(occupancy, "index").sort_index(),
        "co2": pandas.DataFrame.from_dict(co2, "index").sort_index(),
    }

    return data


if __name__ == "__main__":
    p = argparse.ArgumentParser(description="load and analyse IoT JSON data")
    p.add_argument("file", help="path to JSON data file")
    P = p.parse_args()

    """file = Path(P.file).expanduser()"""
    file = "log.txt"

    data = load_data(file)
    #print(data)
    counter = 0
    numer_of_data = len(data['temperature'].office)
    print(numer_of_data)
    for x in range(len(data['temperature'])):
        if(not(math.isnan(data['temperature'].office[x]))):
            #print(data['temperature'].office[x])
            if(abs(data['temperature'].office[x]-data['temperature'].median().office)>= 2 * data['temperature'].std().office):
                counter +=1
    #stats=pandas.DataFrame()
    for k in data:
        #t = data["occupancy"]
        #print(t)
        #data[k].plot()
        if k == 'temperature':
            print('Temperature Median is:')
            print(data[k].median())
            print('Temperature Variance is:')
            print(data[k].var())
            print('Temperature Standard Deviation is:')
            print(data[k].std())
            print('Temperature mean is:')
            print(data[k].mean())
            lower_bound_office = data[k]["office"].mean() - 2 * data[k]["office"].std()
            upper_bound_office = data[k]["office"].mean() + 2 * data[k]["office"].std()
            print("the lower bound in office is : "  , lower_bound_office)
            print("the upper bound in office is : "  , upper_bound_office)
            lower_bound_class = data[k]["class1"].mean() - 2 * data[k]["class1"].std()
            upper_bound_class = data[k]["class1"].mean() + 2 * data[k]["class1"].std()
            print("the lower bound in class1 is : "  , lower_bound_class)
            print("the upper bound in class1 is : "  , upper_bound_class)
            lower_bound_lab = data[k]["lab1"].mean() - 2 * data[k]["lab1"].std()
            upper_bound_lab = data[k]["lab1"].mean() + 2 * data[k]["lab1"].std()
            print("the lower bound in lab1 is : "  , lower_bound_lab)
            print("the upper bound in lab1 is : "  , upper_bound_lab)

            #print(data[k]["office"])
            """  print("here is what : \n")
            print(data[k].std().office)
            print("here is what2 : \n")
            if(not(math.isnan(data[k].office[0]))):
                print(data[k].office[0])
            """

        if k == 'occupancy':
            print('Occupancy Median is:')
            print(data[k].median())
            print('Occupancy Variance is:')
            print(data[k].var())
            print('Occupancy Standard Deviation is:')
            print(data[k].std())
            print('Occupancy mean is:')
            print(data[k].mean())
        """
        time = data[k].index
        data[k].hist()
        plt.figure()
        plt.hist(np.diff(time.values).astype(np.int64) // 1000000000)
        plt.xlabel("Time (seconds)")
        """
        if k == 'temperature':
            data[k].plot.kde()
            plt.title('Temperature probability density function')
        elif k == 'occupancy':
            data[k].plot.kde()
            plt.title('Occupancy probability density function')
        else:
            data[k].plot.kde()
            plt.title('Co2 probability density function')
       # print("here are the time data:")
        #print(data['temperature'].index[1:]) 
        #print("here are the time data   :")
        #print(data['temperature'].index[:-1]) 

    time_diffrence = data['temperature'].index[1:] - data['temperature'].index[:-1]
    #print(time_diffrence)
    time = [t.total_seconds() for t in time_diffrence]
    #print(time)
    time_series = pandas.Series(time)
    #print(time_series)
    time_median = time_series.median()
    time_mean = time_series.mean()
    time_variation = time_series.var()
    time_standard_deviation = time_series.std()
    print("Time mean is : ", time_mean)
    print("Time median is : ", time_median)
    print("Time variation is : ", time_variation)
    print("Time standard deviation is : ", time_standard_deviation)
    plt.figure()
    time_series.plot.kde()
    plt.title("Time interval probability density function")
        
    percentage =  (numer_of_data-counter)/(numer_of_data) * 100  
    print("there are ", 100 -percentage, " % data point in temprature")
    #plt.show()
    