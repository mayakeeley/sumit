from rest_framework import serializers

from .models import Category, Currency, Goal, Subcategory


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            "id",
            "name",
        )


class SubcategorySerializer(serializers.ModelSerializer):
    category_ref = CategorySerializer(source="category", read_only=True)

    class Meta:
        model = Subcategory
        fields = (
            "id",
            "name",
            "category_ref",
        )


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = (
            "id",
            "name",
            "code",
            "symbol",
        )


class GoalSerializer(serializers.ModelSerializer):
    subcategory_ref = SubcategorySerializer(source="subcategory", read_only=True)
    currency_ref = CurrencySerializer(source="currency", read_only=True)

    class Meta:
        model = Goal
        fields = (
            "id",
            "name",
            "subcategory",
            "subcategory_ref",
            "goal_type",
            "goal_format",
            "active",
            "end_date",
            "total",
            "currency",
            "currency_ref",
            "current_balance",
            "achieved",
            "progress",
        )
