#!/usr/bin/env python3
import pandas as pd
import os
import pickle

def retrieve_df():
    cwd = os.getcwd()
    df_name = '/comedian_metrics.pkl'
    file_path = cwd + df_name
    df = pd.read_pickle(file_path)
    return df

def check_word(sub, str_list):
    result = any(sub in mystring for mystring in str_list)
    return result

# takes user-inputted ratings and extracts comedians
def rate_search(df, comics, rate_list):
    total = df.shape[0]
    if rate_list[0] == '1':
        clean = df['rating'] == 1
        df_clean = df[clean]
        df_clean = df_clean.sort_values(by=['edginess'])
        tot_comics = df_clean.shape[0]
        comics = list(df_clean.iloc[0:3,0])
        comics.append(str(tot_comics))
    if rate_list[1] == '1':
        mid = df['rating'] == 2
        df_mid = df[mid]
        df_mid = df_mid.sort_values(by=['edginess'])
        size_of = df_mid.shape[0]
        midpoint = int(size_of/2)
        comics = list(df_mid.iloc[midpoint-1:midpoint+2,0])
        tot_comics = df_mid.shape[0]
        comics.append(str(tot_comics))
    if rate_list[2] == '1':
        dark = df['rating'] == 3
        df_dark = df[dark]
        df_dark = df_dark.sort_values(by=['edginess'], ascending=False)
        comics = list(df_dark.iloc[0:3,0])
        tot_comics = df_dark.shape[0]
        comics.append(str(tot_comics))
    return comics

