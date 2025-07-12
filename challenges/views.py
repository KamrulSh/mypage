from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_challenges = {
    "january": "January challenge",
    "february": "February challenge",
    "march": "March challenge",
    "april": "April challenge",
    "may": "May challenge",
    "june": "June challenge",
    "july": "July challenge",
    "august": "August challenge",
    "september": "September challenge",
    "october": "October challenge",
    "november": "November challenge",
    "december": "December challenge",
}


def index(request):
    return HttpResponse("Hello, world. You're at the index page.")


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("<h1>Not found</h1>")
    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        response_text = monthly_challenges[month]
        response_data = f"<h1>{response_text}</h1>"
        return HttpResponse(response_data)
    except KeyError:
        return HttpResponseNotFound("<h1>Not found</h1>")
