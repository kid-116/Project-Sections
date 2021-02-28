from django.db import models
from accounts.models import Account
from organisations.models import Organisation


class Bracket(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    graduation_year = models.IntegerField()
    members = models.ManyToManyField(Account, related_name="brackets", blank=True, verbose_name='Members')
    organisation = models.ForeignKey(Organisation, related_name="brackets", on_delete=models.CASCADE)
    cr = models.ForeignKey(
        Account, 
        on_delete=models.SET_NULL, 
        default=None, 
        blank=True, 
        related_name='cr_of',
        null=True)
    faculty_advisor = models.ForeignKey(
        Account, 
        on_delete=models.SET_NULL, 
        default=None, 
        blank=True, 
        null=True,
        related_name='facadv_of')

    def __str__(self):
        return self.name + '-' + self.organisation.name

        
class JoinRequest(models.Model):
    id = models.AutoField(primary_key=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, default=None, related_name="join_requests")
    bracket = models.ForeignKey(
        Bracket, 
        on_delete=models.CASCADE, 
        default=None, 
        related_name="join_requests")
    date_created = models.DateTimeField(auto_now_add=True)
    accepted = models.BooleanField(default=None, null=True)

    def __str__(self):
        return self.account.username + '-' + self.bracket.name
