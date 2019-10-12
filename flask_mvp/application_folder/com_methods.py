#!/usr/bin/env python3
import pandas as pd
import os
import pickle

def retrieve_df():
    cwd = os.getcwd()
    df_name = '/comedians.pkl'
    file_path = cwd + df_name
    print('file_path: ', file_path)
    df = pd.read_pickle(file_path)
    return df

# takes user-inputted rating and joke form and returns list of comedians
def comic_search(df, rating, form):
    print('inside comic search \n')
    print('rating: ', rating)
    print('rating type: ', type(rating))
    print('form: ', form)
    
    # pandas is having trouble with the int comparisons when they're variables...?
    comics = df[(df.rating == rating) & (df.form == form)].comedian.tolist()
    print('inside comic search, comics: ', comics)
    return comics

# takes list of comics and returns formatted youtube links for hyperlinking
def comic_url(comics):
    base_url = 'https://www.youtube.com/results?search_query='
    filter_tag = '&sp=EgIYAQ%253D%253D'
    comics_url = [base_url + comic.replace(" ", '+') + '+stand' + '+up' + filter_tag for comic in comics]
    return comics_url
