from edcs_vac083.forms import DemographicForm, ExclusionCriteriaForm, ScreeningTwoForm
from django.shortcuts import render, redirect, get_object_or_404
from edcs_vac083.models import Demographic, ExclusionCriteria, ScreeningTwo, Publisher, Book, Author
from django.http import HttpResponse
from django.views.generic import ListView, DeleteView, DetailView
from django.utils import timezone


class edcs_vac083_home(ListView):
    model = Demographic
    template_name = 'edcs_vac083/edcs_vac083_home.html'


class DemographicView(ListView):
    model = Demographic
    template_name = 'edcs_vac083/edcs_vac083_view.html'


class edcs_vac083_visits(ListView):
    form = ScreeningTwoForm
    model = ScreeningTwo
    template_name = 'edcs_vac083/edcs_vac083_visits.html'


def DemographicCreate(request):
    if request.method == 'POST':
        form = DemographicForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('edcs_dashboard:home')

    else:
        form = DemographicForm()
    return render(request, 'edcs_vac083/edcs_vac083_enter_data.html', {'form': form})


def edcs_vac083_count(request):
    demographicCount = Demographic.objects.count()
    context =(
    {
        'demographicCount' : demographicCount,
    }
    )

    return render(request, 'edcs_vac083/edcs_vac083_home.html', context)

#
# def edcs_vac083_forms(request):
#     # if this is a POST request we need to process the form data
#     if request.method == 'POST':
#         # create a form instance and populate it with data from the request:
#         form = ContactForm(request.POST)
#         # check whether it's valid:
#         if form.is_valid():
#             subject = form.cleaned_data['subject']
#             message = form.cleaned_data['message']
#             sender = form.cleaned_data['sender']
#             cc_myself = form.cleaned_data['cc_myself']
#
#             recipients = ['info@example.com']
#             if cc_myself:
#                 recipients.append(sender)
#
#             send_mail(subject, message, sender, recipients)
#             return HttpResponseRedirect('/thanks/')
#
#     # if a GET (or any other method) we'll create a blank form
#     else:
#         form = ContactForm()
#
#     return render(request, 'edcs_vac083/name.html', {'form': form})


class ExclusionCriteriaView(ListView):
    model = ExclusionCriteria
    template_name = 'edcs_vac083/edcs_vac083_enter_data_exclusion.html.html'


def ScreeningOneView(request):
    if request.method == 'POST':
        form = ScreeningTwoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('edcs_vac083_visits:edcs_vac083_visits')

    else:
        form = ScreeningTwoForm()
    return render(request, 'edcs_vac083/screening/sc1/edcs_vac083_enter_data.html', {'form': form})


def ScreeningTwoView(request):
    if request.method == 'POST':
        form2 = ScreeningTwoForm(request.POST)
        if form2.is_valid():
            form2.save()
            return redirect('edcs_vac083_visits:edcs_vac083_visits')

    else:
        form2 = ScreeningTwoForm()
    return render(request, 'edcs_vac083/edcs_vac083_enter_data2.html', {'form2': form2})


def ScreeningTwoViewData(request):
    if request.method == 'POST':
        form = ScreeningTwoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('edcs_vac083_visits:edcs_vac083_visits')

    else:
        form = ScreeningTwoForm()
    return render(request, 'edcs_vac083/screening/sc2/edcs_vac083_enter_data.html', {'form': form})


class PublisherList(ListView):
    model = Publisher
    template_name = 'edcs_vac083/publisher_list.html'
    context_object_name = 'my_favorite_publishers'
    paginate_by = 10

#
# class PublisherDetail(DetailView):
#
#     model = Publisher
#
#     def get_context_data(self, **kwargs):
#         # Call the base implementation first to get a context
#         context = super().get_context_data(**kwargs)
#         # Add in a QuerySet of all the books
#         context['book_list'] = Book.objects.all()
#         return context


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