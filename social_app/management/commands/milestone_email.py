from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import date
from social_app.models import Milestone
from django.core.mail import send_mail


class Command(BaseCommand):
    help = 'send a reminder for a milestone'

    def handle(self, *args, **kwargs):
        today = date.today()
        milestone = Milestone.objects.filter(date=today)
        if milestone:
            for m in milestone:
                mail_subject = [m.name, m.description,
                                m.date, m.milestoneimage_set.all()]
                message = 'Reminder'
                to_email = 'kazal@gmail.com'
                send_mail(mail_subject, message,
                          'salmansiddik19@gmail.com', [to_email])
        else:
            print('There are no milestone in today...')
