from django.shortcuts import render,redirect
from .models import Board
import json


# Create your views here.

# 메인 페이지
def main(request):
    # 세션에서 개체 받기
    user_id = request.session.get('user_id')    # string 타입으로 받아짐
    user = json.loads(user_id)                  # json을 통하여 파싱
    user = user[0]['fields']['nickname']
    
    boards = Board.objects.all()    # 모든 객체 조회
    return render(request, 'board/board_list.html', {'user':user, 'boards':boards})

# 검색 페이지
def search(request):
    # 세션에서 개체 받기
    user_id = request.session.get('user_id')    # string 타입으로 받아짐
    user = json.loads(user_id)                  # json을 통하여 파싱
    user = user[0]['fields']['nickname']
    
    boards = Board.objects.all()
    
    return render(request, 'board/board_search.html', {'boards': boards, 'user': user})

# 검색 결과
def search_result(request):
    if request.method == "POST":
        search_input = request.POST["search_input"]
        search_category = request.POST["category"]
        
        results = Board.objects.all().filter(product__contains=search_input, category=search_category)     # 검색한 단어가 포함되어있는 항목 검색
        return render(request, 'board/board_search_result.html', {'results': results, 'search_input': search_input, 'search_category': search_category})

# 커뮤니티 메인
def community(request):
        # 세션에서 개체 받기
    user_id = request.session.get('user_id')    # string 타입으로 받아짐
    user = json.loads(user_id)                  # json을 통하여 파싱
    user = user[0]['fields']['nickname']
    
    boards = Board.objects.all()
    return render(request, 'board/board_community.html', {'boards': boards, 'user': user})

def community_add(request):
    return render(request, 'board/board_community_add.html', {})