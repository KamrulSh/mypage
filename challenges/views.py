from django.http import HttpResponse, HttpResponseNotFound


def index(request):
    return HttpResponse("Hello, world. You're at the index page.")


def monthly_challenges_by_number(request, month):
    return HttpResponse(
        f"Hello, world. You're at the monthly challenge {month}."
    )


def monthly_challenges(request, month):
    response_text = None
    if month == "january":
        response_text = f"Hello, world. You're at the {month.upper()} challenge."
    elif month == "february":
        response_text = f"Hello, world. You're at the {month.upper()} challenge."
    else:
        HttpResponseNotFound("Not found")
    return HttpResponse(response_text)
