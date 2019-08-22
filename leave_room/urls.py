from django.urls import path
from leave_room import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static


app_name = 'leave_room'
urlpatterns = [
	path('',views.leave_room, name='leave_room'),
	path('ingredient/', views.ptest, name='ptest'),
	path('ingr_list/',  views.predict_dessert, name='predict_dessert')
	#path('ingredient/?ingredient=<uuid:pk>', views.ptest, name='ptest_pk')
	] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


