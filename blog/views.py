from django.shortcuts import render

# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from blog.models import PostPreview, Post



def index(request):
    # return render_to_response('index.html', {'categories': Category.objects.all(), 'posts': Blog.objects.all()[:5]})
    return render_to_response('index.html', {'post_previews': PostPreview.objects.all()})


def view_post(request, slug):
    return render_to_response('view_post.html', {'post': get_object_or_404(Post, slug=slug)})
#
#
# def view_category(request, slug):
#     category = get_object_or_404(Category, slug=slug)
#     return render_to_response('view_category.html', {'category': category, 'posts': Blog.objects.filter(category=category)[:5]})




