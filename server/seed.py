from config import app, db
from models import Playlist
from faker import Faker

fake = Faker()

with app.app_context():
    print("Seeding database...")

    
    Playlist.query.delete()


    for _ in range(5):
        playlist = Playlist(
            name=fake.word().capitalize() + " Mix",
            description=fake.sentence()
        )
        db.session.add(playlist)

    db.session.commit()

    print("Seeding complete.")
