#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 13:08:37 2020

@author: ahmed-adel
"""

import csv
import json


# occupation  skils Skills Description tasks related occuption code Industries    
header=["Occupation",'Code','Industries','Skills','Skills Description','Tasks']   
with open("jobs.csv", "w+") as file:    
       file2=csv.writer(file, delimiter=',') 
       file2.writerow(header)
index=0
for line in open('json.json','r'):
    row=[]
    skill=''
    task=''
    skill_description=''
    #related_occuption=''
    dic=json.loads(line)
    Occupation=dic['Occupation']
    row.append(Occupation)
    Code=dic['Code']
    row.append(Code)
    Code=Code.replace(".", "-")
    Industries=dic['Industries']
    row.append(Industries)
    skills=dic[str(index)]['skills_'+Code+'.csv']["Skill"]
    skills_Description=dic[str(index)]['skills_'+Code+'.csv']['Skill Description']
    tasks=dic[str(index)]['tasks_'+Code+'.csv']['Task']
    #related_occuptions=dic[str(index)]['related_occupations_'+Code+'.csv']['O*NET-SOC Title']
    index +=1
    
    for x in skills:
        skill=skill+x+' '
    row.append(skill)
    
    for x in tasks:
        task=task+x+' '
    row.append(task)
    
    for x in skills_Description:
        skill_description=skill_description+x+' '
    row.append(skill_description)
    
#    for x in related_occuptions:
#        related_occuption=related_occuption+x+' '
#    row.append(related_occuption)
    
    with open("jobs.csv", "a+") as file:    
        file2=csv.writer(file, delimiter=',')
        file2.writerow(row)
    



