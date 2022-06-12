#!/usr/bin/env python
# coding: utf-8

# <a href="https://colab.research.google.com/github/shayonid/code-20220612-shayonidutta/blob/main/BMI.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# In[10]:


#import libraries
import json


# In[11]:


#upload your json or txt file
#from google.colab import files
#uploaded = files.upload()


# In[12]:


#Load the JSON object inside the BMI.json/txt file using the json.load() method as list of dicts. Open BMI.json/txt using the with() method
from os import path

file_path = path.relpath("C:/Users/sdutta/AppData/Roaming/Python/Python38/Scripts/VAM/BMI.txt")
with open(file_path) as f:
    data = json.load(f)


# In[13]:
def BMI_add(mass,height):
    BMI = round((mass/(height*height)),2)
    
    if BMI > 40.0:
        return BMI, "Very severly obese","Very high risk"
        
    elif BMI >= 35 and BMI <= 39.9:
        return BMI, "Severly obese","High risk"
        
    elif BMI >= 30 and BMI <= 34.9:
        return BMI, "Moderately obese", "Medium risk" 
       
    elif BMI >= 25 and BMI <= 29.9:
        return BMI, "Overweight", "Enhanced risk" 
        
    elif BMI >= 18.5 and BMI <= 24.9:
        return BMI, "Normal Weight", "Low risk"
             
    else:
        return BMI, "underweight", "Malnutrition risk"
        
   

#Calculate BMI and other 2 categories: BMI_Category and Health_risk and append to the end of each dict in the list
for i in data:
    mass = i['WeightKg']
    height = i['HeightCm']* 0.01
    BMI, BMI_Category, Health_Risk = BMI_add(mass, height) 
    i['BMI']= BMI     
    i['BMI_Category']= BMI_Category
    i['Health_Risk']= Health_Risk
    


# In[14]:


# Count the total number of overweight people
print(sum(1 for d in data if d.get('BMI_Category') == 'Overweight'))


# In[14]:


#Writing JSON to a File with Python
json_string = json.dumps(data)
print(json_string)
with open('json_data.json', 'w') as outfile:
    outfile.write(json_string)

