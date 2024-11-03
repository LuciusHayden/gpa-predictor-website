from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_restful import reqparse, fields, marshal_with, Resource
from . import utils

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
api = Api(app)

input_args = reqparse.RequestParser()
input_args.add_argument("age", type=int, help="Age", required=True)
input_args.add_argument("gender", type=str, help="Gender", required=True)
input_args.add_argument("ethnicity", type=str, help="Ethnicity", required=True)
input_args.add_argument("parental_education", type=str, help="Parental Education", required=True)
input_args.add_argument("weekly_study_hours", type=int, help="Weekly Study Hours", required=True)
input_args.add_argument("absences", type=int, help="Absences", required=True)
input_args.add_argument("tutoring", type=bool, help="Tutoring", required=True)
input_args.add_argument("parental_support", type=int, help="Parental Support", required=True)
input_args.add_argument("extracurricular_activities", type=bool, help="Extracurricular Activities", required=True)
input_args.add_argument("sports", type=bool, help="Sports", required=True)
input_args.add_argument("music", type=bool, help="Music", required=True)
input_args.add_argument("volunteering", type=bool, help="Volunteering", required=True)

response_args = reqparse.RequestParser()
response_args.add_argument("GPA", type=int, help="Students GPA", required=True)

inputFields = {
    'age': fields.Integer,
    'gender': fields.String,
    'ethnicity': fields.String,
    'parental_education': fields.String,
    'weekly_study_hours': fields.Integer,
    'absences': fields.Integer,
    'tutoring': fields.Boolean,
    'parental_support': fields.Integer,
    'extracurricular_activities': fields.Boolean,
    'sports': fields.Boolean,
    'music': fields.Boolean,
    'volunteering': fields.Boolean
}

responseFields = {
    'GPA': fields.Float,
    'id': fields.Integer
}

class InputModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    age = db.Column(db.Integer, unique=True, nullable=False)
    gender = db.Column(db.String(80), unique=True, nullable=False)
    ethnicity = db.Column(db.String(80), unique=True, nullable=False)
    parental_education = db.Column(db.String(80), unique=True, nullable=False)
    weekly_study_hours = db.Column(db.Integer, unique=True, nullable=False)
    absences = db.Column(db.Integer, unique=True, nullable=False)
    tutoring = db.Column(db.Boolean, unique=True, nullable=False)
    parental_support = db.Column(db.String(80), unique=True, nullable=False)
    extracurricular_activities = db.Column(db.Boolean, unique=True, nullable=False)
    sports = db.Column(db.Boolean, unique=True, nullable=False)
    music = db.Column(db.Boolean, unique=True, nullable=False)
    volunteering = db.Column(db.Boolean, unique=True, nullable=False)

    def __init__(self, Age, Gender, Ethnic, Parental_Education, Weekly_Study_Hours, Absences, Tutoring, Parental_Support, Extracurricular_Activities, Sports, Music, Volunteering):
        self.age = Age
        self.gender = Gender
        self.ethnicity = Ethnic
        self.parental_education = Parental_Education
        self.weekly_study_hours = Weekly_Study_Hours
        self.absences = Absences
        self.tutoring = Tutoring
        self.parental_support = Parental_Support
        self.extracurricular_activities = Extracurricular_Activities
        self.sports = Sports
        self.music = Music
        self.volunteering = Volunteering

class ResponseModel(db.Model):
    GPA = db.Column(db.Integer, unique=False, nullable=False)
    id = db.Column(db.Float, primary_key=True)

    def __init__(self, GPA):
        self.GPA = GPA

    def __repr__(self):
        return '<GPA %r>' % self.GPA
    
class Predict_GPA(Resource):
    @marshal_with(responseFields)
    def post(self):
        args = input_args.parse_args()
        age = args['age']
        gender = args['gender']
        ethnicity = args['ethnicity']
        parental_education = args['parental_education']
        weekly_study_hours = args['weekly_study_hours']
        absences = args['absences']
        tutoring = args['tutoring']
        parental_support = args['parental_support']
        extracurricular_activities = args['extracurricular_activities']
        sports = args['sports']
        music = args['music']
        volunteering = args['volunteering']
        
        inputModel = InputModel(age, gender, ethnicity, parental_education, weekly_study_hours, absences,
                                 tutoring, parental_support, extracurricular_activities, sports, music, volunteering)
        result = utils.predict_gpa(inputModel)
        print(type(result))
        print(f"result {result}")
        response = ResponseModel(result)
        return response
    
# API routes     
api.add_resource(Predict_GPA, '/api/predict')

CORS(app, resources={r"/api/*": {"origins": "http://localhost:4200", "methods": ["GET", "POST"]}})

# moved to run.py
# if __name__ == '__main__':
#     app.run(debug=True)