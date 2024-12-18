import django_tables2 as tables
from common.global_view_mananger import get_view

class ActionsColumn(tables.Column):
    empty_values=[]
    def render(self, record):
        return get_view(record).col_actions_links()
    
class ProfilDetailNameColumn(tables.Column):
    def render(self, value):
        return get_view(value).detail_linked_name

    def order(self, queryset, is_descending : bool):
        on= '-relation' if is_descending else 'relation'
        return (queryset.order_by(on), True)