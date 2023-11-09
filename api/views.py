from django.shortcuts import render

from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CandidatoSerializer, EmpresaSerializer
from .models import CandidatoModel, EmpresaModel
import pandas as pd
import os

# Create your views here.

class CandidatoViewSet(viewsets.ModelViewSet):
    queryset = CandidatoModel.objects.all()
    serializer_class = CandidatoSerializer


class EmpresaViewSet(viewsets.ModelViewSet):
    queryset = EmpresaModel.objects.all()
    serializer_class = EmpresaSerializer


class ExcelExportAPIView(APIView):
    """
    Generate Excel File
    """
    
    def get(self, request):
        try: 
            # get data
            candidatos = CandidatoModel.objects.all()
            empresas = EmpresaModel.objects.all()

            # check if candidatos is empty
            # create dataFrames
            if len(candidatos) > 0: 
                df1 = pd.DataFrame.from_records(candidatos.values(), exclude=['created_at'])
            else: 
                df1 = pd.DataFrame({"Message": ["Candidatos List is Empty"]})

            # check if candidatos is empty
            # create dataFrame
            if len(empresas) > 0: 
                df2 = pd.DataFrame.from_records(empresas.values(), exclude=['created_at'])
            else:
                df2 = pd.DataFrame({"Message": ["Empresas List is Empty"]})

            # check is "static" directory exists
            if os.path.isdir('static'):
                # export the dataFrame to excel file
                with pd.ExcelWriter('static/ntizu-export.xlsx') as excel_writer:
                    df1.to_excel(excel_writer, sheet_name='Candidatos', index=False)
                    df2.to_excel(excel_writer, sheet_name='Empresas', index=False)
            else:
                # create "static" directory
                os.makedirs('static')
                # export the dataFrame to excel file
                # df.to_excel('ntizuexport.xlsx', index=False)
                with pd.ExcelWriter('static/ntizu-export.xlsx') as excel_writer:
                    df1.to_excel(excel_writer, sheet_name='Candidatos', index=False)
                    df1.to_excel(excel_writer, sheet_name='Empresas', index=False)

            return Response({
                'status':True,
                'message': 'Excel file created'
            }, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({
                'status':False,
                'message': 'Failed to create excel'
            }, status=status.HTTP_400_BAD_REQUEST)