from django.urls import path, include
from django.conf import settings
from . import views
from django.conf.urls.static import static
 
urlpatterns = [
        path('', views.index, name ='index'),
        path('about', views.about, name="about"),
        path('user/<str:username>/', views.user_profile_with_progress, name='user_profile'),
        path('course/<str:courseid>',views.course, name="course"),
        path('courses', views.course_list, name="courses")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)