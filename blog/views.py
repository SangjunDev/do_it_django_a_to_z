from django.views.generic import ListView, DetailView
from .models import Post

# Create your views here.

class PostList(ListView):
  model = Post
  
class PostDetail(DetailView):
  model = Post
  