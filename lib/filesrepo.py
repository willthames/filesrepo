from flask import Flask, render_template
import os
import yaml
import downloader

app = Flask(__name__)

REPO_CONFIG = os.path.join(os.path.dirname(__file__), 'repos.yaml')

app.config.from_object('config.Config')
app.config.from_object(__name__)
app.config['HTTP_PROXY'] = app.config.get('HTTP_PROXY',
    os.environ.get('http_proxy', ''))

with file(app.config['REPO_CONFIG']) as f:
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
    downstream = os.path.join(app.config['REPO_DIR'], reponame, filename)
    upstream = repos[reponame]['url'] + filename
    return downloader.get(upstream, downstream, app.config['HTTP_PROXY'])

if __name__ == '__main__':
    app.run()
