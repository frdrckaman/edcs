from django.urls import path
from edcs_vac083.views import edcs_vac083_home, edcs_vac083_visits, PublisherList, PublisherDetail, BookList,\
                              AcmeBookList, PublisherBookList, AuthorDetailView, edcs_vac083_jquery
from django.contrib import admin


app_name = 'edcs_vac083'

urlpatterns = [
    path('edcs_vac083_home/', edcs_vac083_home, name='edcs_vac083_home'),
    path('edcs_vac083_visits/', edcs_vac083_visits, name='edcs_vac083_visits'),
    path('edcs_vac083_jquery/', edcs_vac083_jquery, name='edcs_vac083_jquery'),
    path('publishers/', PublisherList.as_view()),
    path('detail/', PublisherDetail.as_view()),
    path('book/', BookList.as_view()),
    path('list/', AcmeBookList.as_view()),
    path('admin/', admin.site.urls),
    path('books/<publisher>/', PublisherBookList.as_view()),
    path('authors/<int:pk>/', AuthorDetailView.as_view(), name='author-detail'),
]
