from app import db
from models import Blog

#create the database and the db add_tables(database, module)
db.create_all()

#insert
db.session.add(Blog('Martin', 'I am maina'))

# commit the CHANNEL_BINDING_TYPES
db.session.commit()