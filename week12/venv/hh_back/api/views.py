from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from django.http import JsonResponse
# Create your views here.
from  . models import  Company,Vacancy



def companies(request):
    if request.method == 'GET':
        companies = Company.objects.order_by('id')
        company_list = [company.short() for company in companies]
    return JsonResponse(company_list, safe = False)


def company_detail(request, company_id):
    try:
        company = Company.objects.get(id = company_id)
    except Exception as e:
        return JsonResponse({'error':str(e)})
    return JsonResponse(company.short())

def vacancies(request, company_id):
    vacancies = Vacancy.objects.filter(company_id=company_id)
    vacancy_list = [vacancy.short() for vacancy in vacancies]
    return JsonResponse(vacancy_list, safe = False)

def vacancy_detail(request, vacancy_id):
    vacancy = Vacancy.objects.get(id = vacancy_id)
    return JsonResponse(vacancy.short())

def all_vacancies_top10(request):
    vacancies = Vacancy.objects.all().order_by('-salary')
    top_vacancy_list = [vacancy.short() for vacancy in vacancies[:10]]
    return JsonResponse(top_vacancy_list,safe = False)

def company_vacancies_top10(request, company_id):
    vacancies = Vacancy.objects.all().filter(company_id = company_id).order_by('-salary')
    top_vacancy_list = [vacancy.short() for vacancy in vacancies[:10]]
    return JsonResponse(top_vacancy_list,safe = False)