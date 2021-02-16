from django.db import models
from accounts.models import Account


class Organisation(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    administrator = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, related_name='admin_of')
    is_activated = models.BooleanField(default=None, verbose_name='Activated', null=True)
    members = models.ManyToManyField(Account, related_name='belong_to')

    def __str__(self):
        return self.name


class JoinRequest(models.Model):
    id = models.AutoField(primary_key=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='org_joinreqs')
    org = models.ForeignKey(Organisation, on_delete=models.CASCADE, related_name='joinreqs')
    date_created = models.DateTimeField(auto_now_add=True)
    accepted = models.BooleanField(default=None, null=True)

    def __str__(self):
        return self.account.username + '-' + self.org.name 
