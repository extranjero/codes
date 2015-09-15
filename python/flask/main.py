from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello world"

#Variable rules
@app.route("/user/<username>")
def show_user(username):
    return 'User %s' % username


@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

#HTTP Methods
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        do_the_login()
    else:
        show_the_login_form()

@app.route('/hello/<name>')
def hello(name=None):
    return render_template('index.html', name=name)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

