# views.py

import random
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from ..models import DailyNumbers, Post, Image

def generate_daily_numbers():
    print("Function generate_daily_numbers is running")
    today = timezone.now().date()
    if not DailyNumbers.objects.filter(date=today).exists():
        post_ids = list(Post.objects.values_list('id', flat=True))
        print(post_ids)
        if len(post_ids) >= 3:
            random_numbers = random.sample(post_ids, 3)
            DailyNumbers.objects.create(
                daily1=random_numbers[0],
                daily2=random_numbers[1],
                daily3=random_numbers[2],
            )
            


def daily_posts_view(request):
    today = timezone.now().date()
    daily_numbers = get_object_or_404(DailyNumbers, date=today)
    post1 = get_object_or_404(Post, id=daily_numbers.daily1)
    # print(f"post1.id: {post1.id}")
    image1=Image.objects.filter(post=post1).first()
    post2 = get_object_or_404(Post, id=daily_numbers.daily2)
    image2=Image.objects.filter(post=post2).first()
    post3 = get_object_or_404(Post, id=daily_numbers.daily3)
    image3=Image.objects.filter(post=post3).first()
    context={
        'post1': post1,
        'post2': post2,
        'post3': post3,
        'image1': image1,
        'image2': image2,
        'image3': image3,
    }
    return context
