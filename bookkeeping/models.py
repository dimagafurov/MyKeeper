from django.db import models


# Create your models here.
class Account(models.Model):
    date_add = models.DateTimeField('Date added')
    start_amount = models.DecimalField('Money Amount', max_digits=11, decimal_places=2)
    account_description = models.CharField(max_lenght=2000)
#    account_type = models.IntegerField()
    account_type = models.ForeignKey(AccountType)
    date_delete = models.DateTimeField('Date deleted')


class AccountType(models.Model):
    account_type_description = models.CharField(max_lenght=2000)


class Transaction(models.Model):
    transaction_

class Transaction(models.Model):

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)