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
    # Read the data from the file
    with open(file, "r") as f:
    #with open('log.txt', "r") as f:
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

    file = Path(P.file).expanduser()
    #print(file)
    #file = "log.txt"

    data = load_data(file)
    #print(data)
    #store the data in teh file on the variable data
    #create some variables 
    counter_office = 0
    counter_class = 0
    counter_lab = 0
    #clean the data from NaN values
    number_of_data_office = len(data['temperature'].office.dropna())
    number_of_data_class = len(data['temperature'].class1.dropna())
    number_of_data_lab = len(data['temperature'].lab1.dropna())
    data_office = data['temperature'].office
    #print(data_office)
    data_class = data['temperature'].class1.dropna()
    data_lab = data['temperature'].lab1.dropna()
    #print(number_of_data_lab)
    #print(number_of_data_class)
    #print(number_of_data_office)
    numer_of_data = len(data['temperature'])
    #print(numer_of_data)
    indices_office = []
    indices_class = []
    indices_lab = []

    #stats=pandas.DataFrame()
    #calculate the statistic of the data
    for k in data:
        #t = data["occupancy"]
        #print(t)
        #data[k].plot()
        #for the temprature
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
        #for the occupancy
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
        #plot hte probability density
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

    #statistic for the time difference
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
    #the algorithm part
    for x in range(len(data['temperature'])):
        index = x
        if(not(math.isnan(data['temperature'].office[x]))):
            
            #print(data['temperature'].office[x])
            #if(abs(data['temperature'].office[x]-data['temperature'].median().office)>= 2 * data['temperature'].std().office):
            if(data['temperature'].office[x] <= lower_bound_office or data['temperature'].office[x] >= upper_bound_office ):

                counter_office += 1
                #index = data['temperature'].office[x]
                #print(data['temperature'].office[x])
                data['temperature'].office[x] = float("NaN")
                #print(data['temperature'].office[x])
                indices_office.append(index)
                #numer_of_data = len(data['temperature'])
                #print(numer_of_data)
    for x in range(len(data['temperature'])):
        index = x
        if(not(math.isnan(data['temperature'].lab1[x]))):
            #print(data['temperature'].office[x])
            #if(abs(data['temperature'].lab1[x]-data['temperature'].median().lab1)>= 2 * data['temperature'].std().lab1):
            if(data['temperature'].lab1[x] <= lower_bound_lab or data['temperature'].lab1[x] >= upper_bound_lab ):

                counter_lab +=1
                data['temperature'].lab1[x] = float("NaN")
                indices_lab.append(index)
    for x in range(len(data['temperature'])):
        index = x
        if(not(math.isnan(data['temperature'].class1[x]))):
            #print(data['temperature'].office[x])
            #if(abs(data['temperature'].class1[x]-data['temperature'].median().class1)>= 2 * data['temperature'].std().class1):
            if(data['temperature'].class1[x] <= lower_bound_class or data['temperature'].class1[x] >= upper_bound_class ):

                counter_class +=1
                indices_class.append(index)
                data['temperature'].class1[x] = float("NaN")
    new_data_office = data['temperature'].office.dropna()
    new_data_class = data['temperature'].class1.dropna()
    new_data_lab = data['temperature'].lab1.dropna()
    #print(counter_class)
    #print(counter_lab)
    #print(counter_office)
    #print(indices_office)
    
    #new_data_office = data['temperature'].office.drop(index=indices_office)
    #for x in range(len(indices_office)):

    #print(data['temperature'].office.drop())
    #print(data['temperature'].office[712])
    #new_data_class = data_class.drop(index = indices_class)
    #new_data_lab = data_lab.drop(index = indices_lab)
    percentage_class =  (number_of_data_class-counter_class)/(number_of_data_class) * 100  
    percentage_lab =  (number_of_data_lab-counter_lab)/(number_of_data_lab) * 100  
    percentage_office =  (number_of_data_office-counter_office)/(number_of_data_office) * 100  
    print("there are ", 100 - percentage_class, " % bad data in class1")
    print("there are ", 100 - percentage_lab, " % bad data in lab1")
    print("there are ", 100 - percentage_office, " % bad data in office")
    #print if statemnets
    print('Temperature Median after deleting the bad data in lab1 is:')
    print(new_data_lab.median())
    print('Temperature Variance after deleting the bad data in lab1 is::')
    print(new_data_lab.var())
    print('Temperature Standard Deviation after deleting the bad data in lab1 is:')
    print(new_data_lab.std())
    print('Temperature mean after deleting the bad data in lab1 is:')
    print(new_data_lab.mean())

    print('Temperature Median after deleting the bad data in the office is:')
    print(new_data_office.median())
    print('Temperature Variance after deleting the bad data in the office is::')
    print(new_data_office.var())
    print('Temperature Standard Deviation after deleting the bad data in the office is:')
    print(new_data_office.std())
    print('Temperature mean after deleting the bad data in the office is:')
    print(new_data_office.mean())
    
    print('Temperature Median after deleting the bad data in the class1 is:')
    print(new_data_class.median())
    print('Temperature Variance after deleting the bad data in the class1 is::')
    print(new_data_class.var())
    print('Temperature Standard Deviation after deleting the bad data in the class1 is:')
    print(new_data_class.std())
    print('Temperature mean after deleting the bad data in the class1 is:')
    print(new_data_class.mean())
    


    plt.show()
    