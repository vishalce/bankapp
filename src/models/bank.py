from . import db


class Bank(db.Model):
    __tablename__ = 'banks'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(49), nullable=False, index=True)
    branches = db.relationship('Branch', backref='banks', lazy=True)

    def __init__(self, data):
        self.id = data.get('id')
        self.name = data.get('name')

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self, data):
        for key, item in data.items():
            setattr(self, key, item)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_all_banks():
        return Bank.query.all()

    @staticmethod
    def get_one_bank(id):
        return Bank.query.get(id)

    @staticmethod
    def get_bank(bank):
        return Bank.query.filter_by(name=bank).first()

    def __repr(self):
        return '<{}:{}>'.format(self.id, self.name)
