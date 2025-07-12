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
    list_items = ""
    months = list(monthly_challenges.keys())
    for month in months:
        capt_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href='{month_path}'>{capt_month}</a></li>"
    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)


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
