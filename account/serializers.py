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
        if CustomUser.objects.filter(email=email).exists():
            raise serializers.ValidationError({"email":("email already taken.")})
        return super().validate(args)

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        
        # Adding the below line made it work for me.
        instance.is_active = True
        if password is not None:
            # Set password does the hash, so you don't need to call make_password 
            instance.set_password(password) #without this step password is not hashed, user cannot login.
        instance.save()
        return instance
    
    class Meta:
        model = CustomUser
        fields = ['id','name','email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

class CustomUserSerializer2( serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ['id','name','email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }
