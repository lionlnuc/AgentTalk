from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from web.models.friend import Friend



class GetListFriendView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        try:
            items_count=int(request.query_params.get('itmes_count',0))
            friend_raw=Friend.objects.filter(
                me__user=request.user,
            ).order_by('-update_time')[items_count:items_count+20]
            friend=[]
            for friend in friend_raw:
                character=friend.character
                author=character.author
                friend.append({
                    'id':friend.id,
                    'character':{
                        'id':character.id,
                        'name':character.name,
                        'profile':character.profile,
                        'photo':character.photo.url,
                        'background_image':character.background_image.url,
                        'author':{
                            'user_id':author.id,
                            'username':author.user.username,
                            'photo':author.photo.url,
                        }
                    }
                })
        except:
            return Response({
                'result': '系统异常，请稍后重试',
            })