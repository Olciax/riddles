from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from riddles.models import Riddles, DoneRiddles, MyUser, Level, Curiosity, CuriosityQA


class MyUserInline(admin.StackedInline):
    model = MyUser
    can_delete = False


class UserAdmin(BaseUserAdmin):
    inlines = [MyUserInline, ]


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Riddles)
admin.site.register(DoneRiddles)
admin.site.register(Level)
admin.site.register(Curiosity)
admin.site.register(CuriosityQA)

#