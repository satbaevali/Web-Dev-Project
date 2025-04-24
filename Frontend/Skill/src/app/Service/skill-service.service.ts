import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import {map, Observable} from 'rxjs';
import { Skill } from '../modules/Skill';
import { SkillCategory } from '../modules/SkillCategory';

@Injectable({
  providedIn: 'root'
})
export class SkillServiceService {
  snapshot: any;
  private API = 'http://localhost:8000';

  constructor(private httpClient:HttpClient) { }

  getLogin(username: string, password: string): Observable<{ access: string; refresh: string }> {
    return this.httpClient.post<{ access: string; refresh: string }>(
      'http://localhost:8000/api/api/login/',
      { username, password }
    );
  }

  getRegister(name: string, password: string, email: string): Observable<any> {
    return this.httpClient.post<any>('http://localhost:8000/register/', {
      username: name,
      password,
      email
    });
  }
  getUserProfile(username: string): Observable<any> {
    return this.httpClient.get<any>(`${this.API}/accounts/profile/${username}/`);
  }

  // Обновление профиля конкретного пользователя
  updateUserProfile(username: string, formData: FormData): Observable<any> {
    return this.httpClient.put<any>(`${this.API}/accounts/edit_profile/${username}/`, formData);
  }


  getSkillCategories():Observable<SkillCategory[]>{
    return this.httpClient.get<SkillCategory[]>('http://localhost:8000/api/skill-categories/')
  }

  getSkillDetail(): Observable<Skill[]>{
    return this.httpClient.get<Skill[]>(``)
  }

  getALLSkill(): Observable<Skill[]>{
    return this.httpClient.get<Skill[]>('http://localhost:8000/api/skills/')
  }

  getSkillById(id: number): Observable<Skill> {
    return this.httpClient.get<Skill>(`http://localhost:8000/api/skills/${id}/`);
  }

  getUserOffers(username: string): Observable<any[]> {
    return this.getUserProfile(username).pipe(
      map((profile: any) => profile.teaching_offers || [])
    );
  }

  getUserReviews(username: string): Observable<any[]> {
    return this.getUserProfile(username).pipe(
      map((profile: any) => profile.reviews || [])
    );
}}
