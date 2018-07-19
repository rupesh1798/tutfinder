from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):

    def handle(self, *args, **options):
        if not User.objects.filter(username="gonoobieadmin").exists():
            User.objects.create_superuser("gonoobieadmin", "gonoobieteam@gmail.com", "ploplo00!")
            self.stdout.write(self.style.SUCCESS('Successfully created new super user'))
