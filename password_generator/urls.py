from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from jobs.views import home, password, gen_pswrd

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('blog/', include('blog.urls')),
    path('gen_pswrd/', gen_pswrd, name='gen_pswrd'),
    path('password/', password, name='password'),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
