import jwt
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.http import Http404
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
from users.forms import *


def login_user(request):
    next = request.GET.get('next', None)
    if request.user.is_authenticated():
        return redirect('/')

    form = LoginForm(data=request.POST or None)

    context = {
        'form': form,
    }

    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)
            if user is None:
                messages.error(request, "Invalid login credentials")
                return render(request, 'users/login.html', context)
            else:
                login(request, user)
                if next:
                    return redirect(next)
                return redirect('/')

    return render(request, 'users/login.html', context)


@login_required
def logout_user(request):
    """
    Logout a user
    """
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect('home_page')


@login_required
def user_register(request):
    """
    Register a user
    """
    # if request.user.is_authenticated():
    #     return redirect('/')

    form = RegisterForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = form.save(commit=False)
            user.password = make_password(form.cleaned_data.get('confirm_password'))
            messages.success(request, "We have sent you confirmation email \
                Please confirm your account by clicking on the confirmation link \
                sent to your email.")
            user.save()
            login(request, user)
            return redirect('/')

    context = {
        'form': form
    }
    return render(request, 'users/register.html', context)


def user_send_password_reset_email(request):
    """
    Send password reset email
    """
    if request.user.is_authenticated():
        return redirect('/')

    form = SendPasswordResetEmailForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, "Password reset email sent. Please check your email for instructions.")
            return redirect('send_password_reset_email')

    context = {
        'form': form
    }
    return render(request, 'users/send_password_reset_email.html', context)


def user_password_reset(request):
    """
    Reset user password
    """
    if request.user.is_authenticated():
        return redirect('/')

    token = request.GET.get('token')
    if token is None:
        raise Http404()

    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithm='HS256')
    except jwt.ExpiredSignature:
        messages.error(request, 'Reset token has expired.')
        return redirect('users:send_password_reset_email')
    except jwt.DecodeError:
        messages.error(request, 'Error decoding reset token.')
        return redirect('users:send_password_reset_email')
    except jwt.InvalidTokenError:
        messages.error(request, 'Invalid reset token.')
        return redirect('users:send_password_reset_email')

    try:
        user = User.objects.get(pk=payload['reset'])
    except User.DoesNotExist:
        messages.error(request, 'Invalid token.')
        return redirect('users:send_password_reset_email')

    form = PasswordResetForm(data=request.POST or None, user=user)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, "Password reset successfully.")
            return redirect('users:login_user')

    context = {
        'form': form
    }
    return render(request, 'users/password_reset.html', context)


@login_required
def user_password_change(request):
    """
    change user password
    """

    form = PasswordChangeForm(data=request.POST or None, user=request.user)
    if request.method == 'POST':
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Password Changed successfully')
            login(request, user)

    context = {
        'form': form
    }

    return render(request, 'users/change_password.html', context)


@login_required
def user_profile_edit(request):
    form = ProfileForm(instance=request.user, data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, "profile update.")
            return redirect('profile_edit')

    context = {
        'form': form
    }

    return render(request, 'users/profile_edit.html', context)
