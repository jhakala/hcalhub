from __future__ import unicode_literals

import datetime
from django.db import models
from django.utils import timezone

class Issue(models.Model):
    issue_label = models.CharField(max_length=100)
    issue_comment = models.CharField(max_length=20000, default="")
    issue_category = models.CharField(max_length=30, default="")
    issue_assignee = models.CharField(max_length=50, default="unassigned")
    issue_status = models.CharField(max_length=30, default="")
    issue_dump = models.TextField(default="")
    pub_date = models.DateTimeField("Date reported")
    close_date = models.DateTimeField("Date closed", null=True, blank=True)
    def get_age(self):
        return (timezone.now() - self.pub_date) 
    def __str__(self):
        return "Label: %s\nComment: %s\nCategory: %s\nAssignee: %s\nStatus: %s\nDate reported: %s\nAge: %s" % (
          self.issue_label, self.issue_comment, self.issue_category, self.issue_assignee, 
          self.issue_status, self.pub_date, self.get_age()                                         )
    
class Assignee(models.Model):
    name = models.CharField(max_length=50)   
    email = models.EmailField(default="")
    issues = models.ForeignKey( Issue, on_delete=models.CASCADE, blank=True, null=True)
    def __str__(self):
        return "Name: %s, Email: %s, Issues: %s" % (self.name, self.email, self.issues)
