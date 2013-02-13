from django.contrib import admin
from django.contrib.contenttypes import generic

from .models import Person, CompassUser, Role, Term
from .models import Undergrad, Transfer, GradStudent, Postdoc


class PersonInline(generic.GenericStackedInline):
    model = Person
    max_num = 1


class PersonAdmin(admin.ModelAdmin):
    inlines = [
        PersonInline
    ]


admin.site.register(Person)
admin.site.register(CompassUser)
admin.site.register(Role)
admin.site.register(Term)

admin.site.register(Undergrad,PersonAdmin)
admin.site.register(Transfer, PersonAdmin)
admin.site.register(GradStudent, PersonAdmin)
admin.site.register(Postdoc, PersonAdmin)
