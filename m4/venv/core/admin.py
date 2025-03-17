from django.contrib import admin

from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['titulo', '_autor']
    exclude= ['autor',]

    #metodo para mostar todo o nome no post
    def _autor(self, instance):
        return f'{instance.autor.get_full_name()}'
    
    #metodo para somente o usuario logado ver seu post
    def get_queryset(self, request):
        qs = super(PostAdmin, self).get_queryset(request)
        return qs.filter(autor = request.user)
    

    def save_model(self, request, obj, form, change):
        obj.autor = request.user
        super().save_model(request, obj, form, change)