from django.contrib import admin
from django.urls import path
from lycee import views
from lycee.views import StudentCreateView, StudentEditView, ParticularCallCreateView, CallRollCreateView

urlpatterns = [
    #Page d'accueil
    path('', views.accueil, name='accueil'),
    #Page Django administration
    path('admin/', admin.site.urls),
    #Page principale
    path('lycee/', views.index, name='index'),
    #Page liste des étudiants d'un cursus (selon id)
    path('lycee/<int:cursus_id>/', views.detail, name='detail'),



    path('lycee/cursuscall/view/', views.callview, name="call_view"),
    path('lycee/cursuscall/view/<int:presence_id>/', views.detail_callview, name='detail_cursuscall'),
    path('lycee/cursuscall/<int:cursus_id>/', CallRollCreateView.as_view(), name='call_roll_cursus'),
    path('lycee/call/create/', ParticularCallCreateView.as_view(), name='create_particular_call'),
    path('lycee/student/<int:student_id>/', views.view_student_detail, name='view_student_detail'),



    #Page d'édition d'un étudiant
    path('lycee/student/edit/<pk>/', StudentEditView.as_view(), name='edit_student'),
    #Page de création d'un étudiant
    path('lycee/student/create/', StudentCreateView.as_view(), name='create_student'),

]
