from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

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
        return HttpResponseNotFound("Not found")
    redirect_month = months[month - 1]
    return HttpResponseRedirect(f"/challenges/{redirect_month}")


def monthly_challenge(request, month):
    try:
        response_text = monthly_challenges[month]
        return HttpResponse(response_text)
    except KeyError:
        return HttpResponseNotFound("Not found")
