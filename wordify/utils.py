from django.utils.text import slugify

# def unique_slug_generator_(model_instance,title,slug_field):
#     slug =slug_field(title)
#     model_class = model_instance.__class__
#
#     while model_class._default_manager.filter(slug=slug).exists():
