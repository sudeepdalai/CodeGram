from db import db


class LcSectionModel(db.Model):
    __tablename__ = 'lcSections'

    id = db.Column(db.Integer, primary_key=True)
    cardId = db.Column(db.String(50))
    collapseId = db.Column(db.String(50))
    heading = db.Column(db.String(100))
    problems = db.relationship('LcProblemModel', lazy='dynamic')

    def __init__(self, cardId, collapseId, heading):
        self.heading = heading
        self.collapseId = collapseId
        self.cardId = cardId

    def json(self):
        return {
            'section_id': self.id,
            'heading': self.heading,
            'card_id': self.cardId,
            'collapse_id': self.collapseId,
            'problems': [problem.json() for problem in self.problems.all()]
        }

    @classmethod
    def find_by_heading(cls, heading):
        return cls.query.filter_by(heading=heading).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
