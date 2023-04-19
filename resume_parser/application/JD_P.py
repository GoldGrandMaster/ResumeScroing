
# import pandas as pd
# df = pd.read_csv('borneo-JD.txt', delimiter = "\t")
# df = df.reset_index().T.reset_index().T
# print(df[0])
re = ""
with open('borneo-JD.txt', 'r') as f:
    for line in f.readlines():
        re = re + line
# f = open('borneo-JD.txt', 'r')

print(len(re))