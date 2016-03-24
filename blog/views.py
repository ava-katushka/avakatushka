from django.shortcuts import render

# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from blog.models import PostPreview, Post, Citate
from random import shuffle



def index(request):
    # return render_to_response('index.html', {'categories': Category.objects.all(), 'posts': Blog.objects.all()[:5]})
    post_previews = PostPreview.objects.all().order_by("-time_posted")
    citates = list(Citate.objects.all())
    shuffle(citates)
    return render_to_response('index.html', {'post_previews': post_previews, 'citates': citates})


def view_post(request, slug):
    citates = list(Citate.objects.all())
    shuffle(citates)
    return render_to_response('view_post.html', {'post': get_object_or_404(Post, slug=slug), 'citates': citates})
#
#
# def view_category(request, slug):
#     category = get_object_or_404(Category, slug=slug)
#     return render_to_response('view_category.html', {'category': category, 'posts': Blog.objects.filter(category=category)[:5]})




