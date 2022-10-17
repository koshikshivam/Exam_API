from rest_framework import serializers
from .models import QuizCategory,Teacher,Quiz,submit_your_answers_here,Solutions
from django.contrib.auth.models import User





class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','email','password']



class QuizCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizCategory
        fields = ['category']
        
        
class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['name','subject']
        
        
class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = "__all__"
        
class submit_your_answersSerializer(serializers.ModelSerializer):
    class Meta:
        model = submit_your_answers_here
        fields = ['question','answer','submitted_by']
        
class  solutionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solutions
        fields = ['solutions_given_by', 'question','solutions']