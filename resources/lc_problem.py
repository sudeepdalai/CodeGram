from models.lc_problem import LcProblemModel

class LcProblemResource:
    
    @classmethod
    def post(cls, problem_link, problem_title, difficulty, solution_link, section_id):
        
        if LcProblemModel.find_by_problem_title(problem_title):
            return {'message': "A problem with name '{}' already exists.".format(problem_title)}, 400
        
        prob = LcProblemModel(problem_link, problem_title, difficulty, solution_link, section_id)
        
        try:
            prob.save_to_db()
        except:
            return {"message": "An error occurred creating the problem."}, 500

        return {'message': 'Leetcode Problem created successfully.'}

    @classmethod
    def get(cls, _id):
        problem = LcProblemModel.find_by_id(_id)
        if problem:
            return problem.json()
        
        return {'message': "A problem with id '{}' does not exist.".format(_id)}, 404
    
    @classmethod
    def delete(cls, _id):
        problem = LcProblemModel.find_by_id(_id)
        if problem:
            problem.delete_from_db()
        
        return {'message': 'Leetcode Problem deleted successfully.'}


class LcProblemListResource:
    @staticmethod
    def get():
        result = [problem.json() for problem in LcProblemModel.query.all()]
        return result