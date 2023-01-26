from django.contrib import admin

from sumit.goals.models import Category, Currency, Goal, Subcategory


class SubcategoryModelAdmin(admin.ModelAdmin):
    list_display = ("name", "category")


class GoalModelAdmin(admin.ModelAdmin):
    list_display = ("name", "user", "subcategory", "total")


admin.site.register(Currency)
admin.site.register(Goal, GoalModelAdmin)
admin.site.register(Category)
admin.site.register(Subcategory, SubcategoryModelAdmin)
