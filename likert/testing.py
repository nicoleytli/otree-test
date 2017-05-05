
import csv

headers = ['Symbol','Price','Date','Time','Change','Volume']
rows = [('AA', 39.48, '6/11/2007', '9:36am', -0.18, 181800),
         ('AIG', 71.38, '6/11/2007', '9:36am', -0.15, 195500),
         ('AXP', 62.58, '6/11/2007', '9:36am', -0.46, 935000),
       ]

with open('you.csv', 'a+') as f:
    f_csv = csv.writer(f)
    f_csv.writerow(headers)
    f_csv.writerows(rows)

# reader = csv.reader(open('you.csv'), delimiter=",")
# for symbol in reader:
#     print(symbol)
#
# with open('you.csv') as f:
#     all_objects = list(csv.DictReader(f))
#
# print(all_objects[2]['Symbol'])


