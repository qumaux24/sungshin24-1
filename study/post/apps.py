from django.apps import AppConfig
# from django.utils import timezone
# from .models import DailyNumbers  # DailyNumbers 모델을 임포트합니다.
# from .views.daily_views import generate_daily_numbers


class PostConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'post'
    
    def ready(self):
        from .cron import initialize_scheduler
        initialize_scheduler()
        
        # today = timezone.now().date()
        # if not DailyNumbers.objects.filter(date=today).exists():
        #     generate_daily_numbers()
