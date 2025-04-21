from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
User = get_user_model()


class UserAdmin (UserAdmin):
    pass

<<<<<<< HEAD
admin.site.register(User)

=======
admin.site.register(User)
>>>>>>> 923b7e74aa52c6ad7c42b9ea8d038dfd98d71b79
