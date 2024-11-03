import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { InputModel, ResponseModel } from '../interface/predict';

@Injectable({
  providedIn: 'root'
})
export class PredictService {

  readonly headers : HttpHeaders;

  constructor(private http: HttpClient) {
    this.headers = new HttpHeaders({
      'Content-Type': 'application/json',
    });
   }

   predict(inputModel: InputModel): Observable<ResponseModel> {
      return this.http.post<ResponseModel>('http://localhost:5000/api/predict', inputModel, {headers: this.headers});
   }

}
