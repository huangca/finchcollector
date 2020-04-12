from django.shortcuts import render,redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from  .models import *
from  .forms  import *
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
# Add the following import
from django.http import HttpResponse

# Define the home view
def home(request):
	return render(request,'index.html')

def about(request):
	return render(request,'about.html')
@login_required
def  finches_index(request):
	#finches=Finch.objects.all()
	finches=Finch.objects.filter(user=request.user)
	return render(request,'finches/finches_index.html',{'finches':finches})
@login_required
def finches_detail(request,finch_id):
	finch=Finch.objects.get(id=finch_id)
	toys_finch_doesnt_have = Toy.objects.exclude(id__in = finch.toys.all().values_list('id'))
	feeding_form=FeedingForm()
	return render(request,'finches/finches_detail.html',{'finch':finch,'feeding_form':feeding_form,'toys':toys_finch_doesnt_have})
@login_required
def add_feeding(request,finch_id):
	form=FeedingForm(request.POST)
	if form.is_valid():
		new_feeding=form.save(commit=False)
		new_feeding.finch_id=finch_id
		new_feeding.save()
	return redirect('detail',finch_id=finch_id)
@login_required
def  new_finch(request):
	if request.method=='POST':
		form=FinchForm(request.POST)
		if form.is_valid():
			finch=form.save(commit=False)
			finch.user=request.user
			finch.save()
			return redirect('detail',finch.id)
	else:
		form=FinchForm()
	context = { 'form': form }
	return render(request,'finches/finches_form.html',context)
@login_required
def finches_update(request,finch_id):
	finch=Finch.objects.get(id=finch_id)
  #if  request is a  POST
	if(request.method=="POST"):
		form=FinchForm(request.POST,instance=finch)
		if form.is_valid():
			finch=form.save()
			return  redirect('detail',finch.id)
	else: #if  not  a POST, create  the form
  		form=FinchForm(instance=finch)
	return  render(request,'finches/finches_form.html',{'form':form})
@login_required
def  finches_delete(request,finch_id):
	Finch.objects.get(id=finch_id).delete()
	return redirect('finches_index')
@login_required
def  assoc_toy(request,finch_id,toy_id):
  #get the cat  from our database using the ID and add a  toy to that cat using  the toy_id
	Finch.objects.get(id=finch_id).toys.add(toy_id)
	return  redirect('detail',finch_id=finch_id)

def signup(request):
	error_message=''
	if request.method=='POST':
		form=UserCreationForm(request.POST)
		profile_form=ProfileForm(request.POST)
		if form.is_valid() and profile_form.is_valid():
			user=form.save()
			profile=profile_form.save(commit=False)
			profile.user=user
			profile.save()
			login(request,user)
			return redirect('finches_index')
		else:
			error_message='Invalid sign up'
	form=UserCreationForm()
	profile_form=ProfileForm()
	context={'form':form,'p_form':profile_form,'error_message':error_message}
	return  render(request,'registration/signup.html',context)


#hard code temp data
# class Finch:
# 	def   __init__(self,name,breed,description,age):
# 		self.name=name
# 		self.breed=breed
# 		self.description=description
# 		self.age=age

# finches=[
# 	Finch('Test finch 1','test breed 1','test description 1',3),
# 	Finch('Test finch 2','test breed 1','test description 2',2),
# 	Finch('Test finch 3','test breed 2','test description 3',1)

# ]

class ToyList(LoginRequiredMixin,ListView):
  # This line associates the ListView with the Toy model
  model = Toy

class ToyDetail(LoginRequiredMixin,DetailView):
  model = Toy

# The editable view types include Create, Update, and Delete
# They're also relatively easy to set up but require a little more work
class ToyCreate(LoginRequiredMixin,CreateView):
  model = Toy
  # The CreateView requires a field property to set
  # Here we are saying that all fields associated with a Toy should 
  # be displayed in the form
  fields = '__all__'
  # This CBV will render the template toy_form.html  

class ToyUpdate(LoginRequiredMixin,UpdateView):
  model = Toy
  # In the UpdateView we set the name and description fields as the only two in the form
  fields = ['name', 'description']
  # This CBV will render the template toy_form.html as well


class ToyDelete(LoginRequiredMixin,DeleteView):
  model = Toy
  # The DeleteView requires a success_url be declared to redirect 
  # the user to when they successfully delete a toy
  success_url = '/toys/'
  # This CBV will render the toy_confirm_delete.html template 

