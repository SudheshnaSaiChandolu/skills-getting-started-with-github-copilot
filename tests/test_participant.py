from urllib.parse import quote


def test_unregister_success(client):
    activity = "Chess Club"
    email = "daniel@mergington.edu"
    url = f"/activities/{quote(activity)}/participant"
    resp = client.delete(url, params={"email": email})
    assert resp.status_code == 200
    assert resp.json()["message"] == f"Unregistered {email} from {activity}"

    # verify removed
    get = client.get("/activities")
    assert email not in get.json()[activity]["participants"]


def test_unregister_not_registered(client):
    activity = "Chess Club"
    email = "notfound@mergington.edu"
    url = f"/activities/{quote(activity)}/participant"
    resp = client.delete(url, params={"email": email})
    assert resp.status_code == 400


def test_unregister_activity_not_found(client):
    activity = "Nonexistent"
    email = "x@y.com"
    url = f"/activities/{quote(activity)}/participant"
    resp = client.delete(url, params={"email": email})
    assert resp.status_code == 404
