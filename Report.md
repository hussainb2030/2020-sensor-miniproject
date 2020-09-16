                                                              Senior Design REPORT
   
   Task0: 
   IoT server starting:  localhost port 8765
   ECE Senior Capstone IoT simulator
   
   Task1:
   The file that we stored our data is data2.txt
   
   Task2:
   a)
   Temperature Median is:
class1    26.992625
lab1      20.994436
office    22.998259
Temperature Variance is:
class1    116.107775
lab1        8.768652
office      8.701145
Temperature Standard Deviation is:
class1    10.775332
lab1       2.961191
office     2.949770
Temperature mean is:
class1    27.816794
lab1      21.001556
office    22.994437

b)
Occupancy Median is:
class1    19.0
lab1       5.0
office     2.0
Occupancy Variance is:
class1    18.473663
lab1       5.449712
office     1.868605
Occupancy Standard Deviation is:
class1    4.298100
lab1      2.334462
office    1.366969
Occupancy mean is:
class1    18.877019
lab1       4.803140
office     1.969925

c)
The plots are going to be generated when you run the code "analyze.py"

d)
i: 
Time mean is :  1.1018134946502058
Time median is :  0.714519
Time variation is :  19.935841859922757
Time standard deviation is :  4.4649570949699795
ii)
The plots are going to be generated when you run the code "analyze.py"
iii)
yes, it mimics a well-known distribution which is Erlang distrubtion which can be used in developing a way to predict the waiting times


Task3:

a)
there are  1.242236024844729  % bad data in class1
there are  0.7246376811594217  % bad data in lab1
there are  2.3809523809523796  % bad data in office

emperature Median after deleting the bad data in lab1 is:
20.994435558276656
Temperature Variance after deleting the bad data in lab1 is::
0.32824379224355804
Temperature Standard Deviation after deleting the bad data in lab1 is:
0.5729256428573939
Temperature mean after deleting the bad data in lab1 is:
21.009820902956854
Temperature Median after deleting the bad data in the office is:
22.998572586275085
Temperature Variance after deleting the bad data in the office is::
0.734443061630806
Temperature Standard Deviation after deleting the bad data in the office is:
0.8569965353668625
Temperature mean after deleting the bad data in the office is:
22.969585122294244
Temperature Median after deleting the bad data in the class1 is:
26.9900509692592
Temperature Variance after deleting the bad data in the class1 is::
5.420973367786927
Temperature Standard Deviation after deleting the bad data in the class1 is:
2.3282983846120167
Temperature mean after deleting the bad data in the class1 is:
27.043830418866467

2) 
  A persistent change in temperature in that are within the the lower and upper bounds may not indicate a failure in the sensor. If there were changes in temperature that included values outside of the upper and lower bounds, then it could indicate a failure in the sensor. This is because the values would have to much variation to determine a median, average, and variance. 



3)
the lower bound in office is :  17.09489585954723
the upper bound in office is :  28.89397746155663
the lower bound in class1 is :  6.266130092207092
the upper bound in class1 is :  49.36745722672513
the lower bound in lab1 is :  15.079174006757256
the upper bound in lab1 is :  26.92393761260452


Task 4:
1)how is this simulation reflective of the real world?

  This situation is reflective of the real world with how creating a sensor involves working values such as temperature, occupancy, and CO2 for a room are generated through methods like sensing, measurement, or detection and how data elements like median, mean, and variance are used for determining accuracy. It is also reflective with how it is tested and works with datasets for three different rooms(office, lab, and class) and there are different values for data elements with those as well. The situation is mostly reflective of how the data is handled for devices like sensors. It reflects how data is stored and saved to be analyzed in task 1. Tasks 2 and 3 reflect conductions of analysis of data and organization(detecting and removing bad data) of it.
  
2)how is this simulation deficient? What factors does it fail to account for?
  
  The simulation involves the upper and lower bounds and observes data without bad numbers/elements for temperature. It doens't do the same for the occupancy and the co2. It may be possible that there could be anomalies in occupancy and co2. If there are, then there are good and bad values for temperature mixed with good and bad values for the occupancy and co2. 
  
3)how is the difficulty of initially using this Python websockets library as compared to a compiled language e.g. C++ websockets
  
  The difficulty in learning and using the attributes in the library is close to the same of learning compiled language. The difficulty in working with the websockets was figuring out how to use the pandas dataframe.
  
4) would it be better to have the server poll the sensors, or the sensors reach out to the server when they have data?
  
  If the sensors reach out to the server when they have the data, then there would have been more values for the dataset. This could lead to more bad data values being taken out or eliminated from the data and more good data points to be evaluated. 
