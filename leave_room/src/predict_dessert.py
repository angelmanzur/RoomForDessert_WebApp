import os
import gc

categories=['Cake','Cookies','Pie','Pudding']

def render_html(ingr_list):
	
	y_prob = predict(ingr_list)
	
	dessert_cat = np.where(y_prob[0]==y_prob[0].max())
	dessert = categories[dessert_cat[0][0]]
	
	print('desert list =', dessert)
	html_file = "predict_dessert.html"

	# print('created file ', html_path)
	# file1 = open(html_path,"w")

	# line ="""<head>
	# 			{% extends "base.html" %}
	# 			{% load static %}
	# 			{% block page_content %} 
	# 			<title>Predicting dessert</title>
	# 		 </head>
	# 		 <html>
	# 		 <body>

	# 		   <nav class="white" role="navigation">
    #             <div class="nav-wrapper container" >
                
    #             <a style='color:black' href="../"  class="previous" >Home</a>
    #             <ul class="right">
    #                 <li><a style='color:black' href="https://github.com/angelmanzur/Room_for_dessert">Github</a></li>
    #             </ul>
    #             </div>
    #         </nav>			
	# 		 """
	# file1.writelines(line)

	# line = """ <div id='index-banner'>
	# 	<div>
	# 		<div class='container'> """
	# file1.writelines(line)

	# if dessert == 'Cake' or dessert =='Pie':
	# 	L = "<h2> You should try to make a {0}! </h2>\n".format(dessert)
	# else:
	# 	L = "<h2> You should try to make {0}! </h2>\n".format(dessert)
	# file1.writelines(L)
	
	# line = """<p style="font-size:140%;">This decision was made after learning on +85,000 dessert recipes. 
	# The recipes have an average of 13 ingredients, but some may have more than 40 
	# ingredients (think wedding cakes). The table below shows the probabilties for each dessert predicted.</p>"""
	# file1.writelines(line)

	# line = " </div></div>"
	# # file1.writelines(line)
	# line = """ <div class="container">   
	# 	</div>
    # 	<div class="container">
    #   		<div class="section">
    #   		</div>
    # 	</div>   
  	# 	</div> """
	# file1.writelines(line)
	# line = """
    # 	<div class='section white'>
    # 	<div class="row"> 
    #        <div class="col s4 offset-s4">
    #     """
	# file1.writelines(line)	

	# line = """
    #     	<table class="highlight"> 
    #     		<thead>
    #     			<tr>
    #     				<th> Dessert type </th>
    #     				<th> Probability </th>
    #     			</tr>
    #     		</thead>
    #     		<tbody>
    #     """
	# file1.writelines(line)
	# for item, val in enumerate(categories):
	# 	file1.writelines('<tr><td>'+val + '</td>\n')
	# 	file1.writelines('<td>{:1.1f}%</td></tr>\n'.format(y_prob[0][item]*100))
		
	# file1.writelines('</tbody> </table> </div>\n')
	# file1.writelines('</div>')

	# line = "</div></div>"
	# file1.writelines(line)
	# line = """</body>
    # 	</html>
    # 	"""
	# file1.writelines(line)
	# line = "{% endblock %}"
	# file1.writelines(line)
	# file1.close()

	# print(predict_dessert_type())
	return html_file, dessert, categories, y_prob[0]



import numpy as np
# import tensorflow as tf
import datetime
from django.conf import settings 
from os import environ
word_index = settings.WORD_INDEX
graph = settings.GRAPH
lstm_model=settings.LSTM_MODEL
def predict(ingredients):
	ingredients = ingredients.replace(',', ' ')

	ingredients = ingredients.split(' ')
	#import word index from pickle file

	# pickle_file = '../../Room_for_dessert/models/word_index.pkl'
	# word_index = pickle.load(open(pickle_file, 'rb'))

	sequence = []
	for word in ingredients:
		try:
			sequence.append(word_index[word.lower().strip()])
			print(word)
		except:
			pass
	# print(sequence, ' - the sequence')
	del ingredients

	x_data = np.zeros(100)
	seq_len = len(sequence)+1
	for item in range(-1,-seq_len,-1):
		x_data[item] = int(sequence[item])

	del sequence, seq_len

	hold_data = np.empty([1,100])
	hold_data[0] = x_data

	del x_data
	
	# print('got the data {}'.format(datetime.datetime.now()))
 	# model_file = '../../Room_for_dessert/models/rnn_w2vec_model.pkl'
	# lmodel = pickle.load(open(model_file,'rb'))
	# print('loaded time {}'.format(datetime.datetime.now()))
	# y_pred = lmodel.predict(hold_data)
	# print('end time {}'.format(datetime.datetime.now()))
	# print('hold data', hold_data[0])
	# global GRAPH
	# Keras==2.2.4
	gc.collect()

	with graph.as_default():
	
		# lstm_model2 = graph.get_tensor_by_name('LSTM_MODEL')
		# print('starting time {}'.format(datetime.datetime.now()))
		# kback = environ.keys #os.environ['KERAS_BACKEND']
		# print(kback)
		# print(hold_data)
		# print(lstm_model)
		# print(lstm_model.layers[0].input)
		y_pred = lstm_model.predict(hold_data)
		lstm_model.summary()
	# 	y_pred = np.array([1,3,4,1])
		# print('end time {}'.format(datetime.datetime.now()))
		

	
	# categories=['Cake','Cookies','Pie','Pudding']
	
	return  y_pred