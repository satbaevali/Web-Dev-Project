import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Skill } from '../modules/Skill';
import { SkillCategory } from '../modules/SkillCategory';

@Injectable({
  providedIn: 'root'
})
export class SkillServiceService {
  snapshot: any;

  constructor(private httpClient:HttpClient) { }

  getLogin(username:string,password:string):Observable<{ access: string; refresh: string }>{
    return this.httpClient.post<{ access: string; refresh: string }>('http://localhost:8000/',{
      username:username,
      password:password
    })
  }
  getRegister(username:string,password:string):Observable<any>{
    return this.httpClient.post<any>('http://localhost:8000/',{
      username:username,
      password:password,
    })
  }

  getCategory():Observable<SkillCategory[]>{
    return this.httpClient.get<SkillCategory[]>('')
  }

  getSkillDetail(): Observable<Skill[]>{
    return this.httpClient.get<Skill[]>(``)
  }


}
