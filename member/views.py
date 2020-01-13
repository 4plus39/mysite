from django.shortcuts import render
from .models import Post
from .form import PostForm


# Create your views here.
def hello_view(request):
    # Without use form
    # obj = Post.objects.create(name=request.POST['name'])
    # obj.save()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()

    member_data = Post.objects.all()
    return render(request, 'hello_django.html', {'member_data': member_data})


def member(request):
    member_data = Post.objects.all()
    return render(request, 'member.html', {'member_data': member_data})
