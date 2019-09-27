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
        comics = []
        rate_clean = request.form.get('rate_1')
        rate_mid = request.form.get('rate_2')
        rate_dark = request.form.get('rate_3')

        # put in try/exceptions to curb user errors later!
        rate_list = [rate_clean, rate_mid, rate_dark]
        comics = com_methods.rate_search(df, comics, rate_list)

        if rate_clean:
            rating = 'PG'
        if rate_mid:
            rating = 'PG-13'
        if rate_dark:
            rating = 'R'
        
        template_dict = {
            'rating_key' : rating,
            'comic1': comics[0],
            'comic2': comics[1],
            'comic3': comics[2],
            'comic_total': comics[3]
            }
        return render_template('test_results.html', **template_dict)
    
        # return '''<h1>The language value is: {}</h1>
        #           <h1>The framework value is: {}</h1>
        # <h1>Color selected: {} </h1>'''.format(language, framework, color)
   
    
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
