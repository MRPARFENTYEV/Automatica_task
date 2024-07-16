from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import authentication
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
import json
from visits.models import Worker, Store, Visit
from django.http import JsonResponse
# Create your views here.
import datetime


class AuthView(APIView):
    worker_pk = ''
    print(worker_pk)
    permission_classes = (IsAuthenticated,)

    def get(self, request, phone_num):
        if permission_classes:
            try:
                worker = Worker.objects.get(phone_number=phone_num)
                AuthView.worker_pk += str(worker)
                if worker:
                    data = {}
                    stores = Store.objects.filter(worker=worker)
                    for store in stores:
                        data[store.pk] = store.title
                    return JsonResponse(data)
                    # return Response(data) раскоментировать если захочется увидеть записью а не цифрами
            except Worker.DoesNotExist:
                return Response('Проверьте правильность номера')
        else:
            return Response('У вас нет прав доступа к этой информации')

    def post(self, request,store_pk,latitude, longtitude, phone_num):
        print(store_pk)
        if permission_classes:
            try:
                worker = Worker.objects.get(phone_number=phone_num)
                if worker:
                    visits = Visit.objects.create(worker_id=worker.id,store_id=int(store_pk),latitude=latitude,longitude=longtitude,data_time=datetime.datetime.now())
                    last_visit = Visit.objects.filter(worker=worker).order_by('-data_time').first()
                    return Response({'pk': last_visit.pk, 'data_time': last_visit.data_time})
            except Worker.DoesNotExist:
                return Response('Проверьте правильность номера')
        else:
            return Response('У вас нет прав доступа к этой информации')















'''Пример запроса к AuthView.get'''
# GET http://127.0.0.1:8000/auth/89164554353/
# Content-Type: application/json
# Authorization: Token d0d8cde910889d75d0440342dc11b0711bd1e317

#
# def post(self, request, store_pk, latitude, longtitude, phone_num):
#     print(store_pk)
#     if permission_classes:
#         try:
#             worker = Worker.objects.get(phone_number=phone_num)
#             if worker:
#                 visits = Visit.objects.create(worker_id=worker.id, store_id=int(store_pk), latitude=latitude,
#                                               longitude=longtitude, data_time=datetime.datetime.now())
#                 print(worker)
#                 last_visit = Visit.objects.filter(worker=worker).order_by('-data_time').first()
#                 return Response(last_visit.pk)
#         except Worker.DoesNotExist:
#             return Response('Проверьте правильность номера')
#     else:
#         return Response('У вас нет прав доступа к этой информации')