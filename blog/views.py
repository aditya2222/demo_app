from django.shortcuts import *
from django.views.generic import *
from blog.models import Post
from blog.forms import PostForm
from django.utils import timezone
from django.urls import reverse_lazy
from django.contrib.auth.decorators import *
from django.contrib.auth.mixins import *
# Create your views here.

class AboutView(TemplateView):
    template_name = 'about.html'


class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')


class PostDetailView(DetailView):
    model = Post


class CreatePost(CreateView,LoginRequiredMixin):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm
    model = Post

class UpdatePostView(UpdateView,LoginRequiredMixin):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm
    model = Post


class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')


class DraftListView(ListView,LoginRequiredMixin):

    login_url = '/login/'
    redirect_field_name = 'blog/post_list.html'
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by('created_date')

@login_required
def post_publish(request,pk):
    post=get_object_or_404(Post,pk=pk)
    post.publish()
    return redirect('post_detail',pk=pk)





















