import django_filters
from .models import Notification, models
from django.forms import CheckboxInput

class NotificationFilter(django_filters.FilterSet):
    class Meta:
        model = Notification
        fields = ["is_read", ]
        
        # filter_overrides = {
        #     models.CharField: {
        #         'filter_class': django_filters.CharFilter,
        #         'extra': lambda f: {
        #             'lookup_expr': 'icontains',
        #         },
        #     },
        #     models.BooleanField: {
        #         'filter_class': django_filters.BooleanFilter,
        #         'extra': lambda f: {
        #             'widget': CheckboxInput,
        #         },
        #     },
        # }
        
    @property
    def qs(self):
        parent = super().qs
        return parent.filter(user=self.request.user).order_by('is_read')