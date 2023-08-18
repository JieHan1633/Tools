from pysolar.solar import *
import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data1 = pd.read_csv("HECOData_Clean_2017.csv")
data2 = pd.read_csv("HECOData_Clean_2018.csv")

dt1 = pd.to_datetime(data1['TimeStamp'], format = '%m/%d/%Y %H:%M',utc=True)
dt2 = pd.to_datetime(data2['TimeStamp'], format = '%m/%d/%Y %H:%M',utc=True)

station = {'Waianae':[21.446911,-158.188736]}
latitude = station['Waianae'][0]
longtitude = station['Waianae'][1]

# date = datetime.datetime(2017, 2, 18, 15, 0, tzinfo=datetime.timezone.utc)
zenith1 = []
zenith2 = []
for i in range(len(dt1)):
    idt = dt1[i].to_pydatetime() 
    al = get_altitude(latitude, longtitude, idt)
    zenith1.append(90-al) 
        
for i in range(len(dt2)):
    idt = dt2[i].to_pydatetime() 
    al = get_altitude(latitude, longtitude, idt)
    zenith2.append(90-al)

data1['Zenith'] = zenith1
data2['Zenith'] = zenith2

# with pd.ExcelWriter('HECOData_Clean_2017_with_zenith.xlsx') as ew:
#     data1.to_excel(ew)
# with pd.ExcelWriter('HECOData_Clean_2018_with_zenith.xlsx') as ew:
#     data2.to_excel(ew)
    
# zenith1 = np.reshape(np.array(zenith1),(-1,24))
# zenith2 = np.reshape(np.array(zenith2),(-1,24))

# z = np.concatenate((zenith1,zenith2),axis=0)
# dayTime = np.where(z<87,1,0)
# daytime_duration = np.sum(dayTime, axis=1)
# daytime_hours = np.transpose((z<87).nonzero())

# fig, ax = plt.subplots(figsize =(10, 7))
# labels, counts = np.unique(daytime_hours[:,1]+1, return_counts=True) 
# labels = labels+1
# plt.bar(labels, counts, align='center',edgecolor='black', linewidth=1.2)
# plt.gca().set_xticks(labels)
# plt.xlabel('Hours in a day')
# plt.ylabel('Counts')
# plt.show()

# fig, ax = plt.subplots(figsize =(10, 7))
# labels, counts = np.unique(daytime_duration, return_counts=True) 
# plt.bar(labels, counts, align='center',edgecolor='black', linewidth=1.2)
# plt.gca().set_xticks(labels)
# plt.xlabel('Durations')
# plt.ylabel('Counts')
# plt.show()
