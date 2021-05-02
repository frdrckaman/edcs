from django.urls import path
from edcs_vac083.views import DemographicView, DemographicCreate, \
     edcs_vac083_home, edcs_vac083_visits, edcs_vac083_count, ScreeningOneView,\
     ExclusionCriteriaView, ScreeningTwoView, PublisherList, PublisherDetail, BookList,\
     AcmeBookList, PublisherBookList, AuthorDetailView, ScreeningTwoViewData
from django.contrib import admin


app_name = 'edcs_vac083'

urlpatterns = [
    path("DemographicView", DemographicView.as_view(), name="DemographicView"),
    path('DemographicCreate/', DemographicCreate, name='DemographicCreate'),
    path('edcs_vac083_home/', edcs_vac083_home.as_view(), name='edcs_vac083_home'),
    path('edcs_vac083_visits/', edcs_vac083_visits.as_view(), name='edcs_vac083_visits'),
    # path('edcs_vac083_forms/', edcs_vac083_forms, name='edcs_vac083_forms'),
    path('edcs_vac083_count/', edcs_vac083_count, name='edcs_vac083_count'),
    path('edcs_vac083_screening_one/', ScreeningOneView, name='edcs_vac083_screening_one'),
    path('edcs_vac083_screening_two/', ScreeningTwoView, name='edcs_vac083_screening_two'),
    path('edcs_vac083_enter_data2/', ScreeningTwoViewData, name='edcs_vac083_screening_two_enter_data'),
    path('edcs_vac083_exclusion/', ExclusionCriteriaView.as_view(), name='edcs_vac083_exclusion'),
    path('publishers/', PublisherList.as_view()),
    path('detail/', PublisherDetail.as_view()),
    path('book/', BookList.as_view()),
    path('list/', AcmeBookList.as_view()),
    path('admin/', admin.site.urls),
    path('books/<publisher>/', PublisherBookList.as_view()),
    path('authors/<int:pk>/', AuthorDetailView.as_view(), name='author-detail'),
]
