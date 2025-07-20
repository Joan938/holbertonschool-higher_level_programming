import json
from flask import Flask, render_template

app = Flask(__name__)

def item_data():
    with open("items.json") as items:
        data = json.load(items)
    return data

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def items():
    data = item_data()
    return render_template('items.html', data=data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)