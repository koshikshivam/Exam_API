from django.db import models
from django.contrib.auth.models import User







class QuizCategory(models.Model):
    category = models.CharField(max_length=100)
    
    def __str__(self):
        return self.category
    
    
    
class Teacher(models.Model):
    name = models.ForeignKey(User,on_delete=models.CASCADE)
    subject = models.ForeignKey(QuizCategory,on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.name
   



class Quiz(models.Model):
    quiz_creator = models.ForeignKey(User,on_delete=models.CASCADE)
    Select_subject = models.ForeignKey(QuizCategory,on_delete=models.CASCADE)
    Ques = models.CharField(max_length=100)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    
    
    
    
    def __str__(self):
        return self.Ques







class submit_your_answers_here(models.Model):
    question = models.OneToOneField(Quiz,on_delete=models.CASCADE)
    answer = models.CharField(max_length=100)
    submitted_by = models.CharField(max_length=100)
    





class Solutions(models.Model):
    solutions_given_by = models.ForeignKey(User,on_delete=models.CASCADE)
    question = models.ForeignKey(Quiz,on_delete=models.CASCADE)
    solutions = models.CharField(max_length=100)
    previous = models.CharField(max_length=100)
    
    
    
    
    
    def __str__(self):
        return self.solutions
    



    



