from django.shortcuts import render

from django.contrib.auth.decorators import login_required

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from .serializers import MilestoneSerializer, ImageSerializer
from .models import Milestone, MilestoneImage


@login_required
def home(request):
    return render(request, 'social_app/home.html')


class MilestoneViewSet(viewsets.ModelViewSet):
    serializer_class = MilestoneSerializer
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def get_queryset(self):
        return self.request.user.milestone_set.all()

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


class ImageViewSet(viewsets.ModelViewSet):
    serializer_class = ImageSerializer
    parser_classes = [MultiPartParser, FormParser]

    def get_queryset(self):
        return MilestoneImage.objects.filter(milestone__creator=self.request.user)
