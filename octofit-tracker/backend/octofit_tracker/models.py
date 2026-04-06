
from djongo import models

class Team(models.Model):
	name = models.CharField(max_length=100, unique=True)
	def __str__(self):
		return self.name

class User(models.Model):
	email = models.EmailField(unique=True)
	name = models.CharField(max_length=100)
	team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='members')
	def __str__(self):
		return self.email

class Activity(models.Model):
	name = models.CharField(max_length=100)
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='activities')
	duration = models.IntegerField()  # in minutes
	date = models.DateField()
	def __str__(self):
		return f"{self.name} - {self.user.email}"

class Workout(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField()
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='workouts')
	date = models.DateField()
	def __str__(self):
		return f"{self.name} - {self.user.email}"

class Leaderboard(models.Model):
	name = models.CharField(max_length=100)
	team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='leaderboards')
	score = models.IntegerField()
	def __str__(self):
		return f"{self.name} - {self.team.name}"