from rest_framework import mixins, viewsets


class ListCreateDestroyViewSet(viewsets.GenericViewSet,
                               mixins.CreateModelMixin,
                               mixins.ListModelMixin,
                               mixins.DestroyModelMixin):
    pass
