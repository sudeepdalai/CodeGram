from models.lc_section import LcSectionModel

class LcSectionResource:
    @staticmethod
    def post(card_id, collapse_id, heading):
        
        if LcSectionModel.find_by_heading(heading):
            return {'message': "A section with heading '{}' already exists.".format(heading)}, 400

        section = LcSectionModel(card_id, collapse_id, heading)
        try:
            section.save_to_db()
        except:
            return {"message": "An error occurred creating the section."}, 500
        
        return {'message': 'Leetcode Section created successfully.'}


class LcSectionListResource:
    @staticmethod
    def get():
        result = [section.json() for section in LcSectionModel.query.all()]
        for res in result:
            res['problems'] = sorted(res['problems'], key=lambda x: x['difficulty'])
        return result
