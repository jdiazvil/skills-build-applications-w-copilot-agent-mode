from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from datetime import date

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        Leaderboard.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        # Create Teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create Users
        users = [
            User.objects.create(email='ironman@marvel.com', name='Iron Man', team=marvel),
            User.objects.create(email='captain@marvel.com', name='Captain America', team=marvel),
            User.objects.create(email='spiderman@marvel.com', name='Spider-Man', team=marvel),
            User.objects.create(email='batman@dc.com', name='Batman', team=dc),
            User.objects.create(email='superman@dc.com', name='Superman', team=dc),
            User.objects.create(email='wonderwoman@dc.com', name='Wonder Woman', team=dc),
        ]

        # Create Activities
        Activity.objects.create(name='Running', user=users[0], duration=30, date=date.today())
        Activity.objects.create(name='Cycling', user=users[1], duration=45, date=date.today())
        Activity.objects.create(name='Swimming', user=users[2], duration=60, date=date.today())
        Activity.objects.create(name='Yoga', user=users[3], duration=40, date=date.today())
        Activity.objects.create(name='Boxing', user=users[4], duration=50, date=date.today())
        Activity.objects.create(name='Climbing', user=users[5], duration=35, date=date.today())

        # Create Workouts
        Workout.objects.create(name='Push Ups', description='Standard push ups', user=users[0], date=date.today())
        Workout.objects.create(name='Sit Ups', description='Core workout', user=users[1], date=date.today())
        Workout.objects.create(name='Pull Ups', description='Upper body', user=users[2], date=date.today())
        Workout.objects.create(name='Squats', description='Leg workout', user=users[3], date=date.today())
        Workout.objects.create(name='Deadlifts', description='Strength', user=users[4], date=date.today())
        Workout.objects.create(name='Plank', description='Core stability', user=users[5], date=date.today())

        # Create Leaderboards
        Leaderboard.objects.create(name='Top Marvel', team=marvel, score=300)
        Leaderboard.objects.create(name='Top DC', team=dc, score=280)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
