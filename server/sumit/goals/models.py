from django.db import models

import sumit.goals.constants as consts
from sumit.common.models import AbstractBaseModel
from sumit.core.models import User


class Category(AbstractBaseModel):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name_plural = "Categories"


class Subcategory(AbstractBaseModel):
    name = models.CharField(max_length=255, unique=True)
    category = models.ForeignKey(Category, related_name="goals", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name_plural = "Subcategories"


class Currency(AbstractBaseModel):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=3, unique=True)
    symbol = models.CharField(max_length=3)

    def __str__(self):
        return str(self.code)

    class Meta:
        verbose_name_plural = "Currencies"


class GoalQuerySet(models.QuerySet):
    def for_user(self, user):
        return self.filter(user=user)


class Goal(AbstractBaseModel):
    user = models.ForeignKey(User, related_name="goals", on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    subcategory = models.ForeignKey(Subcategory, related_name="goals", on_delete=models.CASCADE)
    goal_type = models.CharField(choices=consts.GOAL_TYPE_CHOICES, max_length=255)
    goal_format = models.CharField(choices=consts.GOAL_FORMAT_CHOICES, max_length=255, default=consts.TOTAL)
    active = models.BooleanField(default=True)
    end_date = models.DateField(null=True, blank=True)
    total = models.DecimalField(decimal_places=2, max_digits=16)
    currency = models.ForeignKey(Currency, related_name="goals", on_delete=models.CASCADE)

    objects = GoalQuerySet.as_manager()

    @property
    def current_balance(self):
        total_balance = 0
        for account in self.bank_accounts.all():
            total_balance += account.bank_balances.order_by("-date").first().balance
        return total_balance

    @property
    def progress(self):
        if self.total == 0:
            return 0
        if self.total < 0:
            return round((self.total - self.current_balance) / self.total * 100)
        return round(self.current_balance / self.total * 100)

    @property
    def achieved(self):
        return self.current_balance >= 0 and self.current_balance >= self.total

    def __str__(self):
        return str(self.name)
