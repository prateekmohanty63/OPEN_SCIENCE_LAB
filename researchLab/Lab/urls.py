from unicodedata import name
from . import views
from django.urls import path

urlpatterns=[
    path('',views.index,name='index'),
    path('people/',views.people,name='people'),
    path('research/',views.research,name='instrumentation'),
    path('publication/',views.publication,name='publication'),
    path('gallery/',views.gallery,name='gallery'),
    path('news/',views.news,name='news'),
    path('teaching/',views.teaching,name='teaching'),
    path('contact/',views.contact,name='contact'),
    path('registration/',views.registration,name='registration'),
    path('login/',views.login,name='login'),
    # path('expirement/',views.expirement,name='expirement'),
    path('work/',views.work,name="work"),
    path('useLab/',views.useLab,name='use'),
    path('demo/',views.demo,name='demo'),
    path('logout/',views.logout,name="logout"),
    path('dequeue/',views.dequeue,name='dequeue'),

    # peak from the queue
    path('peak/',views.peak,name='peak'),


     # refined pages
     path('work1/',views.work1,name='work1'),
     path('use1/',views.use1,name="use1"),
     path('research1/',views.research1,name='instrumentation1'),
     path('expirement1/',views.expirement1,name="expirement1"),


     # beakerTest
     path('beaker/',views.beakerTest,name='beakerTest')
  
]