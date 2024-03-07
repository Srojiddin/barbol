# from django.views.generic import CreateView, UpdateView
# from django.urls import reverse_lazy
# from django.contrib.auth import get_user_model
# from apps.users.forms import UserFrom, UserUpdateForm
# from django.shortcuts import render, redirect
# from django.views import View
#
#
# User = get_user_model()
#
#
# class SignUpView(CreateView):
#     model = User
#     form_class = UserFrom
#     success_url = reverse_lazy('login')
#     template_name = 'auth/signup.html'
#
#
# def login_logics(request):
#     return render(request, 'auth/login.html', locals())
#
#
# class UserSignUpView(View):
#     def post(self, request):
#         form = UserFrom(request.POST)
#         if form.is_valid():
#             form.save()
#             print("udachno")
#         return redirect('login')
#
#     def get(self, request):
#         form = UserFrom()
#         return render(request, 'auth/signup.html', {"form":form})
