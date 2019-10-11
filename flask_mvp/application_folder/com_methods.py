#!/usr/bin/env python3
import pandas as pd
import os
import pickle

def retrieve_df():
    cwd = os.getcwd()
    df_name = '/comedians.pkl'
    file_path = cwd + df_name
    df = pd.read_pickle(file_path)
    return df

def check_word(sub, str_list):
    result = any(sub in mystring for mystring in str_list)
    return result

# takes user-inputted rating and joke form and returns list of comedians
def comic_search(df, rating, form):
    comics = df[(df.rating == rating) & (df.form == form)].comedian.tolist()
    return comics

