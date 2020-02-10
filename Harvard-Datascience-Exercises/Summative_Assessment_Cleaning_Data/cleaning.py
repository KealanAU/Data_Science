import pandas as pd 
import numpy as np

df = pd.read_csv("./harvard-Clean.csv")
#https://courses.edx.org/asset-v1:HarvardX+PH527x+1T2019+type@asset+block@2.4.7_data.csv.
#make the provided data set appropriate for analysis. 



# Fills NA
df = df.fillna(0)

# Updates age of patient with info if there or leaves as none
for index, value in enumerate(df["Age of patient"]):
    try:
        int(value)
    except:
        df.at[index,"Age of patient"] = None

# Updates gender so male is 1 and female is 0
for index, value in enumerate(df["Patient gender"]):
    if str(value).lower()[:1] == "m":
        df.at[index,"Patient gender"] = 1
    elif str(value).lower()[:1] == "f":
        df.at[index,"Patient gender"] = 0
    else:
        df.at[index,"Patient gender"] = None

for index, value in enumerate(df["Complications?"]):
    if str(value).lower()[:1] == "y":
        df.at[index,"Complications?"] = 1
    elif str(value).lower()[:1] == "n":
        df.at[index,"Complications?"] = 0


# Updates height all to be standard in cms
for index, value in enumerate(df["Height"]):
    value = str(value).lower()
    if value[-1:] == '"':
        result = value.find("'")
        if result > 0: 
            out_num = (int(value[:result])* 30.48) + (int(value[result+1:-1]) * 2.54)
            df.at[index,"Height"] = round(out_num)    
        else:
            out_num = int(value[result+1:-1]) * 2.54
            df.at[index,"Height"] = round(out_num)    
    elif value[-1:] == "'":
        out_num = (int(value[:result])* 30.48)
        df.at[index,"Height"] = round(out_num)    
        
    elif value[-2:] == "cm":
        df.at[index,"Height"] = int(value[:-2])
    elif int(value) > 1:
        pass
    else: 
        df.at[index,"Height"] = None


# Update Tumor information to be non romainan numeric
for index, value in enumerate(df["Tumor stage"]):
    try:
        int(value)
    except:
        if value == "I":
           df.at[index,"Tumor stage"] = 1  
        elif value == "II":
           df.at[index,"Tumor stage"] = 2
        elif value == "III":
           df.at[index,"Tumor stage"] = 3
        elif value == "IV":
           df.at[index,"Tumor stage"] = 4

df["Date enrolled"] = pd.to_datetime(df["Date enrolled"], errors= 'coerce')

print(df["Date enrolled"])


df["Treatment"] = df["Treatment A"]


count = 0
# Updates Treatment to be 0 for A and 1 for B
for index, value in enumerate(df["Treatment"]):
    if "treatment" in value.lower():
        count += 1
    df.at[index,"Treatment"] = count

df = df[df["Treatment A"] != "Treatment B" ]

df = df.rename(columns={"Height" : "Height in cm", "Treatment A":"Patient ID"})

# Updates patient ID
for i in df.index:
    df.at[i,"Patient ID"] = i + 1



print(df.head(10))