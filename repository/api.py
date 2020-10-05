import requests

from flask import Flask, request, jsonify

import db

app = Flask(__name__)

GITHUB_API = "https://api.github.com"


@app.route('/')
def hello_world():
    return "Hello World!"


@app.route('/<string:org>')
def get_organization_repos(org):
    r = requests.get(f'{GITHUB_API}/orgs/{org}/repos', headers={
                     'accept': 'application/vnd.github.v3+json'})
    return jsonify(r.json())


@app.route('/<string:org>/<string:repo>/tags')
def get_repo_tags(org, repo):
    r = requests.get(f'{GITHUB_API}/repos/{org}/{repo}/tags', headers={
                     'accept': 'application/vnd.github.v3+json'})
    return jsonify(r.json())


@app.route('/<string:org>/<string:repo>/comment', methods=["POST"])
def comment_on_repo(org, repo):
    comment = request.json['comment']
    db.add_repo_comment(org, repo, comment)
    return ''


@app.route('/<string:org>/<string:repo>/comments')
def get_repo_comments(org, repo):
    comments = db.get_repo_comments(org, repo)
    if comments is None:
        comments = []
    return jsonify(comments)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
