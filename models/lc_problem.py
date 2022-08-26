from db import db


class LcProblemModel(db.Model):
    __tablename__ = 'lcProblems'

    id = db.Column(db.Integer, primary_key=True)
    problemLink = db.Column(db.String(200))
    problemTitle = db.Column(db.String(100))
    difficulty = db.Column(db.Integer)
    solutionLink = db.Column(db.String(200))

    sectionId = db.Column(db.Integer, db.ForeignKey('lcSections.id'))
    section = db.relationship('LcSectionModel')

    def __init__(self, problemLink, problemTitle, difficulty, solutionLink, sectionId):
        self.sectionId = sectionId
        self.solutionLink = solutionLink
        self.difficulty = difficulty
        self.problemTitle = problemTitle
        self.problemLink = problemLink

    @classmethod
    def find_by_problem_title(cls, problemTitle):
        return cls.query.filter_by(problemTitle=problemTitle).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    def json(self):
        return {
            'problem_id': self.id,
            'problem_link': self.problemLink,
            'problem_title': self.problemTitle,
            'difficulty': self.difficulty,
            'solution_link': self.solutionLink,
            'section_id': self.sectionId
        }

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
