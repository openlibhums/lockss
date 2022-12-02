from django.shortcuts import render, reverse
from django.utils import timezone

from journal import models
from submission import models as submission_models


def index(request):
    if not request.GET.get('year'):
        current_year = timezone.now().year
    else:
        current_year = request.GET.get('year')

    if int(current_year) == timezone.now().year:
        next = False
        previous = int(current_year) - 1
    else:
        next = int(current_year) + 1
        previous = int(current_year) - 1

    check_for_issues_in_previous_years = models.Issue.objects.filter(date__year__lte=previous,
                                                                     journal=request.journal)
    if not check_for_issues_in_previous_years:
        previous = None

    issues = models.Issue.objects.filter(date__year=current_year,
                                         journal=request.journal)
    articles = submission_models.Article.objects.filter(date_published__year=current_year,
                                                        journal=request.journal)

    template = 'clockss/index.html'
    context = {
        'issues': issues,
        'articles': articles,
        'current_year': current_year,
        'next': next,
        'previous': previous,

    }

    return render(request, template, context)
