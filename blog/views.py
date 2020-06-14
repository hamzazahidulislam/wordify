from django.shortcuts import render
from .models import Post, Category

def search_post(request):
    search_keyword = request.POST['search_keyword']
    if search_keyword:
        post = Post.objects.filter(title__contains=search_keyword)
        return render(request, 'search.html', {'post': post,'search_key':search_keyword})
    return render(request, 'search.html')


def detail_post(request, post_id):
    try:
        post_obj = Post.objects.get(id=post_id)
        #profie = Profile.objects.get(user=post_obj.author)
        contex = {'post': post_obj}
        return render(request, 'blog/detail_post.html', contex)
    except Exception as error:
        print(error)
        return render(request, '404.html')



def category_list(requst,id):
    category =Category.objects.filter(id=id)
    category_name =Category.objects.filter(name=id)
    post =Post.objects.all()
    contex = {'ctagorylist':category,'postlist':post,'category_name':category_name}
    return render(requst,'blog/category.html',contex)