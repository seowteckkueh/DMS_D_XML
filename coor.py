import csv
import re

def dms2dd(degrees, minutes, seconds, direction):
    dd = float(degrees) + float(minutes)/60 + float(seconds)/(60*60);
    if direction == 'S' or direction == 'W':
        dd *= -1
    return dd;


def parse_dms(dms):
    parts = re.split('[^\d+\.\d\w]+', dms)
    lat = dms2dd(parts[0], parts[1], parts[2], parts[3])
    lng = dms2dd(parts[4], parts[5], parts[6], parts[7])
    witsml="""    
    <wellLocation uid="offset">
      <latitude uom="dega">{lat}</latitude>
      <longitude uom="dega">{lng}</longitude>
    </wellLocation>
    """.format(lat=lat,lng=lng)
    return witsml

#result = parse_dms("36°57'9\" N 110°4'21\" W")

#print(result)

with open('coordinate.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        #print(row['Well'])
        #print(parse_dms((str(row['Latitude'])+" " +str(row['Longitude']))))
        #print(re.split('[^\d+\.\d\w]+', str(row['Latitude'])))
        row['XML']=parse_dms((row['Latitude']+" " +row['Longitude']))
        print(row['XML'])
        with open('results.csv','a+') as result:
            thewriter=csv.writer(result)
            thewriter.writerow([row['Well']])
            thewriter.writerow([row['XML']])
            #thewriter.writerow([str(row['Well']),str(row['Latitude']),str(row['Longitude']),str(row['XML'])])
