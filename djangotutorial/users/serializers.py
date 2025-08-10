from rest_framework import serializers
from django.contrib.auth.models import Permission
from .models import User, Role

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = User
        fields = ['username', 'password']


    def create(self, validated_data):
        user = User.objects.create_user(
            username = validated_data['username'],
            password = validated_data['password'],
        )

        respondents, created = Role.objects.get_or_create(name='respondents')

        if created:
            view_question = Permission.objects.get(codename='view_question')
            can_answer = Permission.objects.get(codename='can_answer_question')
            respondents.Permission.set([view_question, can_answer])

        user.groups.add(respondents)

        return user

