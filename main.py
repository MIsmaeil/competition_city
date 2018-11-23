# Add python code in this file
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 06:37:40 2018

@author: kanoshy
"""

import csv

citiList=[];
with open('cities.csv','r') as citi_file :
    cities=csv.reader(citi_file)
    for row in cities:
        citiList.append(row)
cities2=citiList[1:]   
#print(cities2)

pointList=[];
with open('points.csv','r') as point_file :
    points=csv.reader(point_file)
    for row in points:
        pointList.append(row)
points2=pointList[1:]   
#print(points2)

result=[]
for tpoint in points2:
    res=["None"]
    xp=int(tpoint[1])
    yp=int(tpoint[2])
    
    for tcity in cities2:
        cityName=tcity[0]
        x1=int(tcity[1])
        y1=int(tcity[2])
        x2=int(tcity[3])
        y2=int(tcity[4])
        if((xp >= x1 and xp<= x2) or (xp <= x1 and xp >= x2)):
            insidex=True
        else:
            insidex=False
        if((yp >= y1 and yp<= y2) or (yp <= y1 and yp >= y2)):
            insidey=True
        else:
            insidey=False   
        
        
        if(insidex and insidey and res !=["None"]):
            res.append(cityName)
        if(insidex and insidey and res ==["None"]):
            res=[cityName]
            
    result.append(tpoint+res)
    

firstRow = pointList[0][:]
firstRow.append('Part of')
#print(firstRow)

result.insert(0,firstRow)
print(result)

with open('output_points.csv','w', newline='') as writeFile :
    writer=csv.writer(writeFile)
    writer.writerows(result)
