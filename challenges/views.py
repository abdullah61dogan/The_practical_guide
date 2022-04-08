from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.

monthly_challenges = {
    "january": "Read 20 pages of paper for the entire mounth!",
    "february": "Sleep less than 7 hours for an entire mounth!",
    "march": "Walk for at least 20 minutes every day!",
    "april": "Read 20 pages of paper for the entire mounth!",
    "may": "Sleep less than 7 hours for an entire mounth!",
    "june": "Walk for at least 20 minutes every day!",
    "july": "Read 20 pages of paper for the entire mounth!",
    "august": "Sleep less than 7 hours for an entire mounth!",
    "september": "Walk for at least 20 minutes every day!",
    "october": "Read 20 pages of paper for the entire mounth!",
    "november": "Sleep less than 7 hours for an entire mounth!",
    "december": None
}


def index(request):
    months = list(monthly_challenges.keys())

    return render(request, "challenges/index.html", {
        "months": months
    })


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month")

    # URL path config ==> /challenge/january
    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month_name": month
        })
    except:
        response_data = render_to_string("404.html")
        return HttpResponseNotFound(response_data)
