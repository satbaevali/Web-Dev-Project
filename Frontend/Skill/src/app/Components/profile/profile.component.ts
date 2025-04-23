import { Component, OnInit } from '@angular/core';
import {Router, RouterLink} from '@angular/router';
import { SkillServiceService } from '../../Service/skill-service.service';
import {SkillCategory} from '../../modules/SkillCategory';
import {FormsModule} from '@angular/forms';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  imports: [
    FormsModule, CommonModule, RouterLink
  ],
  styleUrls: ['./profile.component.css']
})
export class ProfileComponent implements OnInit {
  user: any = {};
  editMode = false;
  selectedFile: File | null = null;
  previewUrl: string | null = null;
  errorMessage: string | null = null;
  allCategories: SkillCategory[] = [];// для выпадающего списка навыков
  selectedSkillId: number | null = null; // выбранный навык

  constructor(private skillService: SkillServiceService, private router: Router) {}

  ngOnInit(): void {
    const username = localStorage.getItem('username');
    if (!username) { this.router.navigate(['/login']); return; }
    this.loadUserProfile(username);
    // подгружаем категории как список для выбора skill
    this.skillService.getSkillCategories().subscribe(c=> this.allCategories=c);
  }

  loadUserProfile(username: string) {
    this.skillService.getUserProfile(username).subscribe({
      next: data => this.user = data,
      error: () => this.errorMessage = 'Не удалось загрузить профиль.'
    });
  }

  onFileSelected(e: Event) {
    const input = e.target as HTMLInputElement;
    if (input.files?.[0]) {
      this.selectedFile = input.files[0];
      const reader = new FileReader();
      reader.onload = ev => this.previewUrl = (ev.target as any).result;
      reader.readAsDataURL(this.selectedFile);
    }
  }

  updateProfile() {
    if (!this.user.first_name || !this.user.last_name) {
      this.errorMessage = 'Заполните имя и фамилию.';
      return;
    }
    const fd = new FormData();
    ['username','first_name','last_name','email','bio'].forEach(f => {
      if (this.user[f] != null) fd.append(f, this.user[f]);
    });
    if (this.selectedFile) fd.append('profile_picture', this.selectedFile, this.selectedFile.name);
    if (this.selectedSkillId) fd.append('skill', this.selectedSkillId.toString());

    const username = this.user.username;
    this.skillService.updateUserProfile(username, fd).subscribe({
      next: () => {
        alert('Профиль сохранён');
        this.editMode = false;
        this.previewUrl = null;
        this.loadUserProfile(username);
      },
      error: () => this.errorMessage = 'Ошибка при сохранении.'
    });
  }

  logout(): void {
    // Удаляем всё, что связано с пользователем
    // Можно очистить весь localStorage, если больше нечего хранить:
    // localStorage.clear();

    // Редирект на страницу логина
    this.router.navigate(['/login']);
  }

  // устанавливаем навык из select
  onSkillChange(id: string) {
    this.selectedSkillId = +id;
  }

  protected readonly HTMLSelectElement = HTMLSelectElement;
}
