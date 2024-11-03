export interface InputModel {
  age : number;
  gender : string;
  ethnicity : string;
  parental_education : string;
  weekly_study_hours : number;
  absences : number;
  tutoring : boolean;
  parental_support : number;
  extracurricular_activities : boolean;
  sports : boolean;
  music : boolean;
  volunteering : boolean;
}

export interface ResponseModel {
  GPA : number;
}
