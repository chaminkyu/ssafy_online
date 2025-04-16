from django.shortcuts import render, redirect

# Create your views here.

# articles -> model form
# accounts -> built-in form

from django.contrib.auth.forms import AuthenticationForm
# (
#     AuthenticationForm, # 로그인을 위한 폼
#     UserCreationForm, # 회원가입
#     PasswordChangeForm, # 비밀번호 변경
# )

from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

# from .models import User

def login(request):
    # 아이디와 패스워드 입력하고 로그인 버튼(submit) 눌렀을 때
    if request.method == 'POST':
        # request.POST : 아이디, 비밀번호
        # request : user <--- AuthenticaionMiddleware에서 왔음
        form = AuthenticationForm(request, request.POST)
        # 유효성 검사
        if form.is_valid():
            # get_user() : 인증된 사용자 객체
            # signup(회원가입)과 차이 ---> 이미 DB에 존재하는 사용자를 인증
            auth_login(request, form.get_user())
            return redirect('articles:index')
        
   #---------------------------------------------------

    # 로그인 버튼 누르기 전    
    else:
        form = AuthenticationForm() # 빈 폼
    
    # GET 요청 or 유효성 검사 실패
    context = {
        'form' : form, # 빈 폼
    }

    return render(request, 'accounts/login.html', context)

def logout(request):
    auth_logout(request)
    return redirect('articles:index')