from rest_framework import serializers

from .models import Lead, Agent


class LeadSerializer(serializers.ModelSerializer):
    """ API сериализатор для Лидов. """

    class Meta:
        model = Lead
        fields = ('name', 'email', 'phone', 'funnel')


class AgentSerializer(serializers.ModelSerializer):
    """ API сериализатор для агентов. """

    class Meta:
        model = Agent
        fields = ('id', 'first_name', 'last_name',
                  'email', 'phone', 'date_of_birth', 'is_staff')
