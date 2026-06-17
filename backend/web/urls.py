from tkinter.font import names

from django.urls import path
from  rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from web.views.index import index

urlpatterns = [
    path('api/token/',TokenObtainPairView.as_view(),name='token_obtian_pair'),
    path('api/token/refresh/',TokenRefreshView.as_view(),name='token_refresh'),
    path('',index),
]