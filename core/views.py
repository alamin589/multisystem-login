










# # views.py
# from django.shortcuts import render, redirect
# from django.contrib import messages
# from django.contrib.auth.hashers import check_password
# from django.contrib.auth.hashers import make_password
# from django.shortcuts import render, redirect
# from django.contrib import messages
# from django.contrib.auth import authenticate, login
# from .forms import UserForm, LoginFormStep1, LoginFormStep2
# from .models import User
# def create_user(request):
#     if request.method == 'POST':
#         form = UserForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.save()
#             return redirect('login_step1')  
#     else:
#         form = UserForm()

#     return render(request, 'create_user.html', {'form': form})

# # views.py

# def login_step1(request):
#     if request.method == 'POST':
#         form = LoginFormStep1(request.POST)
#         if form.is_valid():
#             email = form.cleaned_data['email']
#             try:
#                 user = User.objects.get(email=email)
#             except User.DoesNotExist:
#                 messages.error(request, 'Email not found. Please try again.')
#                 return redirect('login_step1')

#             # Store user ID in session instead of the entire user instance
#             request.session['user_id'] = user.id

#             # Redirect to login_step2 page after successful email verification
#             return redirect('login_step2')

#     else:
#         form = LoginFormStep1()

#     return render(request, 'login_step1.html', {'form': form})
# # views.py

# from django.contrib.auth.hashers import check_password

# def login_step2(request):
#     user_id = request.session.get('user_id', None)

#     if not user_id:
#         return redirect('login_step1')

#     try:
#         user = User.objects.get(id=user_id)
#     except User.DoesNotExist:
#         # Handle the case where the user does not exist
#         return redirect('login_step1')

#     if request.method == 'POST':
#         form = LoginFormStep2(request.POST)
#         if form.is_valid():
#             password = form.cleaned_data['password']

#             # Use check_password to compare the entered password with the hashed password
#             if check_password(password, user.password):
#                 return redirect('user_dashboard')
#             else:
#                 messages.error(request, 'Incorrect password. Please try again.')

#     else:
#         form = LoginFormStep2()

#     return render(request, 'login_step2.html', {'email': user.email, 'form': form})


# def login_step2(request):
#     user_id = request.session.get('user_id', None)

#     if not user_id:
#         return redirect('login_step1')

#     try:
#         user = User.objects.get(id=user_id)
#     except User.DoesNotExist:
#         # Handle the case where the user does not exist
#         return redirect('login_step1')

#     if request.method == 'POST':
#         form = LoginFormStep2(request.POST)
#         if form.is_valid():
#             password = form.cleaned_data['password']
#             if check_password(password, user.password):
#                 return redirect('user_dashboard')
#             else:
#                 messages.error(request, 'Incorrect password. Please try again.')

#     else:
#         form = LoginFormStep2()

#     return render(request, 'login_step2.html', {'email': user.email, 'form': form})

