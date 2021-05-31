from django.shortcuts import render
from datetime import date

from django.contrib.auth.decorators import login_required

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from .serializers import MilestoneSerializer, ImageSerializer
from .models import Milestone, MilestoneImage


@login_required
def home(request):
    user = request.user
    milestones = Milestone.objects.filter(
        creator=user).order_by('date')
    return render(request, 'social_app/home.html', {'milestones': milestones})


@login_required
def milestone(request):
    return render(request, 'social_app/milestone.html')


class MilestoneViewSet(viewsets.ModelViewSet):
    serializer_class = MilestoneSerializer
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def get_queryset(self):
        today = date.today()
        return self.request.user.milestone_set.all().order_by('date')
        # return Milestone.objects.filter(creator=self.request.user).filter(date__gte=today).order_by('date')

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


class ImageViewSet(viewsets.ModelViewSet):
    serializer_class = ImageSerializer
    parser_classes = [MultiPartParser, FormParser]

    def get_queryset(self):
        return MilestoneImage.objects.filter(milestone__creator=self.request.user)
