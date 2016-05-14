from sys import argv
import django
django.setup()

saveToDatabase=argv[1]

from django.utils import timezone
from issues.models import Issue, Assignee

issue = Issue(issue_label="test issue", pub_date=timezone.now())
if saveToDatabase == "save":
  issue.save()
  print "Issue id: %i" % issue.id
print issue

assignee = Assignee(name="John Hakala", email="john_hakala@brown.edu")
if saveToDatabase == "save":
  assignee.save()
  print "Assignee id: %i"  % assignee.id
print assignee
