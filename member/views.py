from django.shortcuts import render
from .models import Post

# Create your views here.
def hello_view(request):
    return render(request, 'hello_django.html', {'data': "hello django"})


def member(request):
    member_data = Post.objects.all()
    return render(request, 'member.html', {'member_data': member_data})
