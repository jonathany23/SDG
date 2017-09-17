from . import models as mod
from rest_framework.serializers import ModelSerializer

class GoalSerializer(ModelSerializer):
    class Meta:
        model = mod.Goal
        fields = ('id_goal', 'goal_description')

class TargetSerializer(ModelSerializer):
    class Meta:
        model = mod.Target
        fields = ('id_goal', 'id_meta', 'description')

class TargetDescSerializer(ModelSerializer):
    class Meta:
        model = mod.TargetDesc
        fields = ('id_meta', 'id_meta_desc', 'description')

class IndicatorSerializer(ModelSerializer):
    class Meta:
        model = mod.Indicator
        fields = ('id_meta_desc', 'serie_code', 'description')

class IndicatorDescSerializer(ModelSerializer):
    class Meta:
        model = mod.IndicatorDesc
        fields = ('id_indicator_desc', 'series_code', 'reference_area', 'time_period', 'sex', 'age_group', 'value')