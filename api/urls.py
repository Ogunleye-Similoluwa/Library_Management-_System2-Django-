from django.urls import path, include
from rest_framework.routers import SimpleRouter

from api.views import *

router = SimpleRouter()
router.register('all_author', viewset=All_Author)

urlpatterns = [

    path('all2/', book_list),
    path('create_book/', book_list),

    path('all/', BookListView.as_view()),
    path('create_book2/', BookCreateView.as_view()),

    # path('get_book/<int:pk>')
    path('all/get_book/<int:pk>', GetBook.as_view()),
    path('all/delete_book/<int:pk>', DeleteBook.as_view()),
    path('all/update_book/<int:pk>', Update_Book.as_view()),

    # path('author/<int:pk>', All_Author),

    path('', include(router.urls))

]
