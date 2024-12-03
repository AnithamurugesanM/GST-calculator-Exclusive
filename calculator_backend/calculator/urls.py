from django.urls import path
from .views import GSTCalculator
# from django.urls import path
# from .views import GstCalculatorView

urlpatterns = [
    path('calculate/', GSTCalculator.as_view(), name='gst_calculator')
]

# urlpatterns = [
#     path('calculate/', GstCalculatorView.as_view(), name='gst_calculator')
# ]


