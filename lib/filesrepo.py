from flask import Flask, render_template
import os
import yaml

app = Flask(__name__)

app.config.from_object('config.Config')

with file('repos.yaml') as f:
    repos = yaml.load(f)

@app.route('/')
def index(): 
    return render_template('index.html', repos=repos)

@app.route('/<reponame>/')
def repo(reponame):
    repopath = os.path.join(app.config['REPO_DIR'], reponame)
    if not os.path.exists(repopath):
        return render_template('repo_not_found.html', reponame=reponame), 404
    return render_template('repo.html', reponame=reponame,
        files=os.listdir(repopath))

@app.route('/<reponame>/<filename>')
def file(reponame, filename):
    return os.path.join(app.config['REPO_DIR'], reponame, filename)

if __name__ == '__main__':
    app.run()
