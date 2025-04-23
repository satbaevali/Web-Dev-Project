import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Router } from '@angular/router';
import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.css'],
  standalone: true,
  imports: [FormsModule, CommonModule],
})
export class ProfileComponent implements OnInit {
  user: any = {
    username: '',
    first_name: '',
    last_name: '',
    email: '',
    bio: '',
    profile_picture: null,
    skill: []
  };
  editMode = false;
  selectedFile: File | null = null;
  previewUrl: string | null = null;
  errorMessage: string | null = null;

  constructor(private http: HttpClient, private router: Router) {}

  ngOnInit(): void {
    const username = localStorage.getItem('username');
    if (username) {
      this.loadUserProfile(username);
    } else {
      this.router.navigate(['/login']);
    }
  }

  // Load user profile data from the server
  loadUserProfile(username: string): void {
    this.http.get(`http://localhost:8000/accounts/profile/${username}/`).subscribe({
      next: (data: any) => {
        this.user = data;
      },
      error: (error) => {
        console.error('Ошибка при загрузке профиля', error);
        this.errorMessage = 'Не удалось загрузить профиль. Попробуйте снова позже.';
      }
    });
  }

  onFileSelected(event: Event): void {
    const input = event.target as HTMLInputElement;
    if (input.files && input.files[0]) {
      this.selectedFile = input.files[0];
      const reader = new FileReader();
      reader.onload = (e: any) => {
        this.previewUrl = e.target.result;
      };
      reader.readAsDataURL(this.selectedFile);
    }
  }

  updateProfile(): void {
    if (!this.user.username || !this.user.first_name || !this.user.last_name) {
      this.errorMessage = 'Пожалуйста, заполните все обязательные поля.';
      return;
    }

    const formData = new FormData();
    formData.append('username', this.user.username);
    formData.append('first_name', this.user.first_name);
    formData.append('last_name', this.user.last_name);
    formData.append('bio', this.user.bio);

    if (this.selectedFile) {
      formData.append('profile_picture', this.selectedFile, this.selectedFile.name);
    }

    this.http.put(`http://localhost:8000/accounts/profile/${this.user.username}/`, formData).subscribe({
      next: (response) => {
        alert('Профиль успешно обновлен');
        this.editMode = false;
        this.previewUrl = null;
        this.loadUserProfile(this.user.username); // Перезагрузка данных с обновленным профилем
      },
      error: (error) => {
        console.error('Ошибка при обновлении профиля:', error);
        this.errorMessage = 'Не удалось обновить профиль. Попробуйте снова.';
      }
    });
  }
}
