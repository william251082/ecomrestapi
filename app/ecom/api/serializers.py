from rest_framework import serializers

from ecom.models import Owner, Product


class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    # owner = serializers.CharField()
    name = serializers.CharField()
    description = serializers.CharField()
    body = serializers.CharField()
    location = serializers.CharField()
    release_date = serializers.DateField()
    active = serializers.BooleanField()
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        print(validated_data)
        return Product.objects.create(**validated_data)

    def update(self, instance, validated_data):
        # instance.owner = validated_data.get('owner', instance.owner)
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.body = validated_data.get('body', instance.body)
        instance.location = validated_data.get('location', instance.location)
        instance.release_date = validated_data.get('release_date', instance.release_date)
        instance.active = validated_data.get('active', instance.active)
        instance.save()
        return instance

    def validate(self, data):
        """ check that description and name are different
        https://www.django-rest-framework.org/api-guide/serializers/#object-level-validation
        """
        if data["name"] == data["description"]:
            raise serializers.ValidationError("Name and Description must be different from one another!")
        return data

    def validate_name(self, value):
        """ check that name is at least 6 chars long
        https://www.django-rest-framework.org/api-guide/serializers/#field-level-validation
        """
        if len(value) < 6:
            raise serializers.ValidationError("The name has to be at least 6 chars long!")
        return value


class OwnerSerializer(serializers.ModelSerializer):
    products = serializers.HyperlinkedRelatedField(many=True,
                                                   read_only=True,
                                                   view_name="product_detail")

    class Meta:
        model = Owner
        fields = "__all__"


