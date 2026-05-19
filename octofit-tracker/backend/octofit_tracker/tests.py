from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class ModelTests(TestCase):
    def setUp(self):
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')
        tony = User.objects.create(name='Tony Stark', email='tony@marvel.com', team=marvel)
        bruce = User.objects.create(name='Bruce Wayne', email='bruce@dc.com', team=dc)
        Activity.objects.create(user=tony, type='Run', duration=30, calories=300)
        Workout.objects.create(name='Morning Cardio', description='Cardio for all')
        Leaderboard.objects.create(user=tony, score=1000)

    def test_user_team(self):
        tony = User.objects.get(name='Tony Stark')
        self.assertEqual(tony.team.name, 'Marvel')

    def test_activity(self):
        activity = Activity.objects.get(type='Run')
        self.assertEqual(activity.calories, 300)

    def test_leaderboard(self):
        entry = Leaderboard.objects.get(score=1000)
        self.assertEqual(entry.user.name, 'Tony Stark')
