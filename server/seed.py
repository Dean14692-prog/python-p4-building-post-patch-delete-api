#!/usr/bin/env python3

from random import choice as rc, randint

from faker import Faker

from app import app
from models import db, User, Review, Game

fake = Faker()

with app.app_context():
    
    print("Deleting all records...")
    Review.query.delete()
    User.query.delete()
    Game.query.delete()

    print("Creating users...")
    users = []
    for i in range(5):
        user = User(name=fake.name())
        users.append(user)
    db.session.add_all(users)

    print("Creating games...")
    games = []
    genres = ['Action', 'Adventure', 'RPG', 'Strategy', 'Sports']
    platforms = ['PC', 'PlayStation', 'Xbox', 'Nintendo Switch']
    for i in range(10):
        game = Game(
            title=fake.unique.word(),
            genre=rc(genres),
            platform=rc(platforms),
            price=randint(10, 60)
        )
        games.append(game)
    db.session.add_all(games)

    print("Creating reviews...")
    reviews = []
    for i in range(25):
        review = Review(
            score=randint(1, 10),
            comment=fake.sentence(),
            game_id=randint(1, 10),
            user_id=randint(1, 5)
        )
        reviews.append(review)
    db.session.add_all(reviews)

    db.session.commit()
    print("Complete.")