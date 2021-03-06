"""ask URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^$', 'qa.views.new_questions', name='new_questions'),
    url(r'^admin/', admin.site.urls),
    url(r'^login/', 'qa.views.test'),
    url(r'^signup/', 'qa.views.test'),
    url(r'^ask/', 'qa.views.test'),
    url(r'^popular/', 'qa.views.popular_questions', name='popular_questions'),
    url(r'^new/', 'qa.views.new_questions', name='new_questions'),
    url(r'^question/(?P<id>\d+)', 'qa.views.question_details', name='question_details'),
    url(r'^.+/', 'qa.views.test404'),
]
