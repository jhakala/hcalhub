from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

# Create your views here.

from .models import Issue, Assignee

class IndexView(generic.ListView):
    template_name = 'issues/index.html'
    context_object_name = 'latest_issue_list'

    def get_queryset(self):
        """Return the last 25 published issues."""
        return Issue.objects.order_by('-pub_date')[:25]

class DetailView(generic.DetailView):
    model = Issue
    template_name = 'issues/detail.html'
