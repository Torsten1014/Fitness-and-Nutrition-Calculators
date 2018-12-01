#!/usr/bin/env python
# coding: utf-8

# In[64]:


def centimeters(m):
    cm = (m * 100)
    return cm 
bold = "\033[1m"
reset = "\033[0;0m"

print(bold + "Meters to Centimeters Calculator" + reset)

m = 1.78

print(centimeters(m))
    


# In[174]:


def pounds(kg):
    lb = (kg * 2.205)
    return lb
bold = "\033[1m"
reset = "\033[0;0m"

print(bold + "Kilograms to Pounds Calculator" + reset)

name = "Roong"
kg = 58.8

print(str(name) + " is " + str(pounds(kg)) + " pounds.")


# In[1]:


def kilos(lb):
    kg = (lb / 2.205)
    return kg
bold = "\033[1m"
reset = "\033[0;0m"

print(bold + "Pounds to Kilograms Calculator" + reset)

name = "Torsten"
lb = 163

print(str(name) + " is " + str(kilos(lb)) + " kilos.")


# In[7]:


name = "BRIAN" 
height_m = 1.62
weight_kg = 81.7

bold = "\033[1m"
reset = "\033[0;0m"
print(bold + "BMI Calculator" + reset)
bmi = weight_kg / (height_m ** 2)
print("bmi: " + str(bmi))
if bmi < 25:
    print(name + " is not overweight")
else:
    print(name + " is overweight.")


# 

# In[6]:


gender = "male"
age = 27
activity_level = 1.55
weight = 81.7
height = 162

female = "female"
male = "male"

bold = "\033[1m"
reset = "\033[0;0m"



activity_level_title = "Activity Level"
activity_level_list = '''
Sedentary = 1.2
Lightly Active = 1.375
Moderately Active = 1.55
Very Active = 1.725
Extremely Active = 1.9
'''
print(bold + activity_level_title + reset + activity_level_list)
print(bold + "TDEE Calculator" + reset)

if gender is "female":
    def w_bmr(weight, height, age, activity_level):
        total_bmr_w = (655 + (9.6 * weight) + (1.8 * height) - (4.7 * age)) * activity_level
        return total_bmr_w
    TDEE = w_bmr(weight, height, age, activity_level)
    print("TDEE = " + str(TDEE) + " calories.")
else:
    def m_bmr(weight, height, age, activity_level):
        total_bmr_m = (66 + (13.7 * weight) + (5 * height) - (6.8 * age)) * activity_level
        return total_bmr_m
    TDEE = m_bmr(weight, height, age, activity_level)
    print("TDEE = " + str(TDEE) + " calories.")


# In[ ]:




