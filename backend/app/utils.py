from .data_model import Neural_Network 
import numpy as np

def transform_data(inputModel):
    age = inputModel.Age
    if (inputModel.Gender == "Male"):
        gender = 0
    else:
        gender = 1

    if (inputModel.Ethnicity == "Caucasian"):
        ethnicity = 0
    elif (inputModel.Ethnicity == "African American"):
        ethnicity = 1
    elif (inputModel.Ethnicity == "Asian"):
        ethnicity = 2
    else:
        ethnicity = 3

    if (inputModel.Parental_Education == "None"):
        parental_education = 0
    elif (inputModel.Parental_Education == "High School"):
        parental_education = 1
    elif (inputModel.Parental_Education == "Some College"):
        parental_education = 2
    elif (inputModel.Parental_Education == "Bachelor's"):
        parental_education = 3
    else:
        parental_education = 4

    weekly_study_hours = inputModel.Weekly_Study_Hours

    absences = inputModel.Absences

    if (inputModel.Tutoring == True):
        tutoring = 1
    else:
        tutoring = 0
    
    if (inputModel.Parental_Support == "None"):
        parental_support = 0
    elif (inputModel.Parental_Support == "Low"):
        parental_support = 1
    elif (inputModel.Parental_Support == "Moderate"):
        parental_support = 2
    elif (inputModel.Parental_Support == "High"):
        parental_support = 3
    else:
        parental_support = 4

    if (inputModel.Extracurricular_Activities == True):
        extracurricular_activities = 1
    else:
        extracurricular_activities = 0

    if (inputModel.Sports == True):
        sports = 1
    else:
        sports = 0

    if (inputModel.Music == True):
        music = 1
    else:
        music = 0

    if (inputModel.Volunteering == True):
        volunteering = 1
    else:
        volunteering = 0

    return [age, gender, ethnicity, parental_education, weekly_study_hours, absences, tutoring, parental_support, extracurricular_activities, sports, music, volunteering]

def predict_gpa(inputModel):
    transformed_data = transform_data(inputModel)
    data = np.array(transformed_data, dtype=float).reshape(-1, 12)
    print(data)
    return Neural_Network.predict(data)