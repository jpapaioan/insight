from flask import render_template, request, redirect
from application_folder import flask_instance
import os
import pickle
import pandas as pd

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

@flask_instance.route('/', methods=['POST', 'GET'])
@flask_instance.route('/index', methods=['POST', 'GET'])
def form_example():
    if request.method == 'POST':  #this block is only entered when the form is submitted
        
        foo = request.form.get('edge_1')
        foo2 = request.form.get('edge_2')
        foo3 = request.form.get('edge_3')
        if foo:
            print(foo)
        
        keyword = ''
        comics = com_search(keyword)
        
        template_dict = {
            'key' : keyword,
            'comedians': comics, 
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
