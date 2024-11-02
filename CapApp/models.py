import uuid
from django.db import models


class Vocabulary(models.Model):
    _id = models.CharField(max_length=100, primary_key=True, default=uuid.uuid4)
    word = models.CharField(max_length=100)
    vietnamese = models.CharField(max_length=100)
    definition = models.TextField()
    examples = models.JSONField()
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.word

# class User(models.Model):
#     username = models.CharField(max_length=100, unique=True)
#     phone = models.CharField(max_length=15, unique=True)
#     password = models.CharField(max_length=128)

#     def __str__(self):
#         return self.username

# class Topic(models.Model):  
#     category = models.CharField(max_length=100, unique=True)  
#     vietnamese = models.CharField(max_length=100)  

#     def __str__(self):  
#         return self.category
    
# class UserProgress(models.Model):  
#     username = models.ForeignKey(User, on_delete=models.CASCADE)  

#     def __str__(self):  
#         return self.user_name  

# class Progress(models.Model):  
#     user = models.ForeignKey(UserProgress, on_delete=models.CASCADE)  
#     date = models.DateField()  
#     time_study = models.CharField(max_length=10)  

#     def __str__(self):  
#         return f"{self.user.user_name} - {self.date} - {self.time_study}"  

# class Game(models.Model):  
#     name = models.CharField(max_length=100)  
#     definition = models.TextField()  
#     difficulty = models.CharField(max_length=50)  
#     age_range = models.CharField(max_length=20)  

#     def __str__(self):  
#         return self.name 

# class GamePlayed(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     game_name = models.ForeignKey(Game, on_delete=models.CASCADE)

#     def __str__(self):
#         return f"{self.user} - {self.game_name}"

# class Score(models.Model):
#     game_played = models.ForeignKey(GamePlayed, related_name='scores', on_delete=models.CASCADE)
#     score = models.CharField(max_length=10)

#     def __str__(self):
#         return self.score
    

