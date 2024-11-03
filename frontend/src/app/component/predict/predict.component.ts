import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import { CommonModule } from '@angular/common';
import { InputModel, ResponseModel } from '../../interface/predict';
import { PredictService } from '../../service/predict.service';
import { ChangeDetectorRef } from '@angular/core';

@Component({
  selector: 'app-predict',
  standalone: true,
  imports: [FormsModule, HttpClientModule, CommonModule],
  templateUrl: './predict.component.html',
  styleUrl: './predict.component.css'
})
export class PredictComponent {

  inputModel: InputModel = {
    age: 0,
    gender: '',
    ethnicity: '',
    parental_education: '',
    weekly_study_hours: 0,
    absences: 0,
    tutoring: false,
    parental_support: 0,
    extracurricular_activities: false,
    sports: false,
    music: false,
    volunteering: false
  };
  responseModel: ResponseModel = {
    GPA: 0
  };

  constructor(private predictService: PredictService, private changeDetectorRef: ChangeDetectorRef) { }

  predict() {
    this.predictService.predict(this.inputModel).subscribe((data: ResponseModel) => {
      this.responseModel = data;
      this.changeDetectorRef.detectChanges();
    });
  }

}
