from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone
from issues.models import Issue, Assignee


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

class ReportView(generic.CreateView):
    model = Issue
    fields = ['issue_label', 'issue_comment', 'issue_category', 'issue_assignee']
    template_name = 'issues/submit.html'

    def form_valid(self, form):
        newIssue = form.save(commit=False)
        newIssue.pub_date = timezone.now()
        newIssue.save()
        return HttpResponseRedirect(newIssue.id)

#TODO make a ModifyView
