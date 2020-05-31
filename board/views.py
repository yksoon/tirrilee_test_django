from django.shortcuts import render,redirect
from django.contrib import sessions
from .models import Board
import json

from .forms import BoardForm
from account.models import Member

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

# 커뮤니티 글작성
def community_add(request):
    boardform = BoardForm()
    return render(request, 'board/board_community_add.html', {'boardform': boardform})

# 커뮤니티 글작성 완료
def community_add_result(request):
    boardform = BoardForm(request.POST, request.FILES)
    user_id = request.session.get('user_id')    # string 타입으로 받아짐
    user = json.loads(user_id)                  # json을 통하여 파싱
    user = user[0]['fields']['nickname']
    
    if request.method == 'POST':
        if boardform.is_valid():
            Board = boardform.save(commit=False)
            Board.category = request.POST["category"]
            Board.nickname = user
            Board.save()
            return redirect('community')
        else:
            return redirect('community')

# 마이페이지
def mypage(request):
    user_id = request.session.get('user_id')    # string 타입으로 받아짐
    user_jason = json.loads(user_id)                  # json을 통하여 파싱
    user = user_jason[0]['fields']['nickname']
    user_email = user_jason[0]['fields']['email']
    user_introduce = user_jason[0]['fields']['introduce']
    
    if request.method == 'POST':
        Member.objects.raw("UPDATE 'account_member' SET introduce='%s' WHERE email='%s'" % (request.POST['introduce'], user_email))
        return redirect('mypage')
    
    return render(request, 'board/board_mypage.html', {'user_email': user_email, 'user': user, 'user_introduce': user_introduce})

# 로그아웃
def logout(request):
    request.session.modified = True
    del request.session['user_id']
    
    return redirect('/')