from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import  leave_room.src.similar_ingrs as similar
import  leave_room.src.predict_dessert as predict
from django.template import loader
def ptest(request):



	if request.method =='GET':

		ingredient = request.GET['ingredient']
		render_file, ings_list, figname = similar.render_html(ingredient.lower().strip())
						
		similar_list = []
		for ingredient_list in ings_list:
			similar_list.append( (ingredient_list[0], '{:1.2f}'.format(ingredient_list[1])))
		
		return render(request, render_file, {'ingredient':ingredient, 
											'ings_list':similar_list,
											'figname':figname})
	else:
		return render(request, 'ptest.html',{'ingredient':ingredient, 'ings_list':ings_list})

# def ptest_pk(request, pk):
	# ingredient = request.GET['ingredient']
	# return render(request, 'ptest.pyf',{'ingredient':pk})

def hello_world(request):
	if request.method =='POST':
		ingredient = request.POST['ingredient']

		
		return render(request, 'index.html', {'ingredient':ingredient})
	else: 
		return render(request, 'index.html',{})

def leave_room(request):
	if request.method =='POST':
		ingredient = request.POST['ingredient']

		
		return render(request, 'index.html', {'ingredient':ingredient})
	else: 
		return render(request, 'index.html',{})

def predict_dessert(request):
	if request.method =='GET':

		ingr_list = request.GET['ingr_list']
		render_file,dessert, categories, probs = predict.render_html(ingr_list)
		

		predicted_results = []
		for i, cat in enumerate(categories):
			predicted_results.append( (cat,'{:1.1f}%'.format(probs[i]*100) ))
		
		return render(request, render_file, {'ingr_list':ingr_list,
												'dessert':dessert, 
												'results':predicted_results})
	else:
		return render(request, 'ptest.html', {})


