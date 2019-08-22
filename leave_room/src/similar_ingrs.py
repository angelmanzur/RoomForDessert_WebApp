
import os
from django.core.files.storage import default_storage
# import cloudstorage as gcs
# import webapp2

# from google.appengine.api import app_identity
#from pattern.text.en import singularize
def render_html(single_ingredient):
    ingred = single_ingredient
    # message, ings_list = find_similar_words(singularize(single_ingredient))
    message, ings_list, figname = find_similar_words(single_ingredient)
    html_file = "similar_ings.html"
#     html_path = "templates/{}".format(html_file)

#     file = default_storage.open(html_path,'w')
#     # file.write('booya hacka')
#     # line = """ \n testing  
#         # lines \n but will it overwrite? """
#     # file.write(line)
#     # file.close()

#     # url = default_storage.url(html_path)

    
#     # html_path = "hello_world/templates/{}".format(html_file)
#     # html_path = "templates/{}".format(html_file)
#     # file1 = open('tmp/saved.html',"w")
#     # file1.writelines('kjdkjdkjf')
#     # file1.close()

#     line ="""<head>
# 				{% extends "base.html" %}
# 				{% load static %}
# 				{% block page_content %} 
#                 <title>Similar ingredients</title>

# 			 </head>
# 			 <html>
# 			 <body>

#             <nav class="white" role="navigation">
#                 <div class="nav-wrapper container" >
                
#                 <a style='color:black' href="../"  class="previous" >Home</a>
#                 <ul class="right">
#                     <li><a style='color:black' href="https://github.com/angelmanzur/Room_for_dessert">Github</a></li>
#                 </ul>
#                 </div>
#             </nav>
# 			 """
#     file.write(line)

#     line = """ <div id='index-banner'>
#                 <div> 
#                     <div class='container'>"""
#     file.write(line)     

#     L = "<h1 style='color:#3d0e06;'> Matching ingredients for <strong>{0}</strong> </h1> \n".format(single_ingredient)
#     file.write(L) 
    
#     line = """<p style="font-size:140%;">The table below shows the  'closest' ingrdients, defined by the similarity score. 
#     The plot shows a 2D representation of such ingredients. In the model each ingredient is represented by a 50 dimension vector.
#     </p>"""
#     file.write(line)

#     line = """ </div> </div> """
#     file.write(line)
#     file.write("<br>"+ message)

#     line = """
# <div class="container">   
# </div>
#     <div class="container">
#       <div class="section">
#       </div>
#     </div>   
#   </div> 
  
    
#     """
#     file.write(line)
#     line = """
#     <div class='section white'>
#     	<div class="row"> 
#             <div class="col s3"> <!-- list -->
#         """
#     file.write(line)

#     if len(ings_list)>0:

#         line = """
#         	<table class="highlight"> 
#         		<thead>
#         			<tr>
#         				<th> Ingredient </th>
#         				<th> Similarity Score </th>
#         			</tr>
#         		</thead>
#         		<tbody>
#         """
#         file.write(line)
    
#     for similar_ing in ings_list:
#     	file.write('<tr><td>'+similar_ing[0] + '</td>\n')
#     	file.write('<td>{0:1.2f}</td> </tr>\n'.format(similar_ing[1]))
#     file.write('</tbody> </table> </div>\n')
#     ###########
#     ## plot the graph
 


#     line = """<div class="col s9"> <!-- figure --> 
#     		<img src="{% static """ +  '"similar_to_{}.png"'.format(ingred) + """ %}"
#     alt="2-D plot showing similar ingredients">
#     </div>"""
#     # file1.writelines(line)
#     line = """ </div>
#         </div>
#     """
#     file.write(line)
#     line = """</body>
#     	</html>
#     	"""
#     file.write(line)
#     line="{% endblock %}"
#     file.write(line)
#     file.close() 
    
    return html_file, ings_list, figname

import pickle
import numpy as np
from sklearn.manifold import TSNE

import matplotlib.pyplot as plt
import os
from os import path
from django.conf import settings 
import io
from google.cloud import storage
w2v_model=settings.W2V_MODEL
def find_similar_words(word):
    # filename = '../../Room_for_dessert/models/w2vec_model.pkl'
 
    try:
        similar = w2v_model.wv.most_similar(positive=word, topn=10)
  
        # return  ' ', similar
        vector = w2v_model.wv.__getitem__('butter')
        vec_size = len(vector)
        arrays = np.empty((0,vec_size), dtype='f')
 
        word_labels = [word]
        color_list = ['blue']
        arrays = np.append(arrays, w2v_model.wv.__getitem__([word]),axis=0)
        
       
        #     ####### get the closest words and make then blue
        # #get a list of the most similar words
        close_words = w2v_model.wv.most_similar([word],topn=10)
        for word_score in close_words:
                # for each word get the vector  
            word_vector = w2v_model.wv.__getitem__([word_score[0]])
                # get the name
            word_labels.append(word_score[0])
            color_list.append('black')
            arrays = np.append(arrays, word_vector, axis=0)
        
        
        tsne_model = TSNE(n_components=2, random_state=0,n_iter=500)
        tsne_data = tsne_model.fit_transform(arrays)


        del tsne_model, arrays

        # print('creating figure')
        fig, _ = plt.subplots()
        fig.set_size_inches(8,6)

        tsne_data_x = []
        tsne_data_y = []
        for i in range(len(tsne_data)):
            tsne_data_x.append(tsne_data[i][0])     
            tsne_data_y.append(tsne_data[i][1])     
    
        print('got the tsne data')
        plt.scatter(tsne_data_x, tsne_data_y, marker='o',s=100, c=color_list)
        for line in range(len(tsne_data)):
            plt.text(tsne_data_x[line],tsne_data_y[line],
                    '  '+word_labels[line],
                    horizontalalignment='left',
                    verticalalignment='bottom',size='large',
                    color=color_list[line],weight='normal').set_size(16)

        plt.xlabel('')
        plt.ylabel('')

        plt.xticks(fontsize=14)
        plt.yticks(fontsize=14)

        plt.title('Food pairing for {}'.format(word.title()), fontsize=24)
        print('try to save the data')
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        client = storage.Client(project='leaveroomfordessert')
        bucket = client.bucket('<BUCKET_NAME>')
        figname = 'similar_to_{}.png'.format(word)
        figname = 'similar_to_map.png'
        blob = bucket.blob('static/{}'.format(figname))
        plt.savefig(buf, format='png')

        blob.upload_from_string(
            buf.getvalue(), 
            content_type='image/png'
        )
        buf.close()

        print('save the figure ')
        # del tsne_data, tsne_data_x, tsne_data_y, fig
        # del word_labels, color_list, vec_size
        print('end')
        return '', similar, figname


    except:
        return 'Word not in vocabulary',[]

    # else:
    	# return 'no file',[]

    return 'found model',[]