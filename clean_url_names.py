import pandas as pd
import os
# print(os.getcwd())
df1 = pd.read_excel("data1.xlsx")
# print(df1.head())
add_in = "https://www.parcelmonitor.com"
# with open(file_name, 'r') as infile:
#     for line in infile:
#         line = line.rstrip('\n')
#         columns = line.split(',')
#         # append the url list
#         url_ls.append(columns[0]) #index zero for url title

s1 = df1['Blog URL'] #assign series to column

list_of_urls = []

for url in s1:
    # update the full url into a list
    url =add_in + url
    list_of_urls.append(url)

with open("full_url.csv", 'w') as out_file:
    for url in list_of_urls:
        out_file.write(url + ',\n')

