import requests

from flask import Flask, request, jsonify

# CORS is enabled only for easy development
from flask_cors import CORS

import db
import repo

app = Flask(__name__)
CORS(app)

GITHUB_API = "https://api.github.com"


@app.route('/<string:org>')
def get_organization_repos(org):
    r = requests.get(f'{GITHUB_API}/orgs/{org}/repos', headers={
                     'accept': 'application/vnd.github.v3+json'})
    repo_names = repo.extract_repos_from_list(r.json())
    return jsonify(repo_names), r.status_code


@app.route('/<string:org>/<string:repo>/tags')
def get_repo_tags(org, repo):
    r = requests.get(f'{GITHUB_API}/repos/{org}/{repo}/tags', headers={
                     'accept': 'application/vnd.github.v3+json'})
    return jsonify(r.json()), r.status_code


@app.route('/comment/<string:org>/<string:repo>', methods=["POST"])
def comment_on_repo(org, repo):
    comment = request.json['comment']
    # TODO support users
    db.add_repo_comment(org, repo, comment=comment, user='todo_user')
    return jsonify({'repo': f'{org}/{repo}', 'comment': comment})


@app.route('/<string:org>/<string:repo>/comments')
def get_repo_comments(org, repo):
    # TODO support users
    comments = db.get_repo_comments(org, repo, user='todo_user')
    return jsonify(comments)


@app.route('/bookmark/<string:org>/<string:repo>', methods=["POST"])
def bookmark_repo(org, repo):
    # TODO support users
    db.bookmark_repo(org, repo, user='todo_user')
    return jsonify({'success': True})


@app.route('/bookmark/<string:org>/<string:repo>', methods=["DELETE"])
def unbookmark_repo(org, repo):
    # TODO support users
    db.unbookmark_repo(org, repo, user='todo_user')
    return jsonify({'success': True})


@app.route('/bookmarks')
def get_bookmarked_repos():
    # TODO support users
    return jsonify(db.get_bookmarked_repos(user='todo_user'))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
