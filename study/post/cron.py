# cron.py

from django_apscheduler.jobstores import DjangoJobStore, register_events
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from .views.daily_views import generate_daily_numbers

def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_jobstore(DjangoJobStore(), "daily_post")

    scheduler.add_job(
        generate_daily_numbers,
        trigger=CronTrigger(hour="00", minute="00"),  # 매일 자정에 실행
        id="generate_daily_numbers",
        max_instances=1,
        replace_existing=True,
        jobstore='daily_post',
    )

    register_events(scheduler)
    scheduler.start()
    print("Scheduler started!")

def initialize_scheduler():
    start_scheduler()
