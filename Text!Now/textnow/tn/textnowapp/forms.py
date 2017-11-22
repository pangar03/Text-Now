from django import forms	
from .models import *
from crispy_forms.helper import FormHelper
from crispy_forms import Layout, Fieldset, HTML, Field

class MsgForm(form.ModelForm):

	sender = forms.CharField(
		label ="De:",
		required = True, 
		widget = forms.TextInput(attrs={'placeholder':'Grupo'}),
	)

	group = forms.CharField(
		label ="Grupo",
		required = True, 
		widget = forms.TextInput(attrs={'placeholder':'Grupo'}),
	)

	group = forms.ImageField(
		label ="Imagen",
		required = False, 
		widget = forms.FileInput,
	)

	message = forms.CharField(
		label ="Mensaje",
		required = False, 
		widget = forms.TextInput(attrs={'placeholder':'...'}),
	)


	

	class Meta:
		model=Msg
		fields= ("sender","group","archive","message")


	def __ini__(self, *args, **kwargs):
		super(MsgForm, self).__ini__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.layout = Layout(
			Fieldset(
				HTML("<div>"),

				HTML("</div>"),
				),
			)
		
		
