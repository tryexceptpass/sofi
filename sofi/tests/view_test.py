from .. import View

def test_basic():
    assert(str(View()) == "<!DOCTYPE html><html><head><link href=\"https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css\" rel=\"stylesheet\"></head><body><script src=\"https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js\"></script></body></html>")