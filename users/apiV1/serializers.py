from django.contrib.auth.models import User
from rest_framework import serializers

class UserCreateSerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField(style={"input_type":"password"},label="Password Tekrar",required=True)

    class Meta:
        model=User
        fields=["first_name","last_name","username","email","password","password_confirm"]
        extra_kwargs={"password":{"write_only":True},"password_confirm":{"write_only":True}}

    def __init__(self,*args,**kwargs):
        super(UserCreateSerializer, self).__init__(*args,**kwargs)
        self.fields["password"].style={"input_type":"password"}
        #self.fields["password_confirm"].style={"input_type":"password"}

    def validate_password_confirm(self, data):
        password=self.get_initial().get("password")
        password_confirm=data

        if password != password_confirm:
            raise serializers.ValidationError("Şifreler Eşleşmedi.")
        return data

    def validate_email(self,value):
        email=value
        user_qs=User.objects.filter(email=email)
        if user_qs.exists():
            raise serializers.ValidationError("Bu email adresi mevcut.")
        return value

    def save(self, **kwargs):
        x=super(UserCreateSerializer, self).save(**kwargs)
        print(x)
        return x

    def update(self, instance, validated_data):
        super(UserCreateSerializer, self).update()
    
    def create(self, validated_data):

        username = validated_data.get("username")
        first_name=validated_data.get("first_name")
        last_name=validated_data.get("last_name")
        email_=validated_data.get("email")
        password=validated_data.get("password")

        new_user = User()
        new_user.username = username
        new_user.first_name=first_name
        new_user.last_name=last_name
        new_user.email=email_
        new_user.set_password(password)
        new_user.save()

        return validated_data

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=50,required=True)
    token = serializers.CharField(read_only=True)
    password = serializers.CharField(style={"input_tyoe":"password"},write_only=True)