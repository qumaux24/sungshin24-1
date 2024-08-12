# management/commands/init_daily_numbers.py
from django.core.management.base import BaseCommand
from django.utils import timezone
from post.models import DailyNumbers
from post.views.daily_views import generate_daily_numbers

class Command(BaseCommand):
    help = 'Initialize DailyNumbers for today'

    def handle(self, *args, **options):
        today = timezone.now().date()
        if not DailyNumbers.objects.filter(date=today).exists():
            generate_daily_numbers()
            self.stdout.write(self.style.SUCCESS('DailyNumbers initialized successfully'))
        else:
            self.stdout.write(self.style.SUCCESS('DailyNumbers already exists for today'))
