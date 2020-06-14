from django.shortcuts import render
from blog.models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
def home(request):
    post = Post.objects.order_by('-date')
    paginator = Paginator(post, 1)
    page = request.GET.get('page')
    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        items = paginator.page(1)
    except EmptyPage:
        items = paginator.page(paginator.num_pages)
    index = items.number - 1
    max_index = len(paginator.page_range)
    start_index = index - 5 if index >= 5 else 0
    end_index = index + 5 if index <= max_index - 5 else max_index
    page_range = paginator.page_range[start_index:end_index]

    total_articale = paginator.get_page(page)
    contex = {'post': total_articale, 'items': items, 'page_range': page_range}
    return render(request, 'home.html', contex)
