import os
from db import db
from pathlib import Path
from flask import Flask, render_template, send_from_directory, url_for
from controllers.lc_problem import lc_problems
from controllers.lc_section import lc_sections
from resources.lc_section import LcSectionListResource


app = Flask(__name__)

app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


@app.before_first_request
def create_tables():
    db.create_all()


@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')


@app.route('/resume', methods=['GET'])
def resume():
    folder_path = os.path.join(app.root_path, "static/files")
    return send_from_directory(directory=folder_path, path='Sudeep_Dalai_Resume.pdf')


@app.route('/leetcode')
def leetcode():
    data = LcSectionListResource.get()
    return render_template("leetcode.html", data=data)

# Problem Related Endpoints
app.register_blueprint(lc_problems, url_prefix='/leetcode')

# Section Related Endpoints
app.register_blueprint(lc_sections, url_prefix='/leetcode') 


'''
To-Do:
-------
Need to make foll. APIs:
- /leetcode/problem/<prob_id> - get json of a problem DONE
- /leetcode/problem/<prob_id> - delete a problem DONE
- /leetcode/problem/<prob_id> - update a problem

- /leetcode/section/<section_id> - get json of a section
- /leetcode/section/<section_id> - update a section
- /leetcode/section/<section_id> - delete of a section

- /leetcode/problem/all - get all problems list DONE
- /leetcode/section/all - get all sections list

'''

if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5000)
