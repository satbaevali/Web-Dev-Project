import { Component } from '@angular/core';
import { RouterLink } from '@angular/router';
import { SkillCategory } from '../../modules/SkillCategory';
import { SkillCategoryComponent } from '../skill-category/skill-category.component';
import { CommonModule } from '@angular/common';
import { Router } from '@angular/router';
@Component({
  selector: 'app-home',
  imports: [SkillCategoryComponent,CommonModule],
  templateUrl: './home.component.html',
  styleUrl: './home.component.css'
})
export class HomeComponent {
  constructor(private router: Router) {}
  skillCategories: SkillCategory[] = [];

  onSkillCategoriesLoaded(categories: SkillCategory[]) {
    this.skillCategories = categories;
  }
  goToProfile() {
    this.router.navigate(['/profile']);
  }
}
