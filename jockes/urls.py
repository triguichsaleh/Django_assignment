from django.urls import path
from .views import JockeListView, JockeCreateView, JockeDetailView, JockeUpdateView, JockeDeleteView, SignupView

urlpatterns = [
    path('', JockeListView.as_view(), name='jocke-list'),
    path('jocke/create/', JockeCreateView.as_view(), name='jocke-create'),
    path('jocke/<int:pk>/', JockeDetailView.as_view(), name='jocke-detail'),
    path('jocke/<int:pk>/update/', JockeUpdateView.as_view(), name='jocke-update'),
    path('jocke/<int:pk>/delete/', JockeDeleteView.as_view(), name='jocke-delete'),
    path('signup/', SignupView.as_view(), name='signup'),
    # Add more URLs as needed

 
]
