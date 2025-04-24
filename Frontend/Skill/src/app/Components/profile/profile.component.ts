import { Component, OnInit, inject } from '@angular/core';
import { Router, RouterLink } from '@angular/router';
import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { SkillServiceService } from '../../Service/skill-service.service';
import { SkillCategory } from '../../modules/SkillCategory';

@Component({
  selector: 'app-profile',
  standalone: true,
  imports: [CommonModule, FormsModule, RouterLink],
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.css']
})
export class ProfileComponent implements OnInit {
  user: any = {};
  editMode = false;
  selectedFile: File | null = null;
  previewUrl: string | null = null;
  errorMessage: string | null = null;
  allCategories: SkillCategory[] = [];
  selectedSkillId: number | null = null;

  // New features state
  offers: any[] = [];
  reviews: any[] = [];
  rating: number = 0;

  private skillService = inject(SkillServiceService);
  private router = inject(Router);

  ngOnInit(): void {
    this.loadInitialData();
  }

  private loadInitialData() {
    const username = localStorage.getItem('username');
    if (!username) { this.router.navigate(['/login']); return; }

    // load profile
    this.skillService.getUserProfile(username).subscribe({
      next: data => {
        this.user = data;
        this.selectedSkillId = data.skill?.id || null;
        this.computeRating();
      },
      error: () => this.errorMessage = 'Не удалось загрузить профиль.'
    });

    // load categories
    this.skillService.getSkillCategories().subscribe(c => this.allCategories = c);

    // load user's teaching offers
    this.skillService.getUserOffers(username).subscribe((o: any[]) => this.offers = o);

    // load reviews separately (if service has method)
    this.skillService.getUserReviews(username).subscribe((r: any[]) => this.reviews = r);
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
    this.errorMessage = null;
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

    this.skillService.updateUserProfile(this.user.username, fd).subscribe({
      next: () => {
        this.editMode = false;
        this.previewUrl = null;
        this.loadInitialData();
      },
      error: () => this.errorMessage = 'Ошибка при сохранении.'
    });
  }

  logout(): void {
    localStorage.clear();
    this.router.navigate(['/login']);
  }

  onSkillChange(id: string) {
    this.selectedSkillId = +id;
  }

  private computeRating() {
    const qs = this.user.reviews || [];
    if (!qs.length) { this.rating = 0; return; }
    this.rating = qs.reduce((sum: number, r: any) => sum + r.rating, 0) / qs.length;
  }
}
