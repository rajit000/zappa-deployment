from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes,authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import request, status as stus
from rest_framework.response import Response
from rest_framework.exceptions import APIException
from datetime import datetime
# from models import models
# Create your views here.
from .queries import *
from .models import *
from .serializers import *


@api_view(['POST'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def StudentList_f(request):
    try:
        data = StudentList_q()
        print('1111111')
        Count = StudentListCount_q()
        print('22222222222')
        if data:
            json_data = {
                'status_code': 200,
                'count': Count,
                'data': replace_null_with_empty_string_many(data),
                'message': 'Data found Successfully'
            }
            return Response(json_data,status=stus.HTTP_200_OK)
        else:
            json_data = {
                'status_code': 200,
                'count': 0,
                'data': [],
                'message': 'Data Not found Successfully'
            }
            return Response(json_data,status=stus.HTTP_200_OK)
            
    except Exception as e:
        print("Error --------:", e)
        json_data = {
            'status_code': 400,
            'status': 'Fail',
            'Reason': e,
            'Remark': 'landed in exception',
        }
        return Exception(json_data,status=stus.HTTP_500_INTERNAL_SERVER_ERROR)
    
@api_view(['POST'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def StudentDetail_f(request):
    try:
        serializer = StudentDetail_s(data=request.data)
        if serializer.is_valid():
            StudentUUID=serializer.data['StudentUUID']
            data = StudentDetail_q(StudentUUID)
            if data:
                json_data = {
                    'status_code': 200,
                    'status': 'Success',
                    'data': replace_null_with_empty_string(data),
                    'message': 'Data found Successfully'
                }
                return Response(json_data,status=stus.HTTP_200_OK)
            else:
                json_data = {
                    'status_code': 200,
                    'status': 'Success',
                    'data': '',
                    'message': 'Data Not found Successfully'
                }
                return Response(json_data,status=stus.HTTP_200_OK)
        else:
            json_data = {
                'status_code': 300,
                'status': 'Fail',
                'Reason': serializer.errors,
                'Remark': 'Send valid data'
            }
            return Response(json_data, status=stus.HTTP_300_MULTIPLE_CHOICES)
    except Exception as e:
        print("Error --------:", e)
        json_data = {
            'status_code': 400,
            'status': 'Fail',
            'Reason': e,
            'Remark': 'landed in exception',
        }
        return Exception(json_data,status=stus.HTTP_500_INTERNAL_SERVER_ERROR)
    
@api_view(['POST'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def StudentDetailDelete_f(request):
    try:
        serializer = StudentDetailDelete_s(data=request.data)

        if serializer.is_valid():
            StudentUUID=serializer.data['StudentUUID']
            data = StudentDetailDelete_q(StudentUUID)
            if data:
                json_data = {
                    'status_code': 200,
                    'status': 'Success',
                    'data': '',
                    'message': 'Data Deleted Successfully'
                }
                return Response(json_data,status=stus.HTTP_200_OK)
            else:
                json_data = {
                    'status_code': 200,
                    'status': 'Success',
                    'data': '',
                    'message': 'Data Not Deleted Successfully'
                }
                return Response(json_data,status=stus.HTTP_200_OK)
        else:
            json_data = {
                'status_code': 300,
                'status': 'Fail',
                'Reason': serializer.errors,
                'Remark': 'Send valid data'
            }
            return Response(json_data, status=stus.HTTP_300_MULTIPLE_CHOICES)
    except Exception as e:
        print("Error --------:", e)
        json_data = {
            'status_code': 400,
            'status': 'Fail',
            'Reason': e,
            'Remark': 'landed in exception',
        }
        return Exception(json_data,status=stus.HTTP_500_INTERNAL_SERVER_ERROR)
    
    
@api_view(['POST'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def StudentDetailsInsert_f(request):
    try:
        serializer = StudentDetailInsert_s(data=request.data)

        if serializer.is_valid():
            data = {
                'FirstName': serializer.data['FirstName'] if serializer.data['FirstName'] else None,
                'LastName': serializer.data['LastName'] if serializer.data['LastName'] else None,
                'Class': serializer.data['Class'] if serializer.data['Class'] else None,
                'Section': serializer.data['Section'] if serializer.data['Section'] else None,
                'City': serializer.data['City'] if serializer.data['City'] else None,
                'District': serializer.data['District'] if serializer.data['District'] else None,
                'State': serializer.data['State'] if serializer.data['State'] else None,
                'Pincode': serializer.data['Pincode'] if serializer.data['Pincode'] else None,
                'About': serializer.data['About'] if serializer.data['About'] else None,
                'IsDeleted':'0',
                'CreatedAt': datetime.now(),
                'CreatedBy':'system',
                'UpdatedAt': datetime.now(),
                'UpdatedBy': 'system'
            }
            Data = StudentDetailInsert_q(list(data.values()))
            if Data:
                json_data = {
                    'status_code': 200,
                    'status': 'Success',
                    'data': '',
                    'message': 'Data Saved Successfully'
                }
                return Response(json_data,status=stus.HTTP_200_OK)
            else:
                json_data = {
                    'status_code': 200,
                    'status': 'Success',
                    'data': '',
                    'message': 'Data Not Saved'
                }
                return Response(json_data,status=stus.HTTP_200_OK)
        else:
            json_data = {
                'status_code': 300,
                'status': 'Fail',
                'Reason': serializer.errors,
                'Remark': 'Send valid data'
            }
            return Response(json_data, status=stus.HTTP_300_MULTIPLE_CHOICES)
    except Exception as e:
        print("Error --------:", e)
        json_data = {
            'status_code': 400,
            'status': 'Fail',
            'Reason': e,
            'Remark': 'landed in exception',
        }
        return Exception(json_data,status=stus.HTTP_500_INTERNAL_SERVER_ERROR)

    
@api_view(['POST'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def StudentDetailsUpdate_f(request):
    try:
        serializer = StudentDetailsUpdate_s(data=request.data)

        if serializer.is_valid():
            StudentUUID = serializer.data['StudentUUID']
            OldData = OldStudentData_q(StudentUUID)
            data = {
                'FirstName': serializer.data['FirstName'] if serializer.data['FirstName'] else OldData['FirstName'],
                'LastName': serializer.data['LastName'] if serializer.data['LastName'] else OldData['LastName'],
                'Class': serializer.data['Class'] if serializer.data['Class'] else OldData['Class'],
                'Section': serializer.data['Section'] if serializer.data['Section'] else OldData['Section'],
                'City': serializer.data['City'] if serializer.data['City'] else OldData['City'],
                'District': serializer.data['District'] if serializer.data['District'] else OldData['District'],
                'State': serializer.data['State'] if serializer.data['State'] else OldData['State'],
                'Pincode': serializer.data['Pincode'] if serializer.data['Pincode'] else OldData['Pincode'],
                'About': serializer.data['About'] if serializer.data['About'] else OldData['About'],
                'UpdatedAt': datetime.now(),
                'UpdatedBy': 'system',
                'StudentUUID' : serializer.data['StudentUUID']
            }
            
            Data = StudentDetailsUpdate_q(list(data.values()))
            if Data:
                json_data = {
                    'status_code': 200,
                    'status': 'Success',
                    'data': '',
                    'message': 'Data updated Successfully'
                }
                return Response(json_data,status=stus.HTTP_200_OK)
            else:
                json_data = {
                    'status_code': 200,
                    'status': 'Success',
                    'data': '',
                    'message': 'Data Not Updated'
                }
                return Response(json_data,status=stus.HTTP_200_OK)
        else:
            json_data = {
                'status_code': 300,
                'status': 'Fail',
                'Reason': serializer.errors,
                'Remark': 'Send valid data'
            }
            return Response(json_data, status=stus.HTTP_300_MULTIPLE_CHOICES)
    except Exception as e:
        print("Error --------:", e)
        json_data = {
            'status_code': 400,
            'status': 'Fail',
            'Reason': e,
            'Remark': 'landed in exception',
        }
        return Exception(json_data,status=stus.HTTP_500_INTERNAL_SERVER_ERROR)
    
