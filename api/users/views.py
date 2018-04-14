from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from rest_framework_jwt.views import ObtainJSONWebToken, jwt_response_payload_handler


class LoginAPIView(ObtainJSONWebToken):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.object.get('token'))
