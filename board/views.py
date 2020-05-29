from django.shortcuts import render,redirect
from .models import Board
import json


# Create your views here.

def main(request):
    user_id = request.session.get('user_id')    # string 타입으로 받아짐
    user = json.loads(user_id)                  # json을 통하여 파싱
    user = user[0]['fields']['email']
    return render(request, 'board/board_list.html', {'user':user})