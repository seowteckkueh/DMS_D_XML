#--Import all the modules--
import tkinter as tk
from tkinter import filedialog as fd
import csv
import re
import shutil
import os


#--- Function Part 1: the conversion---
#converts the degree minutes, seconds to degree
def dms2dd(degrees, minutes, seconds, direction):
    dd = float(degrees) + float(minutes)/60 + float(seconds)/(60*60);
    if direction == 'S' or direction == 'W':
        dd *= -1
    return dd;

#parse the latitude and logitude values split it and convert them to degree using the function dms2dd
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

#read the template file line by line and parse it using function parse_dms
def process():
    with open(path, newline='') as csvfile: 
        reader = csv.DictReader(csvfile)
        xml=""
        for row in reader:
            row['XML']=parse_dms((row['Latitude']+" " +row['Longitude']))
            xml=xml+(row["Well"]+row['XML']+"\n")
        return xml
        

#---Function Part 2: the GUI           
# Opens up the directory browser
def open_file():
    global path
    global show_path
    path=fd.askopenfilename()
    show_path=tk.Label(text=path ,fg='green')
    show_path.grid(column=1, row=2)
    return path

# display the end result in a text field
def display():
    results=process()
    display_result=tk.Text(master=root, height=30, width=70)
    display_result.grid(column=1,row=4)
    display_result.insert(tk.END, results)
    show_path.destroy()

# creates a csv template file and open it with excel
def open_template():
    master_template='master_template.csv'
    template='template.csv'
    shutil.copy(master_template,template)
    os.system("start EXCEL.EXE template.csv")    
    
#---App---
    
root=tk.Tk()
root.title("Degree Minute Second to Decimal Degree Converter")
root.geometry("800x800")
root.iconbitmap("icon.ico")

label=tk.Label(text="This app converts dms to d")
label.grid(column=0,row=0)

label2=tk.Label(text="Results")
label2.grid(column=0, row=4)

button1=tk.Button(text="Browse file..." ,command=open_file)
button1.grid(column=0, row=2)

button2=tk.Button(text="Convert...",command=display)
button2.grid(column=0, row=3)

empty_text_field=tk.Text(master=root, height=30, width=70)
empty_text_field.grid(column=1,row=4)

button3=tk.Button(text='Download template...', command=open_template)
button3.grid(column=0,row=1)

root.mainloop()

