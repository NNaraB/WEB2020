from django.urls import path
from django.views.generic import RedirectView

from . import views


urlpatterns = [
    path('api/companies/', views.companies, name = "companies"),
    path('api/companies/<int:company_id>/', views.company_detail, name = "company_detail") ,
    path('api/companies/<int:company_id>/vacancies/', views.vacancies, name = "vacancies") ,
    path('api/vacancies/<int:vacancy_id>/', views.vacancy_detail, name = "vacancy_detail"),
    path('api/vacancies/top_ten', views.all_vacancies_top10, name = "vacancies_top10"),
    path('api/<int:company_id>/vacancies/top_ten', views.company_vacancies_top10, name="comp_vacancies_top10")
]