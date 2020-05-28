from django.shortcuts import render,redirect
from .models import Board


# Create your views here.

def main(request):
    return render(request, 'board/board_list.html', {})