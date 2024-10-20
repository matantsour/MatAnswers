from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path("",views.indexView.as_view(),name="about-me-page"),
    path("resume",views.resume_page.as_view(),name="resume-page"),
    path("blog",views.blog_page.as_view(),name="blog-page"),
    path("projects",views.projects_page.as_view(),name="projects-page"),
    path("riddles",views.riddles_page.as_view(),name="riddles-page"),
    path("games",views.games_page.as_view(),name="games-page"),
    path("recepies",views.recepies_page.as_view(),name="recepies-page"),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)