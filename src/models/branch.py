from . import db
from .bank import Bank
from marshmallow import fields, Schema


class Branch(db.Model):
    __tablename__ = 'branches'

    ifsc = db.Column(db.String(11), primary_key=True)
    branch = db.Column(db.String(74), nullable=False)
    address = db.Column(db.String(195))
    city = db.Column(db.String(50), nullable=False, index=True)
    district = db.Column(db.String(50), nullable=False)
    state = db.Column(db.String(26), nullable=False)
    bank_id = db.Column(db.Integer, db.ForeignKey('banks.id'))
    bank = db.relationship('Bank', )

    def __init__(self, data):
        self.ifsc = data.get('ifsc')
        self.branch = data.get('branch')
        self.address = data.get('address')
        self.city = data.get('city')
        self.district = data.get('district')
        self.state = data.get('state')
        self.bank_id = data.get('bank_id')

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
    def get_all_branches():
        return Branch.query.all()

    @staticmethod
    def get_one_branch(ifsc):
        return Branch.query.get(ifsc)

    @staticmethod
    def get_branches(bank, city, page, per_page):
        return Branch.query.filter_by(bank_id=bank, city=city).paginate(page=page, per_page=per_page)

    @staticmethod
    def get_branches_with_offset(bank, city, offset, limit):
        return Branch.query.filter_by(bank_id=bank, city=city).offset(offset).limit(limit)

    def __repr(self):
        return '<ifsc {}>'.format(self.ifsc)

    def to_json(self):
        return {
            'ifsc': self.ifsc,
            'bank': self.bank.name,
            'branch': self.branch,
            'address': self.address,
            'city': self.city,
            'district': self.district,
            'state': self.state,
        }
