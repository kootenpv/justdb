from justdb import JustDB


def test_json():
    j = JustDB()
    obj = {"a": 1}
    j["test.json"] = obj
    assert j["test.json"] == obj
    j.remove("test.json")


def test_fallback():
    j = JustDB()
    fallback = "value if not exist"
    assert j.read("some/path/1", fallback) == fallback


def test_server():
    from justdb.server import create_server
    try:
        create_server()
    except SystemExit:
        pass
