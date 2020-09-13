from flask import Flask, request, render_template
import pdb
import torch
import sys
import os

#ishita's laptop does not support BERT
isAmbar = False
if os.getcwd() != 'C:\\Users\\sakur\\Desktop\\Hophacks\\website2\\fact-checker':
    isAmbar = True
    sys.path.insert(0, './cis/home/ambar/my_documents/docker-data/com/hophacks20_2')
    from test_search_engine import check_true, sanitizer2

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

# @app.route('/<string:query>')
# def post(query):
#     res = query + " Hello"
#     # pdb.set_trace()
#     return render_template('result.html', result=res)

@app.route('/', methods=['POST'])
def post2():
    text = request.form['query']
    try:
        if isAmbar:
            response = check_true(sanitizer2(text))
        else: response = 1

        response = ['False', 'Unsure', 'True'][response * 2]
    except:
        response = 'Unsure'

    return render_template('results2.html', result=response, question=text)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
