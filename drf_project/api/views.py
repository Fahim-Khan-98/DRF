from django.shortcuts import render
from api.models import Company,Employee
from api.serializers import companySerializer,EmployeeSerializer
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response



# Create your views here.
class companyViewsets(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = companySerializer

    @action(detail=True,methods=['get'])
    def employees(self,request,pk=None):   
        try:                
            company=Company.objects.get(pk=pk)
            emps=Employee.objects.filter(company=company)
            emps_serializer=EmployeeSerializer(emps,many=True,context={'request':request})
            return Response(emps_serializer.data)
        except Exception as e:
            print(e)
            return Response({
                'message':'Company might not exists !! Error'
            })

    # @action(detail=True,methods=['GET'])
    # def employees(self,request,pk=None):
    #     try:
    #         print(pk)
    #         company = company.objects.get(pk=pk)
            
    #         emps = Employee.objects.filter(company=company)
    #         emp_serializers = EmployeeSerializer(emps,many=True,context={'request':request})
    #     except Exception as e:
    #         print(e)
    #         return Response({
    #             'message' : 'THERE WAS AN ERROR!!!'
    #         }) 

    #     return Response(emp_serializers.data)


class EmployeeViewSets(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer