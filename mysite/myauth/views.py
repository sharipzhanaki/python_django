from random import random

from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.contrib.auth.views import LogoutView
from django.http import HttpRequest, HttpResponse, HttpResponseForbidden
from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, DetailView, UpdateView
from django.views import View
from django.views.decorators.cache import cache_page
from django.utils.translation import gettext_lazy as _, ngettext
from django.contrib.auth.models import User

from .models import Profile
from .forms import ProfileUpdateForm


class HelloView(View):
    welcome_message = _("welcome hello word")

    def get(self, request: HttpRequest) -> HttpResponse:
        items_str = request.GET.get("items") or 0
        items = int(items_str)
        products_line = ngettext(
            "one product",
            "{count} products",
            items,
        )
        products_line = products_line.format(count=items)
        return HttpResponse(f"<h1>{self.welcome_message}</h1>"
                            f"<h2>{products_line}</h2>")


class AboutMeView(UpdateView):
    model = Profile
    fields = ("avatar", )
    template_name = "myauth/about-me.html"
    success_url = reverse_lazy("accounts:about-me")

    def get_object(self, queryset=None):
        profile, _ = Profile.objects.get_or_create(user=self.request.user)
        return profile


class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = "myauth/register.html"
    success_url = reverse_lazy("myauth:about-me")

    def form_valid(self, form):
        response = super().form_valid(form)
        Profile.objects.create(user=self.object)
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password1")
        user = authenticate(
            self.request,
            username=username,
            password=password,
        )
        login(request=self.request, user=user)
        return response


def login_view(request: HttpRequest):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect('/admin/')

        return render(request, 'myauth/login.html')

    username = request.POST["username"]
    password = request.POST["password"]

    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('/admin/')

    return render(request, 'myauth/login.html', context={"error": "Invalid login credentials"})


def logout_view(request: HttpRequest):
    logout(request)
    return redirect(reverse("myauth:login"))

class MyLogoutView(LogoutView):
    next_page = reverse_lazy("myauth:login")


class UsersListView(ListView):
    template_name = "myauth/users_list.html"
    model = User
    context_object_name = "users"


class ProfileDetailsView(DetailView):
    template_name = "myauth/profile_details.html"
    model = Profile
    context_object_name = "profile"


class ProfileUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Profile
    form_class = ProfileUpdateForm
    template_name = "myauth/profile_update.html"

    def test_func(self):
        profile = self.get_object()
        return self.request.user == profile.user or self.request.user.is_staff

    def handle_no_permission(self):
        return HttpResponseForbidden("You don't have permission to update user's profile")

    def get_success_url(self):
        return reverse_lazy("myauth:profile-details", kwargs={"pk": self.object.pk})


@user_passes_test(lambda u: u.is_superuser)
def set_cookie_view(request: HttpRequest) -> HttpResponse:
    response = HttpResponse("Cookie set")
    response.set_cookie("mycookie", "HelloCookie", max_age=3600)
    return response


@cache_page(60 * 2)
def get_cookie_view(request: HttpRequest) -> HttpResponse:
    value = request.COOKIES.get("mycookie", "Cookie not found")
    return HttpResponse(f"Cookie value: {value!r} + {random()}")


@permission_required("myauth.view_profile", raise_exception=True)
def set_session_view(request: HttpRequest) -> HttpResponse:
    request.session["mysession"] = "HelloSession"
    return HttpResponse("Session set!")


@login_required
def get_session_view(request: HttpRequest) ->HttpResponse:
    value = request.session.get("mysession", "Session not found")
    return HttpResponse(f"Session value: {value!r}")
