from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, JockeForm
from django.views.generic import CreateView
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import UpdateView
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views import View
from django.contrib.auth.models import User
from django.views.generic import DeleteView
from django.urls import reverse_lazy
from .models import Jocke


def register_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Optionally, log in the user after registration
            # Example: login(request, user)
            return redirect('home')  # Redirect to home page or any other page
    else:
        form = UserRegistrationForm()

    return render(request, 'register.html', {'form': form})

def create_jocke(request):
    if request.method == 'POST':
        form = JockeForm(request.POST)
        if form.is_valid():
            jocke = form.save(commit=False)
            jocke.user = request.user  # Assign current user to the joke
            jocke.save()
            return redirect('jocke-detail', pk=jocke.pk)  # Redirect to joke detail page or any other page
    else:
        form = JockeForm()

    return render(request, 'create_jocke.html', {'form': form})



class JockeListView(ListView):
    model = Jocke
    template_name = 'jocke_list.html'  # Replace with your template name
    context_object_name = 'jockes'  # Optional: Rename the context variable (default is object_list)
    queryset = Jocke.objects.all()  # Optional: Override the queryset

    # Optionally, you can add more methods or override methods as needed


class JockeCreateView(CreateView):
    model = Jocke
    template_name = 'jocke_form.html'  # Replace with your template name
    fields = ['question', 'answer']  # Specify the fields to include in the form

    def form_valid(self, form):
        # Optionally, manipulate form data before saving
        return super().form_valid(form)



class JockeDetailView(DetailView):
    model = Jocke
    template_name = 'jocke_detail.html'  # Replace with your template name
    context_object_name = 'jocke'  # Optional: Rename the context variable (default is object)



class JockeUpdateView(UpdateView):
    model = Jocke
    template_name = 'jocke_form.html'  # Replace with your template name
    fields = ['question', 'answer']  # Specify the fields to include in the form

    def form_valid(self, form):
        # Optionally, manipulate form data before saving
        return super().form_valid(form)


class JockeDeleteView(DeleteView):
    model = Jocke
    template_name = 'jocke_confirm_delete.html'  # Replace with your template name
    success_url = reverse_lazy('jocke-list')  # URL to redirect after successful deletion



class SignupView(View):
    form_class = UserCreationForm
    template_name = 'signup.html'  # Replace with your template name

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login page after successful registration
        return render(request, self.template_name, {'form': form})
