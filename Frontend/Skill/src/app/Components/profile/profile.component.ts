import { Component, OnInit } from '@angular/core';
import { SkillServiceService } from '../../Service/skill-service.service';
import { Router } from '@angular/router';
import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';
@Component({
  selector: 'app-profile',
  imports: [CommonModule, FormsModule],
  standalone: true,
  templateUrl: './profile.component.html',
  styleUrl: './profile.component.css'
})
export class ProfileComponent implements OnInit {
  user = {
    username: '',
    email: '',
    first_name: '',
    last_name: '',
    bio: '',
    skill: [],
    profile_picture: ''
  };
  errorMessage: string = '';
  selectedFile: File | null = null;
  previewUrl: string | null = null;
  editMode: boolean = false; // 👈 переключатель
  constructor(private skillService: SkillServiceService, private route: Router) {}
  ngOnInit(): void {
    this.loadUserProfile();
  }
  loadUserProfile(): void {
    this.skillService.getUserProfile().subscribe({
      next: (response) => {
        this.user = response; // Загружаем данные профиля
      },
      error: (error) => {
        this.errorMessage = 'Не удалось загрузить профиль';
      }
    });
  }
  updateProfile(): void {
    const formData = new FormData();
    formData.append('username', this.user.username);
    formData.append('email', this.user.email);
    formData.append('first_name', this.user.first_name);
    formData.append('last_name', this.user.last_name);
    formData.append('bio', this.user.bio);
    
    
    if (this.selectedFile) {
      formData.append('profile_picture', this.selectedFile, this.selectedFile.name);
    }
  
    this.skillService.updateUserProfile(formData).subscribe({
      next: (response) => {
        alert('Профиль обновлен успешно');
        this.route.navigate(['/home']);
      },
      error: (error) => {
        this.errorMessage = 'Ошибка при обновлении профиля';
      }
    });
  }
  onFileSelected(event: any): void {
    const file: File = event.target.files[0];
    if (file) {
      this.selectedFile = file;
      this.previewUrl = URL.createObjectURL(file); // Для отображения превью
      console.log('Выбран файл:', file);
    }
  }
  goToProfile() {
    this.route.navigate(['/profile']);
  }
  

}
