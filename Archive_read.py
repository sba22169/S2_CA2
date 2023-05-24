from dotenv import dotenv_values
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests
import json
import warnings
import gzip
import json
import os


# Function copy to add jsonm search experiment ******************
def extract_json_from_directory(directory, search_word):
    """Function to unzip and extract all json all files in a given directory"""
    extracted_data = []
    for file_name in os.listdir(directory):
        if file_name.endswith('.json.gz'):
            print(f"Extracting file {file_name} ")
            file_path = os.path.join(directory, file_name)
            with gzip.open(file_path, 'r') as file:
                print(f" Unzipped:{file}")

                #for line in file:
                    #line = lineA[1:-1]
                    #print(f"Line is:{line}")
                try:
                    json_data = json.loads(file)
                    for item in json_data:
                        print(f"item is {item}")
                        date = item.get('created_at')
                        text = item.get('text')
                        if any(word in text.lower() for word in search_words):
                            extracted_data.append(date,text)
                                
                            
                            #extracted_data.append(json_data)

                except json.JSONDecodeError as e:
                        print(f"Error parsing JSON line in {file_name}: {e}")
        df = pd.DataFrame(extracted_data)
        #filtered = filter_tweets(df,search_word)
    #ftdf.append(filtered)
        

    
        #for data in extracted_data:
            #json.dump(data, output)
    return df


search_words = ['trans','gay']
directory = "/Users/ambrosedesmond/CCT_Projects/Ambrose_MSC_BD_ADA_CA2/Twitter_Archive_Data/20220901"
cbdf = extract_json_from_directory(directory,search_words)
cbdf.shape
# output_file = "/Users/ambrosedesmond/CCT_Projects/Ambrose_MSC_BD_ADA_CA2/Twitter_Archive_Data"