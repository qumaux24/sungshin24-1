from django.apps import AppConfig
from django.utils import timezone
# from .models import DailyNumbers  # DailyNumbers 모델을 임포트합니다.
# from .views.daily_views import generate_daily_numbers
from django.db.models.signals import post_migrate


class PostConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'post'
    
    def ready(self):
        
        from .models import DailyNumbers
        from .views.daily_views import generate_daily_numbers
        
        from .cron import initialize_scheduler
        initialize_scheduler()   
        
        create_default_categories()   
        
        today = timezone.now().date()
        if not DailyNumbers.objects.filter(date=today).exists():
            generate_daily_numbers()
            
        post_migrate.connect(post_migrate_setup, sender=self)
        
def create_default_categories():
    from .models import Category

    default_categories = {
        "koreapost": "한식",
        "chinapost": "중식",
        "japanpost": "일식",
    }

    for name, nickname in default_categories.items():
        Category.objects.get_or_create(name=name, defaults={"nickname": nickname})  # 없으면 생성
    print(" 기본 카테고리 자동 생성 완료!")
    
def post_migrate_setup(sender, **kwargs):
    from .models import DailyNumbers
    from .views.daily_views import generate_daily_numbers

    # 기본 카테고리 생성
    create_default_categories()

    # DailyNumbers 자동 생성
    today = timezone.now().date()
    if not DailyNumbers.objects.filter(date=today).exists():
        generate_daily_numbers()
        print(" 마이그레이션 후 DailyNumbers 자동 생성 완료!")