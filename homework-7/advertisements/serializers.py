from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from advertisements.models import Advertisement


class UserSerializer(serializers.ModelSerializer):
    """Serializer для пользователя."""

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name',
                  'last_name',)


class AdvertisementSerializer(serializers.ModelSerializer):
    """Serializer для объявления."""

    creator = UserSerializer(
        read_only=True,
    )

    class Meta:
        model = Advertisement
        fields = ('id', 'title', 'description', 'creator',
                  'status', 'created_at', )

    def create(self, validated_data):
        """Метод для создания"""

        # Простановка значения поля создатель по-умолчанию.
        # Текущий пользователь является создателем объявления
        # изменить или переопределить его через API нельзя.
        # обратите внимание на `context` – он выставляется автоматически
        # через методы ViewSet.
        # само поле при этом объявляется как `read_only=True`
        validated_data["creator"] = self.context["request"].user
        return super().create(validated_data)

    def validate(self, data):
        """Метод для валидации. Вызывается при создании и обновлении."""

        if self.context["request"].method == 'POST':
            open_adv = Advertisement.objects.filter(creator=self.context["request"].user, status="OPEN")
            if len(open_adv) >= 10:
                raise ValidationError("Создать можно не более 10 объявлений")

        if self.context["request"].method == 'PATCH':
            if data.get('status') == 'OPEN':
                open_adv = Advertisement.objects.filter(creator=self.context["request"].user, status="OPEN")
                if len(open_adv) >= 10:
                    raise ValidationError("Открытых объявлений может быть не более 10")

        return data
