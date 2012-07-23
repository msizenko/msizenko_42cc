from django.shortcuts import render_to_response

def test(request):
    """
    Test page.
    """
    return render_to_response("assignment/test.html")
    
def index(request):
    return render_to_response("assignment/index.html")
