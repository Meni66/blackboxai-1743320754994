from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.views.generic import CreateView
from .models import CollectionPoint, CollectionRequest

def home(request):
    return render(request, 'ewaste_app/home.html')

class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'ewaste_app/register.html'
    success_url = '/'

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response

@login_required
def collection_points(request):
    points = CollectionPoint.objects.all()
    return render(request, 'ewaste_app/collection_points.html', 
                {'points': points})

@login_required
def request_collection(request):
    if request.method == 'POST':
        # Process form submission
        return redirect('my_requests')
    points = CollectionPoint.objects.all()
    return render(request, 'ewaste_app/request_collection.html',
                {'points': points})

@login_required
def my_requests(request):
    requests = CollectionRequest.objects.filter(user=request.user)
    return render(request, 'ewaste_app/my_requests.html',
                {'requests': requests})
