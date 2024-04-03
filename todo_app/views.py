from django.shortcuts import get_object_or_404, render
from .forms import TaskForm
from .models import Task, Post
from django.views.decorators.http import require_http_methods
from django.views.generic.list import ListView

# Create your views here.


def index(request):

    context = {
        'form': TaskForm(),
        'todos': Task.objects.all().order_by('-id'),

    }

    return render(request, 'index.html', context)


def add_form(request):

    if request.method == 'POST':

        form = TaskForm(request.POST)
        if form.is_valid():

            added_todo = form.save()
            context = {
                'added_todo': added_todo
            }

            return render(request, 'partials/added_todo.html', context)

    return render(request, 'partials/add_todo_form.html', {'form': TaskForm()})


@require_http_methods(['DELETE'])
def delete_todo(request, pk):
    todo = get_object_or_404(Task, pk=pk)
    todo.delete()

    context = {
        'todos': Task.objects.all().order_by('-id'),
        'form': TaskForm()
    }

    return render(request, 'partials/todo_list.html', context)


def edit_click(request, pk):

    task = get_object_or_404(Task, pk=pk)

    if request.method == 'GET':
        form = TaskForm()

        context = {'task': task,
                   'form': form
                   }

        return render(request, ['partials/edit_click.html', 'partials/added_todo.html'], context)

    elif request.method == 'POST':
        new_name = request.POST.get(
            task, request.POST.get('name'))

        task.name = new_name
        task.save()

        return render(request, 'partials/added_todo.html', {'added_todo': task})


class BlogListView(ListView):

    model = Post
    template_name = 'blog.html'
    context_object_name = 'posts'  # name of the object that will be used in the template
    ordering = ['-created_date']  # ordering the posts by date_posted

    def get_queryset(self):
        return Post.objects.filter(status='published').order_by('-created_date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_details_url'] = 'post_details'
        return context


def post_details(request, pk):
    if request.method == 'GET':
        post = get_object_or_404(Post, pk=pk)
        return render(request, 'partials/blog/post_details.html', {'post': post})
