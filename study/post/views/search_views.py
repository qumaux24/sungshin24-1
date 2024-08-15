from django.shortcuts import render,redirect, get_object_or_404
from ..models import Post, Image, Comment, Category
from accounts.models import User_detail
from ..forms import PostForm, CommentForm
from django.core.paginator import Paginator
from django.views.decorators.http import require_POST
from django.db.models import Count, Q
from .daily_views import daily_posts_view
from ..models import Userpost, Comment

def search(request, writer_id):

    if request.method == 'POST':
        # search_select2 = request.GET.get('search_select2')
        # searched = request.POST['searched']
        user_detail=get_object_or_404(User_detail, user_id=writer_id)
        allergies=set(user_detail.allergies.replace(',',' ').split())
        allergies = set(allergy.strip().lower() for allergy in allergies)
        

        search_select = request.POST.get('search_select')  # 폼에서 선택한 검색 조건을 가져옴
        searched = request.POST.get('searched', '')

        # 검색어 리스트에서 빈 문자열 제거
        # search_terms = [term for term in search_terms if term]
        search_terms = set(searched.replace(',', ' ').split())
        search_terms = set(term.lower() for term in search_terms)
        
        # for term in search_terms:
        #     query |= Q(search_select2__icontains=term)
        query1 = Q()
        for term in search_terms:
            if search_select == '제목':
                query1 |= Q(title__icontains=term)
            elif search_select == '재료':
                query1 |= Q(ingredient__icontains=term)
            else:
                query1 |= Q(title__icontains=term) | Q(ingredient__icontains=term)
                
        query2 = Q()
        for allergy in allergies:
            query2 |= Q(ingredient__icontains=allergy)
                        
        query=query1 & ~query2
                
        posts = Post.objects.filter(query)
        post_with_count = []
        for post in posts:
            count = 0
            for term in search_terms:
                if search_select == '제목':
                    count += post.title.lower().count(term.lower())
                elif search_select == '재료':
                    count += post.ingredient.lower().count(term.lower())
                else:
                    count += post.title.lower().count(term.lower())
                    count += post.ingredient.lower().count(term.lower())
            post_with_count.append((post, count, post.created_at))
        
        # 포함된 검색어 개수로 게시글 정렬
        post_with_count.sort(key=lambda x: (x[1], x[2]), reverse=True)
        sorted_posts = [post for post, count, post.created_at in post_with_count]
            # query |= Q(content__icontains=term) | Q(title__icontains=term) #제목과 내용 둘 다에서 검색
        # 조건에 맞는 게시물 검색
        
        return render(request, 'searched.html', {'searched': searched, 'posts': sorted_posts})
    else:
        return render(request, 'searched.html', {})
    
def user_search(request, writer_id):
    if request.method == 'POST':
        
        if request.method == 'POST':
            search_select = request.POST.get('usersearch_select')  # 폼에서 선택한 검색 조건을 가져옴
            searched = request.POST.get('usersearched', '')
        
        intermediate_terms = searched.split()
        
        search_terms = []
        for term in intermediate_terms:
            search_terms.extend(term.split(','))

        search_terms = set(searched.replace(',', ' ').split())
        
        query = Q()
        for term in search_terms:
            if search_select == '제목':
                query |= Q(title__icontains=term)
            elif search_select == '내용':
                query |= Q(content__icontains=term)
            else:
                query |= Q(title__icontains=term) | Q(content__icontains=term)
        posts = Userpost.objects.filter(query)
        return render(request, 'searched_userpost.html', {'searched': searched, 'post_list': posts})
    else:
        return render(request, 'searched_userpost.html', {})