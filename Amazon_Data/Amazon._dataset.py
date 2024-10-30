import csv
import numpy as np


with open('C:/Users/5530/OneDrive/Desktop/Data_Analytics/Amazon_DataSet/AWS.csv' ,'r', encoding='utf-8',errors='ignore',newline='') as file_obj:
    file_data = csv.DictReader(file_obj, skipinitialspace=True, delimiter=',')
    my_file = list(file_data)
# print(my_file)

# --------------------------------------------------------------------------------------------------------------------------------

#Task1:- To print the S.no of the title 
# t=[]
# for ele in my_file:
#     t.append(ele['Title'])
# for i,j in enumerate(t[:50],start=40):
#     print(i,j)
# print()

# ------------------------------------------------------------------------------------------------------------------------------------

#Task2:- To get the Title that works as software developers
# count=0 
# for j in t[:31]:  #To prt till 30 S.no
#     if 'Software Development' in j :
#         count+=1
# print(count) #Print the count of 'Software developers'

# ------------------------------------------------------------------------------------------------------------------------------------

#Task3:- To get the location of all India Work stations (Bangalore and KA)
# s=[] 
# for j in my_file:
#     s.append(j['location'])
# k=0
# p=0
# for loc in s:
#     country = [part.strip() for part in loc.split(',')] 
#     # print(country)
#     # for ele in country[1:3]:
#     #     print(ele)
#     if 'Bangalore' in country:
#         k+=1
#     if 'KA' in country:
#         p+=1
# print(k,p)

# --------------------------------------------------------------------------------------------------------------------------------

#Task 4:- No of Jobs in various American City 
# jobs =[]
# citys =[]
# for ele in my_file:
#     jobs.append(ele['location'])
# k={}
# for loc in jobs:
#     jobs_split_form = [part.strip() for part in loc.split(',') ]
#     if 'US'in jobs_split_form:
#         if len(jobs_split_form)>=3:
#             cis=jobs_split_form[2]
#             citys.append(cis)
#             # print(citys)
#             for i in citys:
#                 if i in k:
#                     k[i]+=1
#                 else:
#                     k[i]=1
# # print(k)
# #Way1: Better way(optimized Way to print the key and it value)

# max_values= max(k,key=k.get)
# print(f"City with the highest number of jobs in the city {max_values} with jobs{k[max_values]}")

#Way2: To find it with loop method

# max_count=0
# max_na=''
# for ele in k:
#     if k[ele] > max_count:
#         max_count=k[ele]
#         max_na =ele
# # Print the city and its count
# print(f"City with the highest number of jobs in the city {max_na} with jobs{max_count}")

#----------------------------------------------------------------------------------------------------------------------------------------------------

#Task 5:- Just to split the location acccording to the city,State,Country form the location column (using numpy lib.)
# jobs = []  # List to store job locations
# countries = []  # List to store countries
# states = []  # List to store states
# cities = []  # List to store cities

# # Populate the jobs list from my_file (assumed to be your dataset)
# for ele in my_file:
#     jobs.append(ele['location'])

# # Loop through each job location
# for loc in jobs:
#     # Split the location by commas and strip extra spaces
#     jobs_split_form = [part.strip() for part in loc.split(',')]
#     jobs_split_form = np.array(jobs_split_form)  # Convert to NumPy array
    
#     # Proceed only if there are at least 3 parts (country, state, city)
#     if len(jobs_split_form) >= 3:
#         country = jobs_split_form[0]  # First element is the country
#         state = jobs_split_form[1]    # Second element is the state
#         city = jobs_split_form[2]     # Third element is the city

#         # Append the country, state, and city to their respective lists
#         countries.append(country)
#         states.append(state)
#         cities.append(city)
#     else:
#         # Handle cases with missing parts (optional)
#         print(f"Invalid location format: {jobs_split_form}")

# # Now you have separate lists for countries, states, and cities
# print("Countries:", countries)
# print("States:", states)
# print("Cities:", cities)

#--------------------------------------------------------------------------------------------------------------------------------------

# #Task 6:- No of Bachlor Jobs and Master Job in all the country and which degree job is more in that country
# country = []    # List to store countries
# Basic_eq = []   # List to store basic qualifications

# # Populate country and basic qualifications lists
# for ele in my_file:
#     country.append(ele['location'])  # Country location
#     Basic_eq.append(ele['BASIC QUALIFICATIONS'])  # Job qualifications

# # Create dictionaries to store Bachelor's and Master's job counts per country
# bachelor_count = {}
# master_count = {}

# # Loop through each qualification and count Bachelor's and Master's jobs for each country
# for i in range(len(Basic_eq)):
#     # Clean up country names
#     loc_parts = [part.strip() for part in country[i].split(',')]
    
#     if len(loc_parts) > 0:
#         country_name = loc_parts[0]
#     else:
#         country_name = "Unknown"  # In case of missing country

#     # Check for 'Bachelor' in qualifications
#     if 'Bachelor' in Basic_eq[i]:
#         if country_name in bachelor_count:
#             bachelor_count[country_name] += 1
#         else:
#             bachelor_count[country_name] = 1

#     # Check for 'Master' in qualifications
#     if 'Master' in Basic_eq[i]:
#         if country_name in master_count:
#             master_count[country_name] += 1
#         else:
#             master_count[country_name] = 1

# # Compare Bachelor's and Master's jobs for each country
# for country_name in bachelor_count.keys():
#     bachelor_jobs = bachelor_count.get(country_name, 0)
#     master_jobs = master_count.get(country_name, 0)
    
#     if bachelor_jobs > master_jobs:
#         print(f"{country_name} has more Bachelor's jobs: {bachelor_jobs} vs {master_jobs}")
#     else:
#         print(f"{country_name} has more Master's jobs: {master_jobs} vs {bachelor_jobs}")

#------------------------------------------------------------------------------------------------------------------

