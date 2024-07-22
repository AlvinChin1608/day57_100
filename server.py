from flask import Flask, render_template
import random
from datetime import datetime
import requests

app = Flask(__name__)

@app.route('/')
def home():
    random_number = random.randint(1, 10)
    current_year = datetime.now().year
    return render_template("index.html", num=random_number, year_num=current_year)

@app.route('/guess/<name>')
def guess(name):
    guess_site = requests.get(f'https://api.agify.io?name={name}')
    guess_data = guess_site.json()
    age = guess_data.get("age")

    gender_site = requests.get(f'https://api.genderize.io?name={name}')
    gender_data = gender_site.json()
    gender = gender_data.get("gender")

    return render_template("guess.html", name=name, guess_age=age, guess_gender=gender)

@app.route('/blog/<num>')
def get_blog(num):
    print(num)
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_post = response.json()
    return render_template("blog.html", posts=all_post)

if __name__ == "__main__":
    app.run(debug=True)
