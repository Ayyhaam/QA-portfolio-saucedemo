"""API tests for JSONPlaceholder (https://jsonplaceholder.typicode.com).

JSONPlaceholder is a free fake REST API for practice. It accepts POST/PUT/DELETE
and answers like a real API, but nothing is really saved.
"""
import pytest


@pytest.mark.smoke
def test_tc11_get_all_posts(api):
    response = api.get("/posts")
    assert response.status == 200
    posts = response.json()
    assert len(posts) == 100


def test_tc12_get_one_post(api):
    response = api.get("/posts/1")
    assert response.status == 200
    post = response.json()
    assert post["id"] == 1
    assert post["userId"] == 1
    assert post["title"] != ""


def test_tc13_filter_posts_by_user(api):
    response = api.get("/posts", params={"userId": 1})
    assert response.status == 200
    posts = response.json()
    assert len(posts) > 0
    assert all(post["userId"] == 1 for post in posts)


def test_tc14_create_post(api):
    new_post = {"title": "My test post", "body": "Hello from pytest", "userId": 1}
    response = api.post("/posts", data=new_post)
    assert response.status == 201
    created = response.json()
    assert created["title"] == "My test post"
    assert "id" in created


def test_tc15_update_post(api):
    changed = {"id": 1, "title": "Updated title", "body": "Updated body", "userId": 1}
    response = api.put("/posts/1", data=changed)
    assert response.status == 200
    assert response.json()["title"] == "Updated title"


def test_tc16_delete_post(api):
    response = api.delete("/posts/1")
    assert response.status == 200


def test_tc17_get_post_that_does_not_exist(api):
    response = api.get("/posts/99999")
    assert response.status == 404
