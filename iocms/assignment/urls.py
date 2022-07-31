from django.urls import path 
from .views import (
                    AssignmentListView,
                    AssignmentCreateView, 
                    AssignmentDetailView,
)
app_name = 'assignment'

urlpatterns = [
    path('api/class/<int:class_pk>/list/', AssignmentListView.as_view(), name = 'list'),
    path('api/class/<int:class_pk>/create/', AssignmentCreateView.as_view(), name = 'create'),
    path('api/class/list/<int:pk>/', AssignmentDetailView.as_view(), name = 'details'),
    # path('api/<int:pk>/submit/', AssignmentSubmitView.as_view(), name = 'submit'),
    # path('api/<int:class_pk>/submitted-assignment-list/', SubbmittedAssignmentView.as_view(), name='submitted-list')
]
