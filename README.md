# day57_100
# What I Learned Today

## Using Flask and Jinja2 Templates
Today, I explored how to build a simple blog application using Flask, a lightweight web framework for Python, and Jinja2, a templating engine for Python. Here are some key takeaways:

1. __Flask Basics:__

  - __App Initialization:__ I learned how to initialize a Flask application using Flask(__name__) and set up basic routes using the @app.route decorator.
  - __Running the App:__ I used app.run(debug=True) to run the Flask application in debug mode, which is helpful for development.

2. __Fetching Data:__

  - __Requests Library:__ I used the requests library to fetch blog posts from an external API and parse the JSON response.
  - __Dynamic Routing:__ I set up dynamic routes in Flask to handle different URLs and pass parameters to the routes.

3. __Jinja2 Templating:__

  - __Template Rendering:__ I learned how to use the render_template function to render HTML templates and pass data from my Flask routes to the templates.
  - __For Loops and Conditionals:__ I used Jinja2 templating syntax to loop through the list of blog posts and conditionally render content based on dynamic data.

4. __HTML and CSS Integration:__

  - __Linking Stylesheets:__ I integrated external stylesheets into my HTML templates using the url_for function to generate the correct paths.
  - __Dynamic Content:__ I used Jinja2 to dynamically insert content into the HTML templates, such as blog titles, subtitles, and body text.

Here are some examples of what I implemented:

### Dynamic Link Generation in index.html:
```python
<a href="{{ url_for('get_blog', num=blog_post['id']) }}">{{ blog_post["subtitle"] }}</a>
```

### Conditional Rendering in post.html:
```python
{% for blog_post in posts %}
    {% if blog_post["id"] == num %}
    <div class="content">
        <div class="card">
            <h2>{{ blog_post["title"] }}</h2>
            <p>{{ blog_post["subtitle"] }}</p>
            <p>{{ blog_post["body"] }}</p>
        </div>
    </div>
    {% endif %}
{% endfor %}
```

### Flask Route Example:
```python
@app.route('/blog/<int:num>')
def get_blog(num):
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("post.html", posts=all_posts, num=num)
```
By working on this project, I gained a deeper understanding of how to build dynamic web applications with Flask and Jinja2, as well as how to fetch and render data from external APIs. This knowledge will be valuable for future web development projects.

![](https://github.com/AlvinChin1608/day57_100/blob/main/gif/ScreenRecording2024-07-22at19.08.25-ezgif.com-video-to-gif-converter.gif)
