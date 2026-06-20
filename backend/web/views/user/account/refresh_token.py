from rest_framework.views import APIView
from rest_framework.response import Response

from backend import settings


class RefreshTokenView(APIView):
    def post(self, request):
        try:
            refresh_token = request.data['refresh_token']
            if not refresh_token:
                return Response({
                    'result':'Refresh Token 不存在',
                }, status=401)
            refresh=RefreshTokenView(refresh_token)#如果refresh token过期了/不合法会报异常
            if settings.SIMPLE_JWT['ROTATE_REFRESH_TOKEN']:
                refresh.set_jti()#刷新为有效
                response = Response({
                    'result': 'success',
                    'access': str(refresh.access_token),
                })
                response.set_cookie(
                    key='refresh_token',
                    value=str(refresh),  # refresh返回的是refresh，refresh.access_token返回access，
                    httponly=True,
                    samesite='Lax',
                    secure=True,
                    max_age=86400 * 7,  # 七天内有效
                )
                return response
            return Response({
                'result': 'success',
                'access': str(refresh.access_token),
            })
        except:
            return Response({
                'result':"refresh token 过期了",
            },status=401)