from django.conf.urls import include, url
from rest_framework.routers import SimpleRouter

from . import views

router = SimpleRouter()
rest_base_url = "api/rest/"
router.register(rest_base_url + "goal", views.GoalViewSet)
router.register(rest_base_url + "target", views.TargetViewSet)
router.register(rest_base_url + "targetDesc", views.TargetDescViewSet)
router.register(rest_base_url + "indicator", views.IndicatorViewSet)
router.register(rest_base_url + "indicatorDesc", views.IndicatorDescViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),

    url('^api/rest/targetsByGoal/(?P<id_goal>[0-9]+)/',views.TargetsByGoalViewSet.as_view()),
    url('^api/rest/descByTarget/(?P<target_id>[0-9]+)/',views.DescByTargetViewSet.as_view()),
    url('^api/rest/indicatorByTargetDesc/(?P<target_desc_id>[0-9]+)/',views.IndicatorByTargetDescViewSet.as_view()),

    url('^api/rest/indicatorDescById/(?P<series_code>[A-Z0-9_]+)/',views.IndicatorsIdViewSet.as_view()),
    url('^api/rest/indicatorArea/(?P<series_code>[A-Z0-9_]+)/(?P<reference_area_code>[A-Z_]+)',views.AreaIdViewSet.as_view()),
    url('^api/rest/indicatorTime/(?P<series_code>[A-Z0-9_]+)/(?P<time_period>[0-9]+)',views.TimePeriodViewSet.as_view()),
    url('^api/rest/indicatorSex/(?P<series_code>[A-Z0-9_]+)/(?P<sex_code>[A-Z]+)',views.SexViewSet.as_view()),
]