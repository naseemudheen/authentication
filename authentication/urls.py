
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('user.urls'), namespace='user')),
    path('', include('pwa.urls')),

]
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