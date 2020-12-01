from django.shortcuts import render, redirect
from .models import Articles 
from .forms import	ArticlesForm
from django.views.generic import DetailView, UpdateView, DeleteView




def news_home(request):
	news = Articles.objects.order_by('-date')[:3]
	return render(request, 'news/news_home.html', {'news': news})

#Add and Edit news
class NewsDetailView(DetailView):
	model = Articles
	template_name = 'news/details_view.html'
	context_object_name = 'article'

class NewsUpdateView(UpdateView):
	model = Articles
	template_name = 'news/add_article.html'
	form_class = ArticlesForm

class NewsDeleteView(DeleteView):
	model = Articles
	success_url = '/news/'
	template_name = 'news/news-delete.html'
	form_class = ArticlesForm







def add_article(request):
	error = ''
	if request.method == 'POST':
		form = ArticlesForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect("news_home")
		else: 
			error = "WRONG FORM!"




	form = ArticlesForm()
	data = {
		'form': form, 
		'error': error, 
	}


	return render (request, 'news/add_article.html', data)