from django.shortcuts import render_to_response

def test(request):
    """
    Test page.
    """
    return render_to_response("assignment/test.html")
