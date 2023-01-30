from django.contrib import admin

from sumit.accounts.models import Bank, BankAccount, BankBalance


class BankAccountModelAdmin(admin.ModelAdmin):
    list_display = ("name", "bank", "user")


class BankBalanceModelAdmin(admin.ModelAdmin):
    list_display = ("account", "balance", "date")


admin.site.register(Bank)
admin.site.register(BankBalance, BankBalanceModelAdmin)
admin.site.register(BankAccount, BankAccountModelAdmin)
