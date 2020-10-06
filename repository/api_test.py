from flask import json


from api import app


def test_comment_on_repo():
    app.test_client().post(
        '/comment/golang/golang',
        data=json.dumps({'comment': 'this is a test'}),
        content_type='application/json',
    )
    response = app.test_client().get('golang/golang/comments')

    data = json.loads(response.get_data(as_text=True))

    assert response.status_code == 200
    assert data['comments'][0] == 'this is a test'


def test_bookmark_repo():
    app.test_client().post(
        '/bookmark/golang/golang'
    )

    response = app.test_client().get(
        '/bookmarks'
    )

    data = json.loads(response.get_data(as_text=True))
    assert response.status_code == 200
    assert data[0] == 'golang/golang'
