from django.contrib import admin
from .models import Usuario

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'matricula', 'email', 'tipo_usuario', 'curso', 'departamento', 'data_cadastro')
    list_filter = ('tipo_usuario', 'data_cadastro')
    search_fields = ('nome', 'matricula', 'email')
    readonly_fields = ('data_cadastro',)
    
    fieldsets = (
        ('Informações Básicas', {
            'fields': ('nome', 'matricula', 'email', 'telefone', 'tipo_usuario')
        }),
        ('Informações Acadêmicas/Profissionais', {
            'fields': ('curso', 'departamento')
        }),
        ('Timestamps', {
            'fields': ('data_cadastro',)
        }),
    )

    def get_queryset(self, request):
        return super().get_queryset(request).select_related()
    
