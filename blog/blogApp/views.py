from django.shortcuts import render

posts=[
    {
        'author': 'sanika a',
        'title': 'blog post 1',
        'content': 'first post content',
        'date_posted': 'jan 19, 2023'
    },
     {
        'author': 'mudesh a',
        'title': 'blog post 2',
        'content': 'second post content',
        'date_posted': 'jan 20, 2023'
    },
]
# Create your views here.

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blogApp/home.html', context)

def about(request):
    return render(request, 'blogApp/about.html', {'title': 'About'})