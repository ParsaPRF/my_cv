from django.urls import path
from website import views

app_name = 'website'

urlpatterns = [
    path('', views.index_view, name='index'),
    path('contact/', views.contact_view, name='contact'),
    path('newsletter/', views.newsletter_view, name='newsletter'),
    path('download-cv/', views.download_cv, name='download_cv'),
]
