from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


# -------------------------------------------------------------------
#   1. Serializer para criação/registro
# -------------------------------------------------------------------
class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        min_length=6,
        style={"input_type": "password"},
        help_text="Senha precisa ter no mínimo 6 caracteres.",
    )

    class Meta:
        model = User
        fields = ["id", "email", "username", "password"]

    def validate_email(self, value):
        """
        Garante que não exista usuário com o mesmo email.
        """
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Este e-mail já está em uso.")
        return value

    def create(self, validated_data):
        """
        Criação segura do usuário com set_password.
        """
        password = validated_data.pop("password")
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user


# -------------------------------------------------------------------
#   2. Serializer de perfil (visualização e edição)
# -------------------------------------------------------------------
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "username",
            "bio",
            "avatar",
            "website",
            "location",
            "is_verified",
            "date_joined",
        ]
        read_only_fields = ["id", "email", "is_verified", "date_joined"]
