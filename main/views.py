from django.shortcuts import render


def index(request):
	data = {
		'title': 'Home Page',
		# 'values': ['Some', 'body', 'once', 'told', 'me'],
		# 'obj':{
		# 	'car': "BMW",
		# 	'model':"Z3",
				
		# }
	}
	return render(request, 'main/index.html', data)

def about(request):
	return render(request, 'main/about.html')

def contacts(request):
	return render(request, 'main/contacts.html')