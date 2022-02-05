import csv

states = {
            'AK': 'Alaska',
            'AL': 'Alabama',
            'AR': 'Arkansas',
            'AS': 'American Samoa',
            'AZ': 'Arizona',
            'CA': 'California',
            'CO': 'Colorado',
            'CT': 'Connecticut',
            'DC': 'District of Columbia',
            'DE': 'Delaware',
            'FL': 'Florida',
            'GA': 'Georgia',
            'GU': 'Guam',
            'HI': 'Hawaii',
            'IA': 'Iowa',
            'ID': 'Idaho',
            'IL': 'Illinois',
            'IN': 'Indiana',
            'KS': 'Kansas',
            'KY': 'Kentucky',
            'LA': 'Louisiana',
            'MA': 'Massachusetts',
            'MD': 'Maryland',
            'ME': 'Maine',
            'MI': 'Michigan',
            'MN': 'Minnesota',
            'MO': 'Missouri',
            'MP': 'Commonwealth of the Northern Mariana Islands',
            'MS': 'Mississippi',
            'MT': 'Montana',
            'NA': 'National',
            'NC': 'North Carolina',
            'ND': 'North Dakota',
            'NE': 'Nebraska',
            'NH': 'New Hampshire',
            'NJ': 'New Jersey',
            'NM': 'New Mexico',
            'NV': 'Nevada',
            'NY': 'New York',
            'OH': 'Ohio',
            'OK': 'Oklahoma',
            'OR': 'Oregon',
            'PA': 'Pennsylvania',
            'PR': 'Puerto Rico',
            'RI': 'Rhode Island',
            'SC': 'South Carolina',
            'SD': 'South Dakota',
            'TN': 'Tennessee',
            'TX': 'Texas',
            'UT': 'Utah',
            'VA': 'Virginia',
            'VI': 'United States Virgin Islands',
            'VT': 'Vermont',
            'WA': 'Washington',
            'WI': 'Wisconsin',
            'WV': 'West Virginia',
            'WY': 'Wyoming'
    }

states_dict = {}

with open("User_Analysis/VADER_Sentiment.csv", "r", newline='') as fp:
    reader = csv.reader(fp)
    VADER_values = list(reader)

with open("User_Analysis/User_States.csv", "r", newline='') as fp:
    reader = csv.reader(fp)
    states_list = list(reader)

for state, senti in zip(states_list, VADER_values):
    if state[0] in states_dict:
        val = states_dict[state[0]]
        states_dict[state[0]] = [val[0]+float(senti[0]), val[1]+1]
    else:
        states_dict[state[0]] = [float(senti[0]), 1]

states_VADER = [['Shape Name', 'Sentiment']]

for key, value in states_dict.items():
    states_VADER.append([states[key], (value[0]/value[1])*100])   # Taking average of sentiment (for each state)

with open("User_Analysis/User_State_Sentiments.csv", "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerows(states_VADER)

print("File successfully saved. . .")
