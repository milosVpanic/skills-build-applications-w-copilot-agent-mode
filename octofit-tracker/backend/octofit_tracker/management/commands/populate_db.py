from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.conf import settings
from pymongo import MongoClient
from datetime import timedelta
from bson import ObjectId

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activities, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Connect to MongoDB
        client = MongoClient(settings.DATABASES['default']['HOST'], settings.DATABASES['default']['PORT'])
        db = client[settings.DATABASES['default']['NAME']]

        # Drop existing collections
        db.users.drop()
        db.teams.drop()
        db.activities.drop()
        db.leaderboard.drop()
        db.workouts.drop()

        # Create users
        users = [
            {"_id": ObjectId(), "username": "thundergod", "email": "thundergod@mhigh.edu", "password": "thundergodpassword"},
            {"_id": ObjectId(), "username": "metalgeek", "email": "metalgeek@mhigh.edu", "password": "metalgeekpassword"},
            {"_id": ObjectId(), "username": "zerocool", "email": "zerocool@mhigh.edu", "password": "zerocoolpassword"},
            {"_id": ObjectId(), "username": "crashoverride", "email": "crashoverride@mhigh.edu", "password": "crashoverridepassword"},
            {"_id": ObjectId(), "username": "sleeptoken", "email": "sleeptoken@mhigh.edu", "password": "sleeptokenpassword"},
        ]
        db.users.insert_many(users)

        # Create teams
        blue_team = {"_id": ObjectId(), "name": "Blue Team"}
        gold_team = {"_id": ObjectId(), "name": "Gold Team"}
        db.teams.insert_many([blue_team, gold_team])

        # Assign users to teams
        team_memberships = [
            {"team_id": blue_team["_id"], "user_id": users[0]["_id"]},
            {"team_id": gold_team["_id"], "user_id": users[1]["_id"]},
            {"team_id": blue_team["_id"], "user_id": users[2]["_id"]},
            {"team_id": gold_team["_id"], "user_id": users[3]["_id"]},
            {"team_id": blue_team["_id"], "user_id": users[4]["_id"]},
        ]
        db.teams_members.insert_many(team_memberships)

        # Create activities
        activities = [
            {"_id": ObjectId(), "user_id": users[0]["_id"], "activity_type": "Cycling", "duration": timedelta(hours=1)},
            {"_id": ObjectId(), "user_id": users[1]["_id"], "activity_type": "Crossfit", "duration": timedelta(hours=2)},
            {"_id": ObjectId(), "user_id": users[2]["_id"], "activity_type": "Running", "duration": timedelta(hours=1, minutes=30)},
            {"_id": ObjectId(), "user_id": users[3]["_id"], "activity_type": "Strength", "duration": timedelta(minutes=30)},
            {"_id": ObjectId(), "user_id": users[4]["_id"], "activity_type": "Swimming", "duration": timedelta(hours=1, minutes=15)},
        ]
        db.activities.insert_many(activities)

        # Create leaderboard entries
        leaderboard = [
            {"_id": ObjectId(), "user_id": users[0]["_id"], "score": 100},
            {"_id": ObjectId(), "user_id": users[1]["_id"], "score": 95},
            {"_id": ObjectId(), "user_id": users[2]["_id"], "score": 90},
            {"_id": ObjectId(), "user_id": users[3]["_id"], "score": 85},
            {"_id": ObjectId(), "user_id": users[4]["_id"], "score": 80},
        ]
        db.leaderboard.insert_many(leaderboard)

        # Create workouts
        workouts = [
            {"_id": ObjectId(), "name": "Cycling Training", "description": "Training for a road cycling event"},
            {"_id": ObjectId(), "name": "Crossfit", "description": "Training for a crossfit competition"},
            {"_id": ObjectId(), "name": "Running Training", "description": "Training for a marathon"},
            {"_id": ObjectId(), "name": "Strength Training", "description": "Training for strength"},
            {"_id": ObjectId(), "name": "Swimming Training", "description": "Training for a swimming competition"},
        ]
        db.workouts.insert_many(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
