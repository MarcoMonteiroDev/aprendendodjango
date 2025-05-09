from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUsuarioCreateForm, CustomUsuarioChangeForm
from .models import CustomUsuario

@admin.register(CustomUsuario)
class CustomUsuarioAdmim(UserAdmin):
    add_form = CustomUsuarioCreateForm
    form = CustomUsuarioChangeForm
    model = CustomUsuario
    list_display = ('first_name', 'last_name', 'email', 'fone', 'is_staff')

    fieldsets = (
        (None, {'fields' : ('email','password')}),
        ('Informações Pessoais',{'fields':('first_name','last_name','fone')}),
        ('Permissões',{'fields': ('is_active','is_staff','is_superuser','groups','user_permissions')}),
        ('Datas Importantes', {'fields': ('last_login', 'date_joined')}),
    )
    #o add fieldsets necessario para quando add um usuario
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'first_name', 'last_name', 'fone', 'is_staff', 'is_superuser'),
        }),
    )
