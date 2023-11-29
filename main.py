from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)

@app.route('/')
def index():
    if 'username' in session:
        return render_template('dashboard.html')
    else:
        return render_template('notloggedin.html')

if __name__ == '__main__':
    app.run()