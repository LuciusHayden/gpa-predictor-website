from .data_model import Neural_Network 
import numpy as np

def transform_data(inputModel):
    age = inputModel.age
    if (inputModel.gender == "Male"):
        gender = 0
    else:
        gender = 1

    if (inputModel.ethnicity == "Caucasian"):
        ethnicity = 0
    elif (inputModel.ethnicity == "African American"):
        ethnicity = 1
    elif (inputModel.ethnicity == "Asian"):
        ethnicity = 2
    else:
        ethnicity = 3

    if (inputModel.parental_education == "None"):
        parental_education = 0
    elif (inputModel.parental_education == "High School"):
        parental_education = 1
    elif (inputModel.parental_education == "Some College"):
        parental_education = 2
    elif (inputModel.parental_education == "Bachelor's"):
        parental_education = 3
    else:
        parental_education = 4

    weekly_study_hours = inputModel.weekly_study_hours

    absences = inputModel.absences

    if (inputModel.tutoring == True):
        tutoring = 1
    else:
        tutoring = 0
    
    if (inputModel.parental_support == "None"):
        parental_support = 0
    elif (inputModel.parental_support == "Low"):
        parental_support = 1
    elif (inputModel.parental_support == "Moderate"):
        parental_support = 2
    elif (inputModel.parental_support == "High"):
        parental_support = 3
    else:
        parental_support = 4

    if (inputModel.extracurricular_activities == True):
        extracurricular_activities = 1
    else:
        extracurricular_activities = 0

    if (inputModel.sports == True):
        sports = 1
    else:
        sports = 0

    if (inputModel.music == True):
        music = 1
    else:
        music = 0

    if (inputModel.volunteering == True):
        volunteering = 1
    else:
        volunteering = 0
    return [age, gender, ethnicity, parental_education, weekly_study_hours, absences, tutoring, parental_support, extracurricular_activities, sports, music, volunteering]

def predict_gpa(inputModel):
    transformed_data = transform_data(inputModel)
    data = np.array(transformed_data, dtype=float).reshape(-1, 12)
    print(data)
    return Neural_Network.predict(data)