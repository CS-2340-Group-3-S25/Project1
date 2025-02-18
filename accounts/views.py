from django.shortcuts import render, get_object_or_404
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from .forms import CustomUserCreationForm, CustomErrorList, ForgotPasswordForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import SecurityQuestionForm
from django.contrib.auth.forms import SetPasswordForm


def password_reset(request):
    if request.method == "GET":
        return render(request, "accounts/password_reset.html")

    elif request.method == "POST":
        username = request.POST.get("username")
        security_answer = request.POST.get("security_answer")
        new_password = request.POST.get("new_password")

        try:
            user = User.objects.get(username=username)
            # Check if security answer matches (case-insensitive)
            if user.profile.security_answer.lower() == security_answer.lower():
                user.set_password(new_password)
                user.save()
                return redirect("accounts.login")
            else:
                return render(request, "accounts/password_reset.html", {"error": "Invalid security answer."})
        except User.DoesNotExist:
            return render(request, "accounts/password_reset.html", {"error": "User not found."})

@login_required
def logout(request):
    auth_logout(request)
    return redirect("home.index")


def login(request):
    template_data = {}
    template_data["title"] = "Login"
    if request.method == "GET":
        return render(request, "accounts/login.html", {"template_data": template_data})
    elif request.method == "POST":

        if not User.objects.filter(username=request.POST["username"]).exists():
            return redirect("accounts.signup")

        user = authenticate(
            request,
            username=request.POST["username"],
            password=request.POST["password"],
        )

        if user is None:
            template_data["error"] = "The username or password is incorrect."
            return render(
                request, "accounts/login.html", {"template_data": template_data}
            )
        else:
            auth_login(request, user)
            return redirect("home.index")

def signup(request):
    template_data = {}
    template_data["title"] = "Sign Up"
    if request.method == "GET":
        template_data["form"] = CustomUserCreationForm()
        return render(request, "accounts/signup.html", {"template_data": template_data})
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST, error_class=CustomErrorList)
        if form.is_valid():
            user = form.save()
            # Save security question and answer
            user.profile.security_question = form.cleaned_data["security_question"]
            user.profile.security_answer = form.cleaned_data["security_answer"]
            user.profile.save()
            return redirect("accounts.login")
        else:
            template_data["form"] = form
            return render(request, "accounts/signup.html", {"template_data": template_data})

@login_required
def orders(request):
    template_data = {}
    template_data['title'] = 'Orders'
    template_data['orders'] = request.user.order_set.all()
    return render(request, 'accounts/orders.html',{'template_data': template_data})


def verify_security_question(request, username):
    user = get_object_or_404(User, username=username)

    if request.method == 'POST':
        form = SecurityQuestionForm(request.POST)
        if form.is_valid():
            security_answer = form.cleaned_data['security_answer']
            if user.profile.security_answer == security_answer:
                # Redirect to password reset form after successful verification
                return redirect('reset_password', username=user.username)
            else:
                form.add_error(None, "Incorrect answer.")
    else:
        form = SecurityQuestionForm()

    return render(request, 'accounts/verify_security_question.html', {
        'form': form,
        'security_question': user.profile.security_question
    })

def reset_password(request, username):
    user = get_object_or_404(User, username=username)

    if request.method == 'POST':
        form = SetPasswordForm(user, request.POST)
        if form.is_valid():
            form.save()
            return redirect('password_reset_success')
    else:
        form = SetPasswordForm(user)

    return render(request, 'accounts/reset_password.html', {'form': form})


def forgot_password(request):
    if request.method == 'POST':
        form = ForgotPasswordForm(request.POST)
        if form.is_valid():
            username_or_email = form.cleaned_data['username_or_email']

            # Try to find user by username or email
            user = User.objects.filter(username=username_or_email).first()
            if not user:
                user = User.objects.filter(email=username_or_email).first()

            if user:
                # Redirect to the security question verification
                return redirect('verify_security_question', username=user.username)
            else:
                form.add_error(None, "No user found with this username or email.")
    else:
        form = ForgotPasswordForm()

    return render(request, 'accounts/forgot_password.html', {'form': form})

def password_reset_success(request):
    return render(request, 'accounts/password_reset_success.html')