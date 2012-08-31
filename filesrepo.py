from flask import Flask, render_template
import os

app = Flask(__name__)

app.config.from_object('config.Config')

@app.route('/')
def index(): 
    repos = os.listdir(app.config['REPO_DIR'])
    return render_template('index.html', repos=repos)

if __name__ == '__main__':
    app.run()
