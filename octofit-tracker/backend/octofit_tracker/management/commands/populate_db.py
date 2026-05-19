from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete existing data in correct order to avoid FK issues
        Leaderboard.objects.all().delete()
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        # Create Teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create Users
        users = [
            User(name='Tony Stark', email='tony@marvel.com', team=marvel),
            User(name='Steve Rogers', email='steve@marvel.com', team=marvel),
            User(name='Bruce Wayne', email='bruce@dc.com', team=dc),
            User(name='Clark Kent', email='clark@dc.com', team=dc),
        ]
        User.objects.bulk_create(users)

        # Refresh users from DB to get PKs
        users = list(User.objects.all().order_by('name'))

        # Create Activities
        activities = [
            Activity(user=users[0], type='Run', duration=30, calories=300),
            Activity(user=users[1], type='Swim', duration=45, calories=400),
            Activity(user=users[2], type='Bike', duration=60, calories=500),
            Activity(user=users[3], type='Yoga', duration=50, calories=200),
        ]
        Activity.objects.bulk_create(activities)

        # Create Workouts
        workouts = [
            Workout(name='Morning Cardio', description='Cardio for all'),
            Workout(name='Strength Training', description='Strength for all'),
        ]
        for workout in workouts:
            workout.save()

        # Create Leaderboard
        Leaderboard.objects.create(user=users[0], score=1000)
        Leaderboard.objects.create(user=users[1], score=900)
        Leaderboard.objects.create(user=users[2], score=1100)
        Leaderboard.objects.create(user=users[3], score=950)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
