from pymongo import MongoClient

connection = MongoClient('localhost', 27017)
db = connection.repo_explorer


def add_repo_comment(org, repo_name, user, comment):
    repo = db.repository
    full_repo_name = f'{org}/{repo_name}'
    key = {'username': user, 'repo_name': full_repo_name}
    return repo.update_one(key, {
        '$push': {'comments': comment}}, upsert=True)


def get_repo_comments(org, repo_name, user):
    repo = db.repository
    full_repo_name = f'{org}/{repo_name}'
    key = {'username': user, 'repo_name': full_repo_name}
    repo_comments = repo.find_one(key)
    if repo_comments is None:
        return []
    # make ObjectID serializeable
    repo_comments["_id"] = str(repo_comments["_id"])
    return repo_comments


def bookmark_repo(org, repo_name, user):
    return set_bookmark(org, repo_name, user, bookmarked=True)


def unbookmark_repo(org, repo_name, user):
    return set_bookmark(org, repo_name, user, bookmarked=False)


def set_bookmark(org, repo_name, user, bookmarked):
    bookmarks = db.bookmarks
    full_repo_name = f'{org}/{repo_name}'
    key = {'username': user}
    value = {'repos': full_repo_name}
    return bookmarks.update_one(key, {'$push': value}, upsert=True)


def get_bookmarked_repos(user):
    bookmarks = db.bookmarks
    key = {'username': user}
    return bookmarks.find_one(key)['repos']
