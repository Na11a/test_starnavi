from django.shortcuts import render,redirect
from post.models import Post,Like
from .forms import PostForm
from django.views.generic import ListView, DetailView,CreateView, UpdateView,DeleteView,View
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils import timezone


class HomeListView(ListView):
    model = Post
    template_name = 'post/home.html'
    context_object_name = 'posts'




class PostCreateView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login_page')
    model = Post
    template_name = 'post/edit_page.html'
    form_class = PostForm
    success_url = reverse_lazy('edit_page')
    success_msg = 'Запись создана'
    def get_context_data(self,**kwargs):
        kwargs['list_posts'] = Post.objects.all()
        return super().get_context_data(**kwargs)
    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)
        


class PostUpdateView(LoginRequiredMixin,UpdateView):
    model = Post
    template_name = 'post/edit_page.html'
    form_class = PostForm
    success_url = reverse_lazy('edit_page')
    success_msg = 'Запись успешно обновлена'
    def get_context_data(self,**kwargs):
        kwargs['update'] = True
        return super().get_context_data(**kwargs)
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if self.request.user != kwargs['instance'].author:
            return self.handle_no_permission()
        return kwargs

class PostDeleteView(LoginRequiredMixin,DeleteView):
    model = Post
    template_name = 'post/delete_page.html'
    success_url = reverse_lazy('edit_page')
    success_msg = 'Запись удалена'
    
    def post(self,request,*args,**kwargs):
        messages.success(self.request, self.success_msg)
        return super().post(request)
    def delete(self, request, *args, **kwargs):
        
        self.object = self.get_object()
        if self.object.author != self.request.user:
            return self.handle_no_permission()
        success_url = self.get_success_url()
        self.object.delete()
        return HttpResponseRedirect(success_url)

@login_required
def like_unlike_post(request):
    user = request.user
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        post_obj = Post.objects.get(id=post_id)
        profile = User.objects.get(username=user)

        if profile in post_obj.liked.all():
            post_obj.liked.remove(profile)
        else:
            post_obj.liked.add(profile)

        like, created = Like.objects.get_or_create(user=profile, post_id=post_id)

        if not created:
            if like.value =='Like':
                like.value ='Unlike'

            else:
                like.value='Like'
        else:
            like.value='Like'
        
        like.updated = timezone.now()
        post_obj.save()
        like.save()
    return redirect('home')
