from django.urls import path
#from .views import PostList,PostDetail,UserList,UserDetail
'''Django REST Framework has two default routers: SimpleRouter and DefaultRouter.
We will use SimpleRouter but it’s also possible to create custom routers for more
advanced functionality.'''

from .views import UserViewSet,PostViewSet
from rest_framework.routers import SimpleRouter
# urlpatterns=[
#     path('users/',UserList.as_view()),
#     path('users/<int:pk>/',UserDetail.as_view()),
#     path('<int:pk>/',PostDetail.as_view()),
#     path('',PostList.as_view()),
# ]
'''Routers work directly with viewsets to automatically generate URL patterns for us.
Our current posts/urls.py file has four URL patterns: two for blog posts and two for
Chapter 8: Viewsets and Routers 155
users. We can instead adopt a single route for each viewset. So two routes instead of
four URL patterns. That sounds better, right?'''


router = SimpleRouter()
router.register('users/',UserViewSet,basename='users')
router.register('',PostViewSet,basename='posts')

urlpatterns = router.urls
