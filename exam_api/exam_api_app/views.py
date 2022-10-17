from rest_framework import views
from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet
from .models import QuizCategory,Teacher,Quiz,submit_your_answers_here,Solutions
from django.contrib.auth.models import User
from .serializers import QuizCategorySerializer,TeacherSerializer,QuizSerializer,submit_your_answers_here,solutionsSerializer, submit_your_answersSerializer,UserSerializer
from rest_framework.permissions import BasePermission,IsAdminUser,IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework.authentication import BasicAuthentication,BaseAuthentication,SessionAuthentication

class WriteByAdminOnlyPermission(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if request.method == 'GET':
            return True
        if request.method =="POST" or request.method == "PUT"  or request.method == "DELETE":
            if user.is_staff:
                return True
        return False
    



class WriteBySuperUserPermission(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if request.method =="POST" or request.method == "PUT"  or request.method == "DELETE"  or request.method=='GET':
            if user.is_superuser:
                return True
        return False
    






class UserSerializerModelViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class QuizCatagoryModelViewSet(viewsets.ModelViewSet):
    queryset = QuizCategory.objects.all()
    serializer_class = QuizCategorySerializer
    authentication_classes= [SessionAuthentication]
    permission_classes=[WriteByAdminOnlyPermission]
    
    
    
    

class TeacherModelViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    authentication_classes= [SessionAuthentication]
    permission_classes=[WriteByAdminOnlyPermission]
    
    
    
    
    

class QuizModelViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [ IsAuthenticatedOrReadOnly, WriteByAdminOnlyPermission]
    
    

class SubmitAnswersModelViewSet(viewsets.ModelViewSet):
    queryset = submit_your_answers_here.objects.all()
    serializer_class = submit_your_answersSerializer
    
    

class SolutionsModelViewSet(viewsets.ModelViewSet):
    queryset = Solutions.objects.all()
    serializer_class = solutionsSerializer
    authentication_classes= [SessionAuthentication]
    permission_classes=[WriteBySuperUserPermission]
    
    