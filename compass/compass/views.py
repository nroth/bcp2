from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView

from people.models import CompassUser, Person
from .forms import RegisterForm, ManageForm


def is_person(user):
    """Check to see if this user is a known Compass person"""
    if user.is_authenticated():
        return user.person is not None
    else:
        return False

def is_admin(user):
    """Check to see if user is superuser"""
    return user.is_superuser


class LoginRequiredMixin(object):

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)


class PersonRequiredMixin(object):

    # setting login_url here doesn't seem to make a whole lot of sense
    # but its purpose is to break a redirect loop for a logged in user
    # who does not yet pass the person required test
    # TODO: probably switch this to 403 instead
    @method_decorator(user_passes_test(is_person, login_url="/"))
    def dispatch(self, request, *args, **kwargs):
        return super(PersonRequiredMixin, self).dispatch(request, *args, **kwargs)


class AdminRequiredMixin(object):

    @method_decorator(user_passes_test(is_admin, login_url="/"))
    def dispatch(self, request, *args, **kwargs):
        return super(AdminRequiredMixin, self).dispatch(request, *args, **kwargs)


class MessageMixin(object):
    
    def form_valid(self, form):
        # TODO: add other kinds of messages
        if self.success_message:
            messages.success(self.request, self.success_message)
        return super(MessageMixin, self).form_valid(form)


def home(request):
    if request.user.is_authenticated():
        if request.user.person is not None:
            return render(request, 'home.html')
        else:
            return HttpResponseRedirect('/register/')
    else:
        return render(request, 'home.html')


class ManageView(AdminRequiredMixin, MessageMixin, UpdateView):

    form_class = ManageForm
    template_name="manage.html"
    success_url = "/manage/"


    def dispatch(self, request, *args, **kwargs):

        self.request = request
        self.kwargs = kwargs
        self.object = self.get_object()

        if self.object is None:
            if self.request.user.is_superuser:
                messages.warning(request, "No users need managed")
            return redirect("home")

        return super(ManageView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):

        context = {'pending_count': self.pending_count}
        context.update(kwargs)

        return super(ManageView, self).get_context_data(**context)

    def get_object(self):
        qs = CompassUser.objects.filter(person__isnull=True).filter(has_requested_person=True)
        self.pending_count = qs.count()
        if self.pending_count > 0:
            return qs[0]

    def form_valid(self, form):

        if "approve" in form.data:
            if form.cleaned_data['person']:
                form.save()
                self.success_message = "User Approved"
        if "deny" in form.data:
            pending_user = CompassUser.objects.get(pk=form.instance.pk)
            pending_user.delete()
            self.success_message = "User Denied"

        return HttpResponseRedirect(self.get_success_url())


class RegisterView(LoginRequiredMixin, MessageMixin, UpdateView):

    model = CompassUser
    form_class = RegisterForm
    template_name = "register.html"
    success_url = "/"
    success_message = "Registration received.  Please wait for admin approval."

    def get_object(self, queryset = None):
        return self.request.user

    def form_valid(self, form):
        self.request.user.has_requested_person = True
        self.request.user.save()
        return super(RegisterView, self).form_valid(form)
