from rest_framework import serializers, fields
from .models import Milestone, MilestoneImage


class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = MilestoneImage
        fields = ['milestone', 'image']


class MilestoneSerializer(serializers.ModelSerializer):

    date = fields.DateField(input_formats=['%Y-%m-%d'])
    images = serializers.SerializerMethodField()

    def get_images(self, obj):
        images = MilestoneImage.objects.filter(milestone=obj)
        return ImageSerializer(images, many=True, read_only=False).data

    class Meta:
        model = Milestone
        fields = ('id', 'name', 'description', 'date', 'images')
