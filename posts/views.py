from django.views.generic import ListView
from .models import Post


class HomePageView(ListView):
    model = Post #object_list in templates
    context_object_name = 'all_posts_list'
    template_name = 'home.html'
