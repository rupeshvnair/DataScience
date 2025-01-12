import pandas as pd
import os
from concurrent.futures import ThreadPoolExecutor

#Downloading Datasets from kaggle (code is not required once the dataset is downloaded)
# import kagglehub
# path = kagglehub.dataset_download("akashsharma0105/phone-usage-in-india")
# print(f"The path of the downloaded dataset is {path}")

path = '/Users/rupeshviswanadhan/.cache/kagglehub/datasets/akashsharma0105/phone-usage-in-india/versions/1/phone_usage_india.csv'

output_path = '/Users/rupeshviswanadhan/Desktop/all_git/personal/DataScience/Datasets'
def file_splitter(input_file,number_of_splits,output_folder_name):
    with open(input_file,'r') as file:
        lines = file.readlines()
    total_lines = len(lines)
    split_part = total_lines//number_of_splits
    start = 0
    end = 0
    os.makedirs(f"{output_path}/{output_folder_name}",exist_ok=True)
    for i in range(number_of_splits):
        output = f"{output_path}/{output_folder_name}/file_{i}.csv"
        if i == number_of_splits -1:
            end = len(lines)
        else:
            end = start + split_part
        with open(output,'w') as file:
            if start!= 0:
                file.writelines(lines[0:1])
            file.writelines(lines[start:end])
        start = start + split_part

number_of_splits = 4
output_folder_name = 'phone_usage_india'
file_splitter(path,number_of_splits,output_folder_name)

file_name_list = [f"{output_path}/{output_folder_name}/file_{i}.csv" for i in range(number_of_splits)]


def read_csv_file(file_path):
    return pd.read_csv(file_path)


with ThreadPoolExecutor() as executor:
    results = list(executor.map(read_csv_file,file_name_list))

df1,df2,df3,df4 = results
print(df1.head())
print(df2.head())
print(df3.head())
print(df4.head())

