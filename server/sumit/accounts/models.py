from django.db import models

from sumit.common.models import AbstractBaseModel
from sumit.core.models import User
from sumit.goals.models import Currency, Goal


class Bank(AbstractBaseModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return str(self.name)


class BankAccount(AbstractBaseModel):
    user = models.ForeignKey(User, related_name="bank_accounts", on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    bank = models.ForeignKey(Bank, related_name="bank_accounts", on_delete=models.CASCADE)
    currency = models.ForeignKey(Currency, related_name="bank_accounts", on_delete=models.CASCADE)
    goal = models.ForeignKey(Goal, related_name="bank_accounts", on_delete=models.CASCADE)

    @property
    def current_balance(self):
        return self.bank_balances.order_by("date").first().balance

    def __str__(self):
        return str(self.name)


class BankBalance(AbstractBaseModel):
    account = models.ForeignKey(BankAccount, related_name="bank_balances", on_delete=models.CASCADE)
    date = models.DateField()
    balance = models.DecimalField(decimal_places=2, max_digits=16)

    def __str__(self):
        return str(self.account.name)
