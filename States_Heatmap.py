# import matplotlib.pyplot as plt
# from matplotlib.cm import get_cmap
import json
import csv
'''
x = list(range(1,12))
y = [1]*11
colors = list(range(0,10)) + [398]

# cmap = 'cool', 'jet', 'rainbow'
plt.scatter(x, y, s=200, c=colors, cmap="jet")
cbar = plt.colorbar(orientation="vertical")

plt.show()

cmap = get_cmap('jet')
rgba = cmap(0.5)
print(rgba)
'''
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

with open("User_Analysis/User_States.json", "r") as fp:
    states_dict = json.load(fp)

state_colors = [['Shape Name', 'User Count']]

for key, value in states_dict.items():
    '''
    color = cmap(float(value)/398)
    color = (round(color[0]*255), round(color[1]*255), round(color[2]*255))
    state_colors.append([states[key], '#{:02X}{:02X}{:02X}'.format(*color)])
    '''
    state_colors.append([states[key], value])

with open("User_Analysis/User_State_Distribution.csv", "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerows(state_colors)

print("File successfully saved. . .")
