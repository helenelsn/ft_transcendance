import django_tables2 as tables
from common.view_getter import get_view

class ActionsColumn(tables.Column):
    empty_values=[]
    def render(self, record):
        return get_view(record).actions_links()
    
class LinkedDetailNameColumn(tables.Column):
    def render(self, value):
        return get_view(value).detail_linked_name

    def order(self, queryset, is_descending : bool):
        on= '-relation' if is_descending else 'relation'
        return (queryset.order_by(on), True)