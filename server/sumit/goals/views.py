from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, mixins, permissions, viewsets

from sumit.goals.serializers import GoalSerializer

from .models import Goal


class GoalViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Goal.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = ["end_date"]

    def get_queryset(self):
        return Goal.objects.for_user(self.request.user)

    def get_serializer_class(self):
        return GoalSerializer
