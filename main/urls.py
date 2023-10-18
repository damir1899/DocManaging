from django.urls import path

from .views import (IndexView,
                    DocumentDetailView,
                    SignUpView,
                    LoginView, 
                    LogoutView,
                    AddDocumentView, 
                    DeleteDocumentView,)


urlpatterns = [
    path('', IndexView),
    path('logout/', LogoutView),
    path('add_document/', AddDocumentView),
    path('signup/', SignUpView),
    path('login/', LoginView),
    path('<slug:slug>/', DocumentDetailView),
    path('delete/<post_id>', DeleteDocumentView, name='delete'),

]
