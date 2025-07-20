from flask import Flask, render_template, json, request
import csv
import sqlite3

app = Flask(__name__)

def item_data():
    with open("items.json") as items:
        data = json.load(items)
    return data


def read_json():
    with open('products.json') as file:
        return json.load(file)


def read_csv():
    products = []
    with open('products.csv', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            products.append({
                'id': int(row['id']),
                'name': row['name'],
                'category': row['category'],
                'price': float(row['price'])
            })
    return products


def read_sql():
    products = []
    try:
        with sqlite3.connect('products.db') as conn:
            cur = conn.cursor()
            cur.execute("SELECT id, name, category, price FROM Products")
            rows = cur.fetchall()
            for row in rows:
                products.append({
                    'id': row[0],
                    'name': row[1],
                    'category': row[2],
                    'price': row[3]
                })
    except sqlite3.Error as e:
        print(f"Dtabase error: {e}")
    return products


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


@app.route('/products', methods=['GET'])
def products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)

    if source not in ['json', 'csv', 'sql']:
        return render_template('product_display.html', error='Wrong source')
    if source == 'json':
        products = read_json()
    elif source == 'csv':
        products = read_csv()
    elif source == 'sql':
        products = read_sql()
    
    if product_id:
        products = [product for product in products if product['id'] == product_id]
    if product_id and not products:
        return render_template('product_display.html', error='Product not found')

    return render_template('product_display.html', products=products)


if __name__ == '__main__':
    app.run(debug=True, port=5000)