from rest_framework import serializers

class HealthCheckSerializer(serializers.Serializer):
    DATABASE = 0
    API_INTEGRATION = 1

    COMPONENT_CHOICES = (
        (DATABASE, "Database"),
        (API_INTEGRATION, "API Integration")
    )

    component = serializers.ChoiceField(choices=COMPONENT_CHOICES) # числовое значение