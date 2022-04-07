from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

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
    "december": "Walk for at least 20 minutes every day!"
}

# Create your views here.


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month")

    redirect_month = months[month - 1]
    return HttpResponseRedirect("/challenges/" + redirect_month)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("Please write one of the months!")
