# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework.response import Response
from .models import *
from rest_framework.generics import ListAPIView
# Create your views here.
from django.db.models import Case, CharField, Value
from django.db.models import F, Q, When
from django.db.models import OuterRef, Subquery
from django.db.models.functions import Length

def index(request):
    return render(request,'index.html')


class getsearchdataview(APIView):
    def get(self,request,**kwargs):
        word = request.GET.get("word")
        l=[]
        data_ex = words.objects.filter(Column_2__iexact=word).values_list("Column_2")[:25]
        len_ex = data_ex.count()
        data_st = words.objects.filter(
            Column_2__icontains =word
        ).annotate(containswords=Case(
            When(Column_2__icontains=word, then=F('Column_2')),
            output_field=CharField()

        )).filter(
            Column_2__istartswith=word,
        ).exclude(Column_2__iexact=word).values_list("Column_2")[:(25-len_ex)]

        len_of_startswidth = data_st.count()
        l.extend(data_ex)
        l.extend(data_st)
        if len_of_startswidth+len_ex < 25:
            data_cont = words.objects.filter(Column_2__icontains =word).exclude(Column_2__istartswith=word).values_list("Column_2")[:25-(len_of_startswidth+len_ex)]
            l.extend(data_cont)

        return Response(l)
