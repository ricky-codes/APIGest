from string import ascii_uppercase
from typing import List
import pandas as pd

from collections import defaultdict

pd.set_option('display.max_rows',500)
#pd.set_option('display.max_columns', 500)

workbook = pd.read_excel('apigest_product_dump.xlsx')
dataframe = pd.DataFrame(workbook, columns= ['CATEGORIES'])
dataframe = dataframe["CATEGORIES"].str.upper()
dataframe = dataframe.drop_duplicates()
dataframe = dataframe.sort_values()
dataframe = dataframe.str.split(" ", n=6, expand=True)
dataframe = dataframe.reset_index(drop=True)

for index, row in dataframe.iterrows():
    for j in range(1, len(row)):
        if row[j] != None:
            if (row[j] == "E" or row[j] == "DE" or row[j] == "A" or row[j] == "EM" or str(row[j])[-1:] == ","):
                category_list = []
                for i in range(1, len(row)):
                    if row[i] != None:
                        category_list.append(row[i])
                        row[i] = None
                row[0] = row[0] + " " + ' '.join(category_list)

#dataframe = dataframe.rename(columns={0:'Category', 1: 'Subcategory', 2: '1', 3: '2', 4: '3', 5: '4'})
#dataframe = dataframe.set_index(['Category', 'Subcategory'])




print(dataframe)

#print(dataframe)


#indexes = pd.MultiIndex.from_frame(dataframe, names=("0", "1", "2", "3", "4", "5"))

#indexed_dataframe = pd.DataFrame(dataframe, index=indexes)

#print(indexed_dataframe)

#grouped_dataframe = dataframe.groupby(by=["Category"])

#second_grouped_dataframe = pd.DataFrame(grouped_dataframe.groupby(by=["Subcategory"]))


#print(grouped_dataframe.head(200))


#dataframe.to_excel(r'dataframe.xlsx')
#print(dataframe.to_json(orient="index"))
#for name, group in second_grouped_dataframe:
#    print(group)

#print(grouped_dataframe.head(200))

#print(grouped_dataframe)

#print(grouped_dataframe.get_group(("VINHO")))