import os
from sqlalchemy.orm import sessionmaker
from faker import Faker
from datetime import datetime, timedelta
from models import Task, create_schema, get_session
from dotenv import load_dotenv

load_dotenv()

def populate_db(session, num_records=100):
    fake = Faker()
    for _ in range(num_records):
        title = fake.sentence(nb_words=4)
        description = fake.text(max_nb_chars=200)
        due_date = fake.date_between(start_date='-30d', end_date='+30d')
        completed = fake.boolean(chance_of_getting_true=50)
        completion_date = due_date + timedelta(days=fake.random_int(min=1, max=10)) if completed else None
        
        task = Task(
            title=title,
            description=description,
            due_date=due_date,
            completed=completed,
            completion_date=completion_date
        )
        session.add(task)
    session.commit()

if __name__ == '__main__':
    create_schema()
    session = get_session()
    populate_db(session)
    print("Database initialized with sample data.")
