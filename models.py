from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)


    #models go below here, where we define our patterns
    #essentially our schema, what data should look like


class Pet(db.Model):
    __tablename__ = "pets"

    def __repr__(self):
        p = self
        return f"<Pet id={pet.id} name={p.name} species={p.species} hunger={p.hunger}>"

    id = db.Column(db.Integer,
                    primary_key=True,
                    autoincrement=True)
    name = db.Column(db.String(50),
                    nullable=False,
                    unique=True)
    species = db.Column(db.String(30), nullable=True)
    hunger = db.Column(db.Integer, nullable=False, default=20)

    def greet(self):
        return f"Hi I am {self.name}, the {self.species}"