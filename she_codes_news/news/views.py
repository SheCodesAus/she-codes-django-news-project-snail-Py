from tokenize import String
from django.test import tag
from django.views import generic
from django.urls import reverse_lazy
from .models import NewsStory, Tag
from .forms import StoryForm

class IndexView(generic.ListView):
    template_name = 'news/index.html'

    def get_queryset(self):
        '''Return all news stories.'''
        return NewsStory.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_stories'] = NewsStory.objects.all().order_by('-pub_date')[:3]
        context['all_stories'] = NewsStory.objects.all().order_by('-pub_date')
        context['all_tags'] = Tag.objects.all().order_by('slug')

        return context

class StoryView(generic.DetailView):
    model = NewsStory
    template_name = 'news/story.html'
    context_object_name = 'story'

class AddStoryView(generic.CreateView):
     form_class = StoryForm
     context_object_name = 'storyForm'
     template_name = 'news/createStory.html'
     success_url = reverse_lazy('news:index')

     def form_valid(self, form):
         form.instance.author = self.request.user
         return super().form_valid(form)

class EditStoryView(generic.UpdateView):
    model = NewsStory
    form_class = StoryForm
    context_object_name = 'storyForm'
    template_name = 'news/editStory.html'
    success_url = reverse_lazy('news:index')


class DeleteStoryView(generic.DeleteView):
    model = NewsStory
    template_name = 'news/deleteStory.html'
    success_url = reverse_lazy('news:index')


class TagView(generic.DetailView):
    # template_name = 'news/category.html'
    model = Tag




 
# class CategoryView(generic.ListView):
#     template_name = 'news/category.html'   

    # def get_queryset(self):
    #     '''Return all news stories.'''
    #     return NewsStory.objects.all()


    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['all_stories'] = NewsStory.objects.filter(tag__iexact=self.kwargs['tag'])
    #     return context