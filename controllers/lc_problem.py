from flask import Blueprint, request
from resources.lc_problem import LcProblemResource, LcProblemListResource

lc_problems = Blueprint('lc_problems', __name__)


@lc_problems.route('/problem', methods=['POST'])
def post_lc_problem():
    request_data = request.get_json()

    problem_link = request_data.get('problem_link')
    problem_title = request_data.get('problem_title')
    difficulty = request_data.get('difficulty')
    solution_link = request_data.get('solution_link')
    section_id = request_data.get('section_id')

    return LcProblemResource.post(problem_link, problem_title, difficulty, solution_link, section_id)


@lc_problems.route('/problem/<int:problem_id>', methods=['GET'])
def get_lc_problem_by_id(problem_id):
    return LcProblemResource.get(problem_id)


@lc_problems.route('/problem/<int:problem_id>', methods=['DELETE'])
def delete_lc_problem_by_id(problem_id):
    return LcProblemResource.delete(problem_id)


@lc_problems.route('/problems/all', methods=['GET'])
def get_all_lc_problems():
    return LcProblemListResource.get()