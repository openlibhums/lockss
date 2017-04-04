from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.utils import timezone

from journal import models
from submission import models as submission_models


def index(request):
    if not request.GET.get('year'):
        current_year = timezone.now().year
    else:
        current_year = request.GET.get('year')

    issues = models.Issue.objects.filter(date__year=current_year)
    articles = submission_models.Article.objects.filter(date_published__year=current_year)

    template = 'clockss/index.html'
    context = {
        'issues': issues,
        'articles': articles,
        'current_year': current_year,
    }

    return render(request, template, context)
