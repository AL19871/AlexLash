
def edit_context(request_query, context):
    context['permission_address_view'] = request_query.user.has_perm('books.view_addresses')
    context['permission_city_view'] = request_query.user.has_perm('books.view_cities')
    context['permission_order_view'] = request_query.user.has_perm('order.view_order')
    context['permission_login'] = request_query.user.is_authenticated
    context['permission_userprofile_view'] = request_query.user.has_perm('customer.view_userprofile')
    context['q'] = request_query.GET.get('q') if request_query.GET.get('q') and request_query.GET.get('q') != None else 'Search'
    field_to_sort = request_query.GET.get('field')
    direction_to_sort = request_query.GET.get('direction')
    context['field_to_sort'] = field_to_sort
    context['sort_form'] = f'field={field_to_sort}&direction={direction_to_sort}'
    direction_to_sort = None if field_to_sort == None else 'up' if direction_to_sort == 'down' else 'down'
    context['direction_to_sort'] = direction_to_sort
    context['sort_form_new'] = f'direction={direction_to_sort}'

    return context