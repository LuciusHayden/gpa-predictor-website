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
input_args.add_argument("Age", type=int, help="Age", required=True)
input_args.add_argument("Gender", type=str, help="Gender", required=True)
input_args.add_argument("Ethnicity", type=str, help="Ethnicity", required=True)
input_args.add_argument("Parental_Education", type=str, help="Parental Education", required=True)
input_args.add_argument("Weekly_Study_Hours", type=int, help="Weekly Study Hours", required=True)
input_args.add_argument("Absences", type=int, help="Absences", required=True)
input_args.add_argument("Tutoring", type=bool, help="Tutoring", required=True)
input_args.add_argument("Parental_Support", type=int, help="Parental Support", required=True)
input_args.add_argument("Extracurricular_Activities", type=bool, help="Extracurricular Activities", required=True)
input_args.add_argument("Sports", type=bool, help="Sports", required=True)
input_args.add_argument("Music", type=bool, help="Music", required=True)
input_args.add_argument("Volunteering", type=bool, help="Volunteering", required=True)

response_args = reqparse.RequestParser()
response_args.add_argument("GPA", type=int, help="Students GPA", required=True)

inputFields = {
    'Age': fields.Integer,
    'Gender': fields.String,
    'Ethnicity': fields.String,
    'Parental_Education': fields.String,
    'Weekly_Study_Hours': fields.Integer,
    'Absences': fields.Integer,
    'Tutoring': fields.Boolean,
    'Parental_Support': fields.Integer,
    'Extracurricular_Activities': fields.Boolean,
    'Sports': fields.Boolean,
    'Music': fields.Boolean,
    'Volunteering': fields.Boolean
}

responseFields = {
    'GPA': fields.Float,
    'id': fields.Integer
}

class InputModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Age = db.Column(db.Integer, unique=True, nullable=False)
    Gender = db.Column(db.String(80), unique=True, nullable=False)
    Ethnicity = db.Column(db.String(80), unique=True, nullable=False)
    Parental_Education = db.Column(db.String(80), unique=True, nullable=False)
    Weekly_Study_Hours = db.Column(db.Integer, unique=True, nullable=False)
    Absences = db.Column(db.Integer, unique=True, nullable=False)
    Tutoring = db.Column(db.Boolean, unique=True, nullable=False)
    Parental_Support = db.Column(db.Integer, unique=True, nullable=False)
    Extracurricular_Activities = db.Column(db.Boolean, unique=True, nullable=False)
    Sports = db.Column(db.Boolean, unique=True, nullable=False)
    Music = db.Column(db.Boolean, unique=True, nullable=False)
    Volunteering = db.Column(db.Boolean, unique=True, nullable=False)

    def __init__(self, Age, Gender, Ethnic, Parental_Education, Weekly_Study_Hours, Absences, Tutoring, Parental_Support, Extracurricular_Activities, Sports, Music, Volunteering):
        self.Age = Age
        self.Gender = Gender
        self.Ethnicity = Ethnic
        self.Parental_Education = Parental_Education
        self.Weekly_Study_Hours = Weekly_Study_Hours
        self.Absences = Absences
        self.Tutoring = Tutoring
        self.Parental_Support = Parental_Support
        self.Extracurricular_Activities = Extracurricular_Activities
        self.Sports = Sports
        self.Music = Music
        self.Volunteering = Volunteering

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
        Age = args['Age']
        Gender = args['Gender']
        Ethnicity = args['Ethnicity']
        Parental_Education = args['Parental_Education']
        Weekly_Study_Hours = args['Weekly_Study_Hours']
        Absences = args['Absences']
        Tutoring = args['Tutoring']
        Parental_Support = args['Parental_Support']
        Extracurricular_Activities = args['Extracurricular_Activities']
        Sports = args['Sports']
        Music = args['Music']
        Volunteering = args['Volunteering']

        inputModel = InputModel(Age, Gender, Ethnicity, Parental_Education, Weekly_Study_Hours, Absences,
                                 Tutoring, Parental_Support, Extracurricular_Activities, Sports, Music, Volunteering)
        result = utils.predict_gpa(inputModel)
        print(type(result))
        print(f"result {result}")
        response = ResponseModel(result)
        return response
    
# API routes     
api.add_resource(Predict_GPA, '/api/predict')

CORS(app, resources={r"/api/*": {"origins": "http://localhost:5000", "methods": ["GET", "POST"]}})

# moved to run.py
# if __name__ == '__main__':
#     app.run(debug=True)