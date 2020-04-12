from django.forms import ModelForm
from .models import Feeding,Finch,Profile

class  FinchForm(ModelForm):
	class Meta:
		model=Finch
		fields=['name','breed','description','age']

class FeedingForm(ModelForm):
	class Meta:
		model = Feeding
		fields = ['date', 'meal']
class ProfileForm(ModelForm):
	class Meta:
		model=Profile
		fields=['fav']
