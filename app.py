from flask import Flask, render_template, request, redirect
from scrapper import scrapSnapdeal

app = Flask(__name__)


@app.route('/')
def index():
  return "Hello WELCOME to Nishit's Price Comparison App"

@app.route('/search')
def search():
  return render_template('search.html')

@app.route('/result', methods = ['POST'])
def result():
  query = request.form.get('query')

  result = scrapSnapdeal(query)
  return render_template('result.html', result = result)

if __name__ == "__main__":
  app.run(port = 8000, debug = False)
