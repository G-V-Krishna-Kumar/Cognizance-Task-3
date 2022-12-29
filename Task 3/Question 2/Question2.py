import pandas as p

def read_csv_file(file_name):
    with open(file_name, "r") as read_object:
        reader_object = read_object
        read_object.close()
    return content

df = p.read_csv("Q2-Dataset.csv")
print("Total nan values before: ", df.isnull().sum().sum())

df1 = df.fillna(value = 0)
print("Total nan values now: ", df1.isnull().sum().sum())

