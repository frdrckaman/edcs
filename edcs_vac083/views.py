from django.shortcuts import render, redirect, get_object_or_404
from edcs_vac083.models import Demographic, ExclusionCriteria, ScreeningTwo,\
    Publisher, Book, Author
from django.views.generic import ListView, DeleteView, DetailView
from django.utils import timezone


def edcs_vac083_home(request):
    context = {

    }
    return render(request, 'edcs_vac083/edcs_vac083_home.html', context)


def edcs_vac083_visits(request):
    screeningTwo = ScreeningTwo()
    screeningOne = Demographic()

    counte = ExclusionCriteria.objects.count()
    count = ScreeningTwo.objects.count()
    counts1 = Demographic.objects.count()
    context = {
        'screeningOne': screeningOne, 'screeningTwo': screeningTwo, 'count': count,
        'counts1': counts1, 'counte': counte
    }
    return render(request, 'edcs_vac083/edcs_vac083_visits.html', context)


def edcs_vac083_jquery(request):

    context = {
        'edcs_vac083_jquery': edcs_vac083_jquery
    }
    return render(request, 'edcs_vac083/edcs_vac083_jquery.html')


class PublisherList(ListView):
    model = Publisher
    template_name = 'edcs_vac083/publisher_list.html'
    context_object_name = 'my_favorite_publishers'
    paginate_by = 10


class PublisherDetail(DetailView):
    context_object_name = 'publisher'
    queryset = Publisher.objects.all()


class BookList(ListView):
    queryset = Book.objects.order_by('-publication_date')
    context_object_name = 'book_list'


class AcmeBookList(ListView):
    context_object_name = 'book_list'
    queryset = Book.objects.filter(publisher__name='ACME Publishing')
    template_name = 'edcs_vac083/acme_list.html'


class PublisherBookList(ListView):
    template_name = 'edcs_vac083/books_by_publisher.html'
    def get_queryset(self):
        self.publisher = get_object_or_404(Publisher, name=self.kwargs['publisher'])
        return Book.objects.filter(publisher=self.publisher)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in the publisher
        context['publisher'] = self.publisher
        return context


class AuthorDetailView(DetailView):
    queryset = Author.objects.all()
    template_name = 'edcs_vac083/author_detail.html'
    def get_object(self):
        obj = super().get_object()
        # Record the last accessed date
        obj.last_accessed = timezone.now()
        obj.save()
        return obj