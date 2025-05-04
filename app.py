from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/')
def ome():
    return render_template('base.html')

@app.route('/foods')
def foods():
    with open('food_data.json') as f:
        food_items = json.load(f)
    return render_template('foods.html', foods=food_items)

@app.route('/my-list')
def my_list():
    return "<h2> This will show the users selected food list.</h2>"

if __name__ == '__main__':
    app.run(debug=True)