from pymongo import MongoClient

connection = MongoClient('db', 27017)
db = connection.repo_explorer


def add_repo_comment(org, repo_name, comment):
    repo = db.repository
    desired_repo = repo.find_one({'full_name': f'{org}/{repo_name}'})
    if desired_repo:
        result = repo.update_one({'_id': desired_repo.get('_id')}, {
            '$push': {'comments': comment}})
    else:
        result = repo.insert_one(
            {'full_name': f'{org}/{repo_name}', 'comments': [comment]})

    return result


def get_repo_comments(org, repo_name):
    repo = db.repository
    res = repo.find_one({'full_name': f'{org}/{repo_name}'})
    # workaround to fix ObjectID not serializeable
    res["_id"] = str(res["_id"])
    return res
