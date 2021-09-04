import requests
import json
import datetime as DT
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
from scipy import stats

#Determining dates of one week ago and yesterday
today = DT.date.today()
week_ago = today - DT.timedelta(days=8)
week_ago = str(week_ago) + "T00:00:00.000"
yesterday = today - DT.timedelta(days=1)
yesterday = str(yesterday) + "T00:00:00.000"


response = requests.get("https://data.cdc.gov/resource/unsk-b7fc.json/?$select=location&date=2021-06-15T00:00:00.000").text
response2 = requests.get("https://data.cdc.gov/resource/unsk-b7fc.json?$select=admin_per_100k, location&$where=date='{}'".format(yesterday)).text
response3 = requests.get("https://data.cdc.gov/resource/9mfq-cb36.json?$select=new_case, state&$where=submission_date>='{}'".format(week_ago)).text
# response4 = requests.get("https://data.cdc.gov/resource/9mfq-cb36.json/?$select=submission_date=2021-06-15T00:00:00.000").text



data = json.loads(response2)
data1 = json.loads(response3)






#List of states graphed
states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", 
        "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
        "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
        "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
        "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

#Population of each state
state_pop = {'CA': 39512223, 'TX': 28995881, "FL": 21477737, "NY": 19453561, "PA": 12801989, "IL": 12671821, "OH": 11689100, "GA": 10617423, "NC": 10488084, "MI": 9986857, "NJ": 8882190, "VA": 8535519, "WA": 7614893, "AZ": 7278717, "MA": 6949503, "TN": 6833174, "IN": 6732219, "MO": 6137428, "MD": 6045680, "WI": 5822434, "CO": 5758736, "MN": 5639632, "SC": 5148714, "AL": 4903185, "LA": 4648794, "KY": 4467673, "OR": 4217737, "OK": 3956971, "CT": 3565287, "UT": 3205958, "IA": 3155070, "NV": 3080156, "AR": 3017825, "MS": 2976149, "KS": 2913314, "NM": 2096829, "NE": 1934408, "ID": 1787065, "WV": 1792147, "HI": 1415872, "NH": 1359711, "ME": 1344212, "MT": 1068778, "RI": 1059361, "DE": 973764, "SD": 884659, "ND": 762062, "AK": 731545, "VT": 623989, "WY": 578759, "DC": 705749}



covid_cases = {}
for entry in data1:
    if entry['state'][:2] in states: 
            covid_cases[entry['state'][:2]] = covid_cases.get(entry['state'][:2], 0) + float(entry['new_case'])

covid_cases_100k = {}
for entry in covid_cases:
    covid_cases_100k[entry] = round((covid_cases[entry] / state_pop[entry]) * 100000, 2)

admin_100k = {}
for entry in data:
    if entry['location'][:2] in states:
        admin_100k[entry['location'][:2]] = admin_100k.get(entry['location'][:2], 0) + float(entry['admin_per_100k'])


xarr = []
for entry in states:
    xarr.append(admin_100k[entry])

yarr = []
for entry in states:
    yarr.append(covid_cases_100k[entry])


x = np.array(xarr)
y = np.array(yarr)



fig, ax = plt.subplots() 


#Remove the lines on the top and right side of the graph
right_side = ax.spines["right"]
top_side = ax.spines["top"]
right_side.set_visible(False)
top_side.set_visible(False)



plt.scatter(x, y, label='Label 1', color='red', s=25, marker="o")


#Plots the x axis, y axis, and title labels
plt.xlabel("Total Vaccine Doses per 100k Population", fontsize="xx-large")
plt.ylabel("Cumulative Covid Cases per 100k Population in Last 7 Days", fontsize="xx-large")
# plt.title("Title", fontsize="xx-large")

for i, txt in enumerate(states):
    ax.annotate(txt, (xarr[i], yarr[i]))

m, b = np.polyfit(x, y, 1)

plt.plot(x, m*x + b)

plt.show()