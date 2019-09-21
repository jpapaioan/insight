#!/usr/bin/env python3
import pandas as pd
import os
import pickle

def check_word(sub, str_list):
    result = any(sub in mystring for mystring in str_list)
    return result

def com_search(word):
    cwd = os.getcwd()
    file_path = cwd + '/cw.pkl'
    df_cw = pd.read_pickle(file_path)
    com_str = []
    for i in range(len(df_cw.iloc[:,0])):
        if check_word(word, df_cw.iloc[i,1]):
            com_str.append(df_cw.iloc[i,0])
    return com_str
