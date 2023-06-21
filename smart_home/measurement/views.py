from rest_framework.decorators import api_view
from rest_framework.response import Response


# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
@api_view(['GET'])
def demo(request):
    data = {'message': 'Hello'}
    return Response(data)
