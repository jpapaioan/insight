from flask import render_template, request, redirect
from application_folder import flask_instance, com_methods
import os
import pandas as pd


def check_word(sub, str_list):
    result = any(sub in mystring for mystring in str_list)
    return result



@flask_instance.route('/', methods=['POST', 'GET'])
@flask_instance.route('/index', methods=['POST', 'GET'])
def form_example():
    if request.method == 'POST':  #this block is only entered when the form is submitted
        df = com_methods.retrieve_df()
        rating = request.form['rating']
        joke_style = request.form['joke_style']
        print('rating: ', rating)
        print('joke_style: ', joke_style)
        # put in try/exceptions to curb user errors later!

        comics = com_methods.comic_search(df,rating, joke_style)
        print('comics: ', comics)
        
        comic_url = 'Anthony+Jeselnik+stand+up'
        filter_url = '&sp=EgIYAQ%253D%253D'
        base_url = 'https://www.youtube.com/results?search_query='
        test_url = base_url+comic_url+filter_url
        template_dict = {
            'rating_key' : rating,
            'comic1': comics[0],
            'comic2': comics[1],
            'comic3': comics[2],
            'comic_total': comics[3],
            'vid_link': test_url
            }
        return render_template('test_results.html', **template_dict)
    
    colors = ['red', 'blue', 'cyan']
    
    return render_template('test.html', colors=colors)



### OLD stuff here, ignore it

@flask_instance.route('/index_old')
def index():
    user = {'username': 'Dan'}
    # render template assumes the file is in "templates/*given_filename.html*
    colors = {'a', 'b', 'c'}
    return render_template('index.html', title='My own title', user=user, colors=colors)

@flask_instance.route('/index_old2', methods=['POST', 'GET'])
def index2():
    # if request.method == 'POST':
    #     user = request.form['nm']
    #     print(user)
    #     return "hey1"
    # else:
    #     return 
    #     user = request.args.get('nm')
    #     return "hey2"
    user = {'username': 'Dan'}
    # render template assumes the file is in "templates/*given_filename.html*
    colors = {'a', 'b', 'c'}
    x=request.args.get('x')
    print(x)
    return render_template('index2.html', title='My own title', user=user, colors=colors)
