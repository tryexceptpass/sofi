from sofi.ui import View

def test_basic():
    assert(str(View()) == "<head><title>Sofi</title><link href=\"https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css\" rel=\"stylesheet\"></head><body></body>")
