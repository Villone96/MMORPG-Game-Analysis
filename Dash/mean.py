import pandas as pd
import csv
df = pd.read_csv('AllianceGraph/outdegreeDistribution.csv')

with open('AllianceGraph/OutDegreeMean.csv', 'w', newline='') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    filewriter.writerow(['type','range', 'value'])
    
  



    ranges = df['range'].unique().tolist()
    types = df['type'].unique().tolist()
    s=0
    print(types)
    for r in ranges:
        for t in types:
            dff = df[df['range'] == r]
            dfff =  dff[dff['type'] == t]
            s = (dfff['value'].sum())/30
            filewriter.writerow([t, r, str(s)])
            print('Type: ' + t)
            print('Range: ' + r)
            print('mean: ' + str(s))