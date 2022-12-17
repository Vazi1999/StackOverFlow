from fetch import *
from flask import Flask , render_template , url_for , request
import os

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('page.html')


@app.route('/search')
def search():
    query = request.args.get("search_query")
    if query == None:
        return render_template('page.html')
    else:
        by_search(query)
    return render_template('page.html')


@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    file.save(os.path.join("E:\VsCode Files\Python\StackOverFlow\Test", file.filename))
    with open(os.path.join("E:\VsCode Files\Python\StackOverFlow\Test", file.filename), 'r') as f:
        data = f.read()
        if by_code(data):
            return render_template('noErrors.html')
    return render_template('page.html')



if __name__ == '__main__':
    app.run(debug=True)





