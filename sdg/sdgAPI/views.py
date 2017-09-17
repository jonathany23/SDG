from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.viewsets import ModelViewSet
from rest_framework import generics

from . import models as mod
from . import serializers as ser

# Create your views here.
#def index(request):
#    return HttpResponse("Hello, world. You're at the polls index.")


class GoalViewSet(ModelViewSet):
    queryset = mod.Goal.objects.all()
    serializer_class = ser.GoalSerializer

class TargetViewSet(ModelViewSet):
    queryset = mod.Target.objects.all()
    serializer_class = ser.TargetSerializer

class TargetDescViewSet(ModelViewSet):
    queryset = mod.TargetDesc.objects.all()
    serializer_class = ser.TargetDescSerializer

class IndicatorViewSet(ModelViewSet):
    queryset = mod.Indicator.objects.all()
    serializer_class = ser.IndicatorSerializer

class IndicatorDescViewSet(ModelViewSet):
    queryset = mod.IndicatorDesc.objects.all()
    serializer_class = ser.IndicatorDescSerializer


class IndicatorsIdViewSet(generics.ListAPIView):
    serializer_class = ser.IndicatorDescSerializer

    def get_queryset(self):
        series_code = self.kwargs['series_code']
        indicator_desc = mod.IndicatorDesc.objects.filter(series_code=series_code)
        return indicator_desc

class AreaIdViewSet(generics.ListAPIView):
    serializer_class = ser.IndicatorDescSerializer

    def get_queryset(self):
        series_code = self.kwargs['series_code']
        reference_area_code = self.kwargs['reference_area_code']
        indicator_desc = mod.IndicatorDesc.objects.filter(series_code=series_code,reference_area_code=reference_area_code)
        return indicator_desc

class TimePeriodViewSet(generics.ListAPIView):
    serializer_class = ser.IndicatorDescSerializer

    def get_queryset(self):
        series_code = self.kwargs['series_code']
        time_period = self.kwargs['time_period']
        indicator_desc = mod.IndicatorDesc.objects.filter(series_code=series_code,time_period=time_period)
        return indicator_desc

class SexViewSet(generics.ListAPIView):
    serializer_class = ser.IndicatorDescSerializer

    def get_queryset(self):
        series_code = self.kwargs['series_code']
        sex_code = self.kwargs['sex_code']
        indicator_desc = mod.IndicatorDesc.objects.filter(series_code=series_code,sex_code=sex_code)
        return indicator_desc


class TargetsByGoalViewSet(generics.ListAPIView):
    serializer_class = ser.TargetSerializer

    def get_queryset(self):
        id_goal = self.kwargs['id_goal']
        target = mod.Target.objects.filter(id_goal=id_goal)
        return target

class DescByTargetViewSet(generics.ListAPIView):
    serializer_class = ser.TargetDescSerializer

    def get_queryset(self):
        target_id = self.kwargs['target_id']
        targetDesc = mod.TargetDesc.objects.filter(id_meta=target_id)
        return targetDesc

class IndicatorByTargetDescViewSet(generics.ListAPIView):
    serializer_class = ser.IndicatorSerializer

    def get_queryset(self):
        target_desc_id = self.kwargs['target_desc_id']
        indicator = mod.Indicator.objects.filter(id_meta_desc=target_desc_id)
        return indicator