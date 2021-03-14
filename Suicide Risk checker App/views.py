from django.http import HttpResponse
from django.shortcuts import render
import joblib
import math


def home(request):
    return render(request, 'home.html')


def result(request):

    Rf = joblib.load('finalized_modeltest.sav')

    lis = []

    lis.append(request.GET['Age_group'])
    lis.append(request.GET['Gender'])
    lis.append(request.GET['Marital_status'])
    lis.append(request.GET['Occupation'])
    lis.append(request.GET['Problem_with_family'])
    lis.append(request.GET['Marital_dissatisfaction'])
    lis.append(request.GET['Relationship_problem'])
    lis.append(request.GET['Unexpected_result_or_failed in exam'])
    lis.append(request.GET['Sexual_harassment'])
    lis.append(request.GET['Problem_in_workspace'])
    lis.append(request.GET['Victim_of_domestic_violation'])
    lis.append(request.GET['Chronic_physical_illness'])
    lis.append(request.GET['financial_constraint'])
    lis.append(request.GET['Depressed'])
    lis.append(request.GET['Struggled_with_dept'])
    lis.append(request.GET['Mentall_illness_apart_from depression'])
    lis.append(request.GET['Not_getting_job'])
    lis.append(request.GET['False_allegation'])

    answer = Rf.predict_proba([lis])[:, 1]
    ans = answer[0]*100
    ans = math.ceil(ans)

    return render(request, "result.html", {'ans': ans})
