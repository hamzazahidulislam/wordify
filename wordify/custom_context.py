from blog.models import Category, Post, Profile
def mycontext(request):
    profile = Profile.objects.all()
    categories = Category.objects.all()
    latest_post = Post.objects.order_by('-date')[0:3]
    userprofile = Profile.objects.all()
    return {'categories': categories, 'latest_post': latest_post, 'userprofile': userprofile, 'profile': profile}