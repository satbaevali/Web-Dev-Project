import django_filters
from .models import Skill


class SkillFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains', label='Search by skill name')

    class Meta:
        model = Skill
        fields = ['name']