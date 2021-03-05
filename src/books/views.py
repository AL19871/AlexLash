from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import DetailView, DeleteView, ListView, UpdateView, CreateView
from books.models import Autors, Genres, Publishers, BooksList, Series, Addresses, Cities
from django.db.models import Q

def edit_context(request_query, context):
    context['permission_address_view'] = request_query.user.has_perm('books.view_addresses')
    context['permission_city_view'] = request_query.user.has_perm('books.view_cities')
    context['permission_seria_view'] = request_query.user.has_perm('books.view_series')
    context['permission_publisher_view'] = request_query.user.has_perm('books.view_publishers')
    context['permission_book_view'] = request_query.user.has_perm('books.view_bookslist')
    context['permission_genre_view'] = request_query.user.has_perm('books.view_genres')
    context['permission_author_view'] = request_query.user.has_perm('books.view_autors')
    context['q'] = request_query.GET.get('q')
    field_to_sort = request_query.GET.get('field')
    direction_to_sort = request_query.GET.get('direction')
    context['field_to_sort'] = field_to_sort
    context['sort_form'] = f'field={field_to_sort}&direction={direction_to_sort}'
    direction_to_sort = 'up' if direction_to_sort == 'down' else 'down'
    context['direction_to_sort'] = direction_to_sort
    context['sort_form_new'] = f'direction={direction_to_sort}'

    return context

def home_page(request):
    context = {}
    context['object_book_current'] = BooksList.objects.first()
    context['objects_book_list'] = BooksList.objects.all()
    context['objects_author_list'] = Autors.objects.all()

    context = edit_context(request, context)

    return render(request, template_name = 'home.html', context=context)

class BookList(ListView):
    login_url = reverse_lazy('my-login')
    model = BooksList
    paginate_by = 10
    #permission_required = 'books.view_bookslist'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['permission_add'] = self.request.user.has_perm('books.add_bookslist')
        context['permission_view'] = self.request.user.has_perm('books.view_bookslist')
        context['permission_change'] = self.request.user.has_perm('books.change_bookslist')
        context['permission_delete'] = self.request.user.has_perm('books.delete_bookslist')
        context['search_field'] = 'books-list'
        
        context = edit_context(self.request, context)

        return context

    def get_ordering(self):
        field_to_sort = self.request.GET.get('field') if self.request.GET.get('field') else 'pk'
        direction_to_sort = '-' if self.request.GET.get('direction') == 'down' else ''
        return f'{direction_to_sort}{field_to_sort}' if field_to_sort else super().get_ordering()

    def get_queryset(self):
        field_to_query = self.request.GET.get('q')
        qs = super().get_queryset()
        if field_to_query:
            qs = qs.filter(Q(name__icontains=field_to_query) | Q(cost__icontains=field_to_query) | Q(amount__icontains=field_to_query) | Q(rating__icontains=field_to_query))
        qs = qs.order_by(self.get_ordering())
        return qs

class BookDetail(DetailView):
    login_url = reverse_lazy('my-login')
    model = BooksList

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['permission'] = self.request.user.has_perm('books.view_bookslist')
        context = edit_context(self.request, context)
        return context

class BookDelete(PermissionRequiredMixin, DeleteView):
    login_url = reverse_lazy('my-login')
    model = BooksList
    permission_required = ('books.view_bookslist', 'books.delete_bookslist')
    success_url = reverse_lazy('books-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['permission'] = self.request.user.has_perm('books.delete_bookslist')
        context = edit_context(self.request, context)
        return context

class BookCreate(PermissionRequiredMixin, CreateView):
    login_url = reverse_lazy('my-login')
    model = BooksList
    permission_required = ('books.view_bookslist', 'books.add_bookslist')
    fields = ('name', 'image', 'cost', 'author', 'seria', 'genre', 'year_of_publishing', 'number_of_pages', 'binding', 
        'format_of_book', 'ISBN', 'weight', 'age_restrictions', 'publisher', 'amount', 'active', 'rating')
    success_url = reverse_lazy('books-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['permission'] = self.request.user.has_perm('books.add_bookslist')
        context = edit_context(self.request, context)
        return context

class BookUpdate(PermissionRequiredMixin, UpdateView):
    login_url = reverse_lazy('my-login')
    model = BooksList
    fields = ('name', 'cost', 'amount', 'active')
    template_name = 'bookslist_update.html'
    permission_required = ('books.view_bookslist', 'books.change_bookslist')
    success_url = reverse_lazy('books-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['permission'] = self.request.user.has_perm('books.change_bookslist')
        context = edit_context(self.request, context)
        return context

class AutorDetail(PermissionRequiredMixin, DetailView):
    login_url = reverse_lazy('my-login')
    model = Autors
    permission_required = 'books.view_autors'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['permission'] = self.request.user.has_perm('books.view_autors')
        context = edit_context(self.request, context)
        return context

class AutorDelete(PermissionRequiredMixin, DeleteView):
    login_url = reverse_lazy('my-login')
    model = Autors
    permission_required = ('books.view_autors', 'books.delete_autors')
    success_url = reverse_lazy('autors-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['permission'] = self.request.user.has_perm('books.delete_autors')
        context = edit_context(self.request, context)
        return context

class AutorList(PermissionRequiredMixin, ListView):
    login_url = reverse_lazy('my-login')
    model = Autors
    paginate_by = 10
    permission_required = 'books.view_autors'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['permission_add'] = self.request.user.has_perm('books.add_autors')
        context['permission_view'] = self.request.user.has_perm('books.view_autors')
        context['permission_change'] = self.request.user.has_perm('books.change_autors')
        context['permission_delete'] = self.request.user.has_perm('books.delete_autors')
        context['search_field'] = 'autors-list'
        context = edit_context(self.request, context)
        
        return context

    def get_ordering(self):
        field_to_sort = self.request.GET.get('field') if self.request.GET.get('field') else 'pk'
        direction_to_sort = '-' if self.request.GET.get('direction') == 'down' else ''
        return f'{direction_to_sort}{field_to_sort}' if field_to_sort else super().get_ordering()

    def get_queryset(self):
        field_to_query = self.request.GET.get('q')
        qs = super().get_queryset()
        if field_to_query:
            qs = qs.filter(Q(first_name__icontains=field_to_query) | Q(last_name__icontains=field_to_query) | Q(date_of_birth__icontains=field_to_query))
        qs = qs.order_by(self.get_ordering())
        return qs

class AutorCreate(PermissionRequiredMixin, CreateView):
    login_url = reverse_lazy('my-login')
    model = Autors
    fields = ('first_name', 'last_name', 'date_of_birth', 'address')
    permission_required = ('books.view_autors', 'books.add_autors')
    success_url = reverse_lazy('autors-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['permission'] = self.request.user.has_perm('books.add_autors')
        context = edit_context(self.request, context)
        return context

class AutorUpdate(PermissionRequiredMixin, UpdateView):
    login_url = reverse_lazy('my-login')
    model = Autors
    fields = ('first_name', 'last_name', 'date_of_birth')
    template_name = 'autors_update.html'
    permission_required = ('books.view_autors', 'books.change_autors')
    success_url = reverse_lazy('autors-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['permission'] = self.request.user.has_perm('books.change_autors')
        context = edit_context(self.request, context)
        return context

class GenreDetail(PermissionRequiredMixin, DetailView):
    login_url = reverse_lazy('my-login')
    model = Genres
    permission_required = 'books.view_genres'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['permission'] = self.request.user.has_perm('books.view_genres')
        context = edit_context(self.request, context)
        return context

class GenreDelete(PermissionRequiredMixin, DeleteView):
    login_url = reverse_lazy('my-login')
    model = Genres
    permission_required = ('books.view_genres', 'books.delete_genres')
    success_url = reverse_lazy('genres-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['permission'] = self.request.user.has_perm('books.delete_genres')
        context = edit_context(self.request, context)
        return context

class GenreList(PermissionRequiredMixin, ListView):
    login_url = reverse_lazy('my-login')
    model = Genres
    paginate_by = 10
    permission_required = 'books.view_genres'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['permission_add'] = self.request.user.has_perm('books.add_genres')
        context['permission_delete'] = self.request.user.has_perm('books.delete_genres')
        context['permission_view'] = self.request.user.has_perm('books.view_genres')
        context['permission_change'] = self.request.user.has_perm('books.change_genres')
        context['search_field'] = 'genres-list'
        context = edit_context(self.request, context)
        
        return context

    def get_ordering(self):
        field_to_sort = self.request.GET.get('field') if self.request.GET.get('field') else 'pk'
        direction_to_sort = '-' if self.request.GET.get('direction') == 'down' else ''
        return f'{direction_to_sort}{field_to_sort}' if field_to_sort else super().get_ordering()

    def get_queryset(self):
        field_to_query = self.request.GET.get('q')
        qs = super().get_queryset()
        if field_to_query:
            qs = qs.filter(Q(name__icontains=field_to_query) | Q(description__icontains=field_to_query))
        qs = qs.order_by(self.get_ordering())
        return qs

class GenreCreate(PermissionRequiredMixin, CreateView):
    login_url = reverse_lazy('my-login')
    model = Genres
    fields = ('name', 'description')
    permission_required = ('books.view_genres', 'books.add_genres')
    success_url = reverse_lazy('genres-list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['permission'] = self.request.user.has_perm('books.add_genres')
        context = edit_context(self.request, context)
        return context

class GenreUpdate(PermissionRequiredMixin, UpdateView):
    login_url = reverse_lazy('my-login')
    model = Genres
    fields = ('name', 'description')
    template_name = 'genres_update.html'
    permission_required = ('books.view_genres', 'books.change_genres')
    success_url = reverse_lazy('genres-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['permission'] = self.request.user.has_perm('books.change_genres')
        context = edit_context(self.request, context)
        return context

class SeriaDetail(PermissionRequiredMixin, DetailView):
    login_url = reverse_lazy('my-login')
    model = Series
    permission_required = 'books.view_series'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['permission'] = self.request.user.has_perm('books.view_series')
        context = edit_context(self.request, context)
        return context

class SeriaDelete(PermissionRequiredMixin, DeleteView):
    login_url = reverse_lazy('my-login')
    model = Series
    success_url = reverse_lazy('series-list')
    permission_required = ('books.view_series', 'books.delete_series')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['permission'] = self.request.user.has_perm('books.delete_series')
        context = edit_context(self.request, context)
        return context

class SeriaList(PermissionRequiredMixin, ListView):
    login_url = reverse_lazy('my-login')
    model = Series
    paginate_by = 10
    permission_required = 'books.view_series'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['permission_add'] = self.request.user.has_perm('books.add_series')
        context['permission_change'] = self.request.user.has_perm('books.change_series')
        context['permission_delete'] = self.request.user.has_perm('books.delete_series')
        context['permission_view'] = self.request.user.has_perm('books.view_series')
        context['search_field'] = 'series-list'
        context = edit_context(self.request, context)

        return context

    def get_ordering(self):
        field_to_sort = self.request.GET.get('field') if self.request.GET.get('field') else 'pk'
        direction_to_sort = '-' if self.request.GET.get('direction') == 'down' else ''
        return f'{direction_to_sort}{field_to_sort}' if field_to_sort else super().get_ordering()

    def get_queryset(self):
        field_to_query = self.request.GET.get('q')
        qs = super().get_queryset()
        if field_to_query:
            qs = qs.filter(Q(name__icontains=field_to_query) | Q(description__icontains=field_to_query))
        qs = qs.order_by(self.get_ordering())
        return qs

class SeriaCreate(PermissionRequiredMixin, CreateView):
    login_url = reverse_lazy('my-login')
    model = Series
    fields = ('name', 'description')
    permission_required = ('books.view_series', 'books.add_series')
    success_url = reverse_lazy('series-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['permission'] = self.request.user.has_perm('books.add_series')
        context = edit_context(self.request, context)
        return context

class SeriaUpdate(PermissionRequiredMixin, UpdateView):
    login_url = reverse_lazy('my-login')
    model = Series
    fields = ('name', 'description')
    template_name = 'series_update.html'
    permission_required = ('books.view_series', 'books.change_series')
    success_url = reverse_lazy('series-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['permission'] = self.request.user.has_perm('books.change_series')
        context = edit_context(self.request, context)
        return context

class PublisherDetail(PermissionRequiredMixin, DetailView):
    login_url = reverse_lazy('my-login')
    model = Publishers
    permission_required = 'books.view_publishers'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['permission'] = self.request.user.has_perm('books.view_publishers')
        context = edit_context(self.request, context)
        return context

class PublisherDelete(PermissionRequiredMixin, DeleteView):
    login_url = reverse_lazy('my-login')
    model = Publishers
    success_url = reverse_lazy('publishers-list')
    permission_required = ('books.view_publishers', 'books.delete_publishers')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['permission'] = self.request.user.has_perm('books.delete_publishers')
        context = edit_context(self.request, context)
        return context

class PublisherList(PermissionRequiredMixin, ListView):
    login_url = reverse_lazy('my-login')
    model = Publishers
    paginate_by = 10
    permission_required = 'books.view_publishers'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['permission_view'] = self.request.user.has_perm('books.view_publishers')
        context['permission_change'] = self.request.user.has_perm('books.change_publishers')
        context['permission_add'] = self.request.user.has_perm('books.add_publishers')
        context['permission_delete'] = self.request.user.has_perm('books.delete_publishers')
        context['search_field'] = 'publishers-list'
        context = edit_context(self.request, context)

        return context

    def get_ordering(self):
        field_to_sort = self.request.GET.get('field') if self.request.GET.get('field') else 'pk'
        direction_to_sort = '-' if self.request.GET.get('direction') == 'down' else ''
        return f'{direction_to_sort}{field_to_sort}' if field_to_sort else super().get_ordering()

    def get_queryset(self):
        field_to_query = self.request.GET.get('q')
        qs = super().get_queryset()
        if field_to_query:
            qs = qs.filter(Q(name__icontains=field_to_query) | Q(address__city__name__icontains=field_to_query))
        qs = qs.order_by(self.get_ordering())
        return qs

class PublisherCreate(PermissionRequiredMixin, CreateView):
    login_url = reverse_lazy('my-login')
    model = Publishers
    fields = ('name', 'address')
    success_url = reverse_lazy('publishers-list')
    permission_required = ('books.view_publishers', 'books.add_publishers')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['permission'] = self.request.user.has_perm('books.add_publishers')
        context = edit_context(self.request, context)
        return context

class PublisherUpdate(PermissionRequiredMixin, UpdateView):
    login_url = reverse_lazy('my-login')
    model = Publishers
    fields = ('name', )
    template_name = 'publishers_update.html'
    success_url = reverse_lazy('publishers-list')
    permission_required = ('books.view_publishers', 'books.change_publishers')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['permission'] = self.request.user.has_perm('books.change_publishers')
        context = edit_context(self.request, context)
        return context

class AddressDetail(PermissionRequiredMixin, DetailView):
    login_url = reverse_lazy('my-login')
    model = Addresses
    permission_required = 'books.view_addresses'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['permission'] = self.request.user.has_perm('books.view_addresses')
        context = edit_context(self.request, context)
        return context

class AddressDelete(PermissionRequiredMixin, DeleteView):
    login_url = reverse_lazy('my-login')
    model = Addresses
    success_url = reverse_lazy('addresses-list')
    permission_required = ('books.view_addresses', 'books.delete_addresses')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['permission'] = self.request.user.has_perm('books.delete_addresses')
        context = edit_context(self.request, context)
        return context

class AddressList(PermissionRequiredMixin, ListView):
    login_url = reverse_lazy('my-login')
    model = Addresses
    paginate_by = 10
    permission_required = 'books.view_addresses'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['permission_add'] = self.request.user.has_perm('books.add_addresses')
        context['permission_view'] = self.request.user.has_perm('books.view_addresses')
        context['permission_change'] = self.request.user.has_perm('books.change_addresses')
        context['permission_delete'] = self.request.user.has_perm('books.delete_addresses')
        context['search_field'] = 'addresses-list'
        context = edit_context(self.request, context)

        return context

    def get_ordering(self):
        field_to_sort = self.request.GET.get('field') if self.request.GET.get('field') else 'pk'
        direction_to_sort = '-' if self.request.GET.get('direction') == 'down' else ''
        return f'{direction_to_sort}{field_to_sort}' if field_to_sort else super().get_ordering()

    def get_queryset(self):
        field_to_query = self.request.GET.get('q')
        qs = super().get_queryset()
        if field_to_query:
            qs = qs.filter(Q(city__name__icontains=field_to_query) | Q(street__icontains=field_to_query))
        qs = qs.order_by(self.get_ordering())
        return qs

class AddressCreate(PermissionRequiredMixin, CreateView):
    login_url = reverse_lazy('my-login')
    model = Addresses
    fields = ('city', 'street', 'block', 'house')
    success_url = reverse_lazy('addresses-list')
    permission_required = ('books.view_addresses', 'books.add_addresses')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['permission'] = self.request.user.has_perm('books.add_addresses')
        context = edit_context(self.request, context)
        return context

class AddressUpdate(PermissionRequiredMixin, UpdateView):
    login_url = reverse_lazy('my-login')
    model = Addresses
    fields = ('street', 'block', 'house')
    template_name = 'addresses_update.html'
    success_url = reverse_lazy('addresses-list')
    permission_required = ('books.view_addresses', 'books.change_addresses')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['permission'] = self.request.user.has_perm('books.change_addresses')
        context = edit_context(self.request, context)
        return context

class CityDetail(PermissionRequiredMixin, DetailView):
    login_url = reverse_lazy('my-login')
    model = Cities
    permission_required = 'books.view_cities'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['permission'] = self.request.user.has_perm('books.view_cities')
        context = edit_context(self.request, context)
        return context

class CityDelete(PermissionRequiredMixin, DeleteView):
    login_url = reverse_lazy('my-login')
    model = Cities
    redirect_field_name = 'redirect_to'
    permission_required = ('books.view_cities', 'books.delete_cities')
    success_url = reverse_lazy('cities-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['permission'] = self.request.user.has_perm('books.delete_cities')
        context = edit_context(self.request, context)
        return context

class CityList(PermissionRequiredMixin, ListView):
    login_url = reverse_lazy('my-login')
    model = Cities
    paginate_by = 10
    permission_required = 'books.view_cities'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['permission_add'] = self.request.user.has_perm('books.add_cities')
        context['permission_view'] = self.request.user.has_perm('books.view_cities')
        context['permission_delete'] = self.request.user.has_perm('books.delete_cities')
        context['permission_change'] = self.request.user.has_perm('books.change_cities')
        context['search_field'] = 'cities-list'
        context = edit_context(self.request, context)

        return context

    def get_ordering(self):
        field_to_sort = self.request.GET.get('field') if self.request.GET.get('field') else 'pk'
        direction_to_sort = '-' if self.request.GET.get('direction') == 'down' else ''
        return f'{direction_to_sort}{field_to_sort}' if field_to_sort else super().get_ordering()

    def get_queryset(self):
        field_to_query = self.request.GET.get('q')
        qs = super().get_queryset()
        if field_to_query:
            qs = qs.filter(name__icontains=field_to_query)
        qs = qs.order_by(self.get_ordering())
        return qs

class CityCreate(PermissionRequiredMixin, CreateView):
    login_url = reverse_lazy('my-login')
    model = Cities
    permission_required = ('books.view_cities', 'books.add_cities')
    fields = ('name',)
    success_url = reverse_lazy('cities-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['permission'] = self.request.user.has_perm('books.add_cities')
        context = edit_context(self.request, context)
        return context

class CityUpdate(PermissionRequiredMixin, UpdateView):
    login_url = reverse_lazy('my-login')
    model = Cities
    permission_required = ('books.view_cities', 'books.change_cities')
    fields = ('name', )
    template_name = 'cities_update.html'
    success_url = reverse_lazy('cities-list')
    login_url = reverse_lazy('my-login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['permission'] = self.request.user.has_perm('books.change_cities')
        context = edit_context(self.request, context)
        return context
