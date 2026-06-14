from urllib.parse import quote


def test_signup_success(client):
    activity = "Chess Club"
    email = "newstudent@mergington.edu"
    url = f"/activities/{quote(activity)}/signup"
    resp = client.post(url, params={"email": email})
    assert resp.status_code == 200
    assert resp.json()["message"] == f"Signed up {email} for {activity}"

    # verify participant added
    get = client.get("/activities")
    assert email in get.json()[activity]["participants"]


def test_signup_existing_fails(client):
    activity = "Chess Club"
    existing = "michael@mergington.edu"
    url = f"/activities/{quote(activity)}/signup"
    resp = client.post(url, params={"email": existing})
    assert resp.status_code == 400
