import rest_framework_simplejwt 
from rest_framework import serializers
from .models import CustomUser

class MyTokenObtainPairSerializer(rest_framework_simplejwt.serializers.TokenObtainPairSerializer):
    
    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        refresh["my_claim"] = "value" # here you can add custom cliam
        refresh['email'] = self.user.email
        refresh['foo'] = ["foo1", "foo2","foo3"]
        refresh['groups'] = list(self.user.groups.values_list('name', flat=True))
        data["refresh"] = str(refresh)
        data["access"] = str(refresh.access_token)
        return data


class ChangePasswordSerializer(serializers.Serializer):    
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    class Meta:
        model = CustomUser

class CustomUserSerializer( serializers.ModelSerializer):
    name = serializers.CharField(min_length=3, max_length=50)
    email = serializers.EmailField(min_length=8, max_length=50)

    def validate(self,args):
        email = args.get("email",None)
        if CustomUser.objects.filter(email=None).exists():
            raise serializers.ValidationError({"email":("email already taken.")})
        return super().validate(args)

    class Meta:
        model = CustomUser
        fields = ['id','name','email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

