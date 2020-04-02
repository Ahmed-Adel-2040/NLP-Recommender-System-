#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 13:08:37 2020

@author: ahmed-adel
"""

import csv
import json


# occupation  skils Skills Description tasks related occuption code Industries    
header=["Occupation",'Code','Industries','Skills','Skills Description','Tasks','Related Occupations']   
with open("jobs.csv", "w+") as file:    
       file2=csv.writer(file, delimiter=',') 
       file2.writerow(header)

def Concate_List(List):
    word=''
    for x in List:
        word=word+x+' '
    return word

def check_Key(key,Dic={}):
    keys=Dic.keys()
    for key1 in keys:
        if key==key1:
            
            return True
    return False
    



index=0
for line in open('json.json','r'):
    row=[]
    skill=''
    task=''
    skill_description=''
    related_occuption=''
    dic=json.loads(line)
    Occupation=dic['Occupation']
    row.append(Occupation)
    Code=dic['Code']
    row.append(Code)
    Code=Code.replace(".", "-")
    Industries=dic['Industries']
    row.append(Industries)
    if check_Key(str(index)+'skills_'+Code+'.csv',dic):    
        skills=dic[str(index)]['skills_'+Code+'.csv']["Skill"]
        skill=Concate_List(skills)       
    else:
        skill='this is No skills for this job'
    row.append(skill)
    
    if check_Key(str(index)+'skills_'+Code+'.csv',dic):    
        skills_Description=dic[str(index)]['skills_'+Code+'.csv']['Skill Description']
        skill_description=Concate_List(skills_Description)      
    else:
        skill='this is No descriptions for these skills'
    row.append(skill_description)
    
    if check_Key(str(index)+'tasks_'+Code+'.csv',dic):    
        tasks=dic[str(index)]['tasks_'+Code+'.csv']['Task']
        task=Concate_List(tasks)
    else:
        task='oops this we can not find tasks for this job'
    row.append(task)
    
    if check_Key(str(index)+'related_occupations_'+Code+'.csv',dic):     
        related_occuptions=dic[str(index)]['related_occupations_'+Code+'.csv']['O*NET-SOC Title']
        related_occuption=Concate_List(related_occuptions)
    else:
        related_occuption='there is no related jobs for that job'
    row.append(related_occuption)
    index +=1
    
    
    with open("jobs.csv", "a+") as file:    
        file2=csv.writer(file, delimiter=',')
        file2.writerow(row)
    



