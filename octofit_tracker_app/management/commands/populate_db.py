from django.core.management.base import BaseCommand
from octofit_tracker_app.models import User, Team, Activity, Leaderboard, Workout
from datetime import timedelta
from django.conf import settings
from pymongo import MongoClient
from django.db import connection

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activities, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        try:
            # Get MongoDB connection
            client = MongoClient(settings.DATABASES['default']['HOST'], 
                               settings.DATABASES['default']['PORT'])
            db = client[settings.DATABASES['default']['NAME']]
            
            # Drop all collections
            self.stdout.write("Clearing existing data...")
            collections = ['users', 'teams', 'activities', 'leaderboard', 'workouts', 'teams_members']
            for collection in collections:
                if collection in db.list_collection_names():
                    db[collection].drop()
            
            # Create users directly in MongoDB
            self.stdout.write("Creating users...")
            users_data = [
                {'username': 'thundergod', 'email': 'thundergod@mhigh.edu', 'password': 'thundergodpassword'},
                {'username': 'metalgeek', 'email': 'metalgeek@mhigh.edu', 'password': 'metalgeekpassword'},
                {'username': 'zerocool', 'email': 'zerocool@mhigh.edu', 'password': 'zerocoolpassword'},
                {'username': 'crashoverride', 'email': 'crashoverride@mhigh.edu', 'password': 'crashoverridepassword'},
                {'username': 'sleeptoken', 'email': 'sleeptoken@mhigh.edu', 'password': 'sleeptokenpassword'},
            ]
            
            user_ids = []
            for data in users_data:
                result = db.users.insert_one(data)
                user_ids.append(result.inserted_id)
                self.stdout.write(f"Created user: {data['username']}")

            # Create teams
            self.stdout.write("Creating teams...")
            blue_team = db.teams.insert_one({'name': 'Blue Team'})
            gold_team = db.teams.insert_one({'name': 'Gold Team'})

            # Create team memberships
            for i, user_id in enumerate(user_ids):
                team_id = blue_team.inserted_id if i % 2 == 0 else gold_team.inserted_id
                db.teams_members.insert_one({
                    'team_id': team_id,
                    'user_id': user_id
                })
            self.stdout.write("Created teams and assigned members")

            # Create activities
            self.stdout.write("Creating activities...")
            activities_data = [
                {'user_id': user_ids[0], 'activity_type': 'Cycling', 'duration': str(timedelta(hours=1))},
                {'user_id': user_ids[1], 'activity_type': 'Crossfit', 'duration': str(timedelta(hours=2))},
                {'user_id': user_ids[2], 'activity_type': 'Running', 'duration': str(timedelta(hours=1, minutes=30))},
                {'user_id': user_ids[3], 'activity_type': 'Strength', 'duration': str(timedelta(minutes=30))},
                {'user_id': user_ids[4], 'activity_type': 'Swimming', 'duration': str(timedelta(hours=1, minutes=15))},
            ]
            db.activities.insert_many(activities_data)

            # Create leaderboard entries
            self.stdout.write("Creating leaderboard entries...")
            leaderboard_data = []
            for i, user_id in enumerate(user_ids):
                score = 100 - (i * 5)  # Decreasing scores: 100, 95, 90, 85, 80
                leaderboard_data.append({'user_id': user_id, 'score': score})
            db.leaderboard.insert_many(leaderboard_data)

            # Create workouts
            self.stdout.write("Creating workouts...")
            workouts_data = [
                {'name': 'Cycling Training', 'description': 'Training for a road cycling event'},
                {'name': 'Crossfit', 'description': 'Training for a crossfit competition'},
                {'name': 'Running Training', 'description': 'Training for a marathon'},
                {'name': 'Strength Training', 'description': 'Training for strength'},
                {'name': 'Swimming Training', 'description': 'Training for a swimming competition'},
            ]
            db.workouts.insert_many(workouts_data)

            self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error populating database: {str(e)}'))
