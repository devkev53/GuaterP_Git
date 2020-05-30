"""guaterpura URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include((
    	'base.urls', 'base'), namespace='base')), # <- Llamamos a base
    path('', include((
        'pedido.urls', 'pedido'), namespace='pedido')),
    path('', include((
        'producto.urls', 'producto'), namespace='producto')),
    path('', include((
        'perfil.urls', 'empleado'), namespace='empleado')),
    path('', include((
        'cliente.urls', 'cliente'), namespace='cliente')),
    path('', include((
        'venta.urls', 'venta'), namespace='venta')),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "Guater Pura"
admin.site.site_title = "Portal de Guater Pura"
admin.site.index_title = "Bienvenidos al sitio de administración"