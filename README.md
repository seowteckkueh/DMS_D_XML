# DMS_D_XML

Problem statement
---
I have to import well location to my servers in WITSML format.
The well location are provided by well planner in degree,minute and second format, 
however in WITSML format, the location have be in decimal.

Solution
---
I writen a python code to convert the latitude and longitude value in degree, minute
and second format to decimal. And after that insert these latitude and logitude value in
WITSML format with 'welllocation' tag so I can paste it into my query software so I can add
these values to our servers.

Input and output
---
Input file will be a csv file named coordinate.csv
Three columns must be included in the csv file which are 'Well', 'Latitude' and 'Longitude'
Output will be well name followed by its corresponding well location in WITSML format.
