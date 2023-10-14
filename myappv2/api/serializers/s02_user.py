from rest_framework import serializers
from phonenumber_field.serializerfields import PhoneNumberField
from main import models

# Custom User Serializer
class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CustomUser()
        exclude = (
            "password",
            "last_login",
            "date_joined",
            "groups",
            "user_permissions",
        )


# Login Serializer
class LoginSerializer(serializers.Serializer):
    email                   = serializers.CharField(required = False)
    phone                   = serializers.CharField(required = False)
    password                = serializers.CharField()
    device                  = serializers.CharField(required = False)
    token_type              = serializers.CharField()
    method                  = serializers.CharField()


# Check Reset Code Serializer
class ResetCodeSerializer(serializers.Serializer):
    check_type              = serializers.CharField()
    email                   = serializers.CharField(required = False)
    phone                   = serializers.CharField(required = False)
    code                    = serializers.CharField()
    password                = serializers.CharField(required = False)


# Register User Serializer
class RegisterUserSerializer(serializers.Serializer):
    reg_type                = serializers.CharField()
    email                   = serializers.CharField(required = False)
    phone                   = serializers.CharField(required = False)
    password                = serializers.CharField()


# Activate Account Serializer
class ActivateAccountSerializer(serializers.Serializer):
    act_type                = serializers.CharField()
    email                   = serializers.CharField(required = False)
    phone                   = serializers.CharField(required = False)
    code                    = serializers.CharField()


# Send Activation Code Serializer
class SendActivationCodeSerializer(serializers.Serializer):
    email                   = serializers.CharField(required = False)
    phone                   = serializers.CharField(required = False)
    act_type                = serializers.CharField()


# Change Email/Phone Number during Activation
class ChangeEmailPhoneSerializer(serializers.Serializer):
    change_type             = serializers.CharField()
    old_email               = serializers.CharField(required = False)
    old_phone               = serializers.CharField(required = False)
    email                   = serializers.CharField(required = False)
    phone                   = serializers.CharField(required = False)



# Send Reset Link Serializer
class SendResetLinkSerializer(serializers.Serializer):
    email                   = serializers.CharField(required = False)
    phone                   = serializers.CharField(required = False)
    method                  = serializers.CharField()


# Email Confirmation Token
class EmailConfirmationSerializer(serializers.Serializer):
    email                   = serializers.EmailField()


# Notification Serializer
class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserNotification
        exclude = (
            "user",
        )


# Change Notification Status Serializer
class NotificationStatusSerializer(serializers.Serializer):
    tokens                  = serializers.CharField()
    id                      = serializers.IntegerField(required = False)
    page                    = serializers.IntegerField(required = False)


# Property Model Serializer with some Fields
class WishlistPropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Property
        fields = (
            "name",
            "id",
            "price",
            "cur"
        )


# Wishlist Item Model Serializer
class WistlistItemSerializer(serializers.ModelSerializer):
    property_model = WishlistPropertySerializer()
    class Meta:
        model = models.WistlistItem
        fields = ("__all__")



# Wishlist Model Serializer
class WishlistSerializer(serializers.ModelSerializer):
    items = WistlistItemSerializer(many = True)
    class Meta:
        model = models.Wishlist
        fields = ("__all__")


# Get WishLists Serializer
class GetWishlistsSerializer(serializers.Serializer):
    tokens                  = serializers.CharField()
    page                    = serializers.CharField(required = False)


# Add Wishlist Serializer
class AddWishlistSerializer(serializers.Serializer):
    tokens                  = serializers.CharField()
    name                    = serializers.CharField()
    date                    = serializers.CharField()


# Delete Wishlist Serializer
class DelWishlistSerializer(serializers.Serializer):
    tokens                  = serializers.CharField()
    id                      = serializers.IntegerField()


# Add Item to Wishlist
class AddWishlistItemSerializer(serializers.Serializer):
    tokens                  = serializers.CharField()
    id                      = serializers.IntegerField()
    pid                     = serializers.IntegerField()
    date                    = serializers.CharField()


# Del Item from Wishlist
class DelWishlistItemSerializer(serializers.Serializer):
    tokens                  = serializers.CharField()
    id                      = serializers.IntegerField()
    iid                     = serializers.IntegerField()







