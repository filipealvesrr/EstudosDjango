from django.urls import path
# from recipes.views import home
# from recipes import views
# Algumas alternativas acima
from . import views  # Foi usado o ponto por estar na pasta recipes

urlpatterns = [
    path('', views.home),
    # o argumento <id>, informa que na view recipe deve ser
    # passado um id como parametro da função.
    path('recipes/<int:id>/', views.recipe)
]
