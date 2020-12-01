from .models import Articles	
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea

class ArticlesForm(ModelForm):
	class Meta:
		model = Articles
		fields = ['title', 'announcement', 'full_text', 'date']

		widgets = {
			"title": TextInput(attrs={
				'class': 'form-control',
				'placeholder': "Article's name",

				}),
			"announcement": TextInput(attrs={
				'class': 'form-control',
				'placeholder': "Announcement",

				}),

			"date": DateTimeInput(attrs={
				'class': 'form-control',
				'placeholder': "Date of publication",
				'type': "date",

				}),
			
			"full_text": Textarea(attrs={
				'class': 'form-control',
				'placeholder': "Article's text",


				}),
						

		}