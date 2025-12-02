from .models import Usuario
from .forms import RegistroUsuarioForm
from ..articulo.models import Articulo
from ..comentario.models import Comentario
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth.models import Group
from django.views.generic import CreateView, ListView, DeleteView
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.http import JsonResponse
from django.contrib.auth.forms import PasswordResetForm

class RegistrarUsuario(CreateView):
    template_name = 'registracion/registrar.html'
    form_class = RegistroUsuarioForm

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Registro exitoso. Por favor, inicia sesión.')
        group = Group.objects.get(name='registrado')
        self.object.groups.add(group)
        return redirect('apps.usuario:login')

class LoginUsuario(LoginView):
    template_name = 'registracion/login.html'

    def get_success_url(self):
        messages.success(self.request, 'Login exitoso')
        return reverse('index')
     
class LogoutUsuario(LogoutView):
    next_page = 'index'
    template_name = 'registracion/logout.html'

    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        messages.success(request, 'Logout exitoso')
        return response

class UsuarioListView(LoginRequiredMixin, ListView):
    model = Usuario
    template_name = 'usuario/listUsuario.html'
    context_object_name = 'usuarios'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.exclude(is_superuser=True)
        return queryset

class UsuarioDeleteView(LoginRequiredMixin, DeleteView):
    model = Usuario
    success_url = reverse_lazy('apps.usuario:listUsuario')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        colaborador_group = Group.objects.get(name='Colaborador')
        es_colaborador = colaborador_group in self.object.groups.all()
        context['es_colaborador'] = es_colaborador
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        # 🚫 Evitar que el usuario se elimine a sí mismo
        if self.object == request.user:
            messages.error(request, "No podés eliminar tu propio usuario.")
            return redirect('apps.usuario:listUsuario')

        eliminar_comentarios = request.POST.get('eliminarComentarios', False)
        eliminar_posts = request.POST.get('eliminarPosts', False)

        if eliminar_comentarios:
            Comentario.objects.filter(usuario=self.object).delete()

        if eliminar_posts:
            Articulo.objects.filter(autor=self.object).delete()

        messages.success(request, f'Usuario {self.object.username} eliminado correctamente')
        return self.delete(request, *args, **kwargs)


class MyPasswordResetView(PasswordResetView):
    template_name = 'registracion/recuperarContra.html'

    def get_success_url(self):
        messages.success(self.request, 'Se envió un email de recuperación. Revise su casilla de correo para recuperar su cuenta.')
        return reverse('index')