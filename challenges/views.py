from django.http import HttpResponse, HttpResponseNotFound


def index(request):
    return HttpResponse("Hello, world. You're at the index page.")


def monthly_challenges(request, month):
    response_text = None
    if month == "january":
        response_text = "Hello, world. You're at the January challenge."
    elif month == "february":
        response_text = "Hello, world. You're at the February challenge."
    else:
        HttpResponseNotFound("Not found")
    return HttpResponse(response_text)
