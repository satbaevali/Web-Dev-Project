import { Component } from '@angular/core';
import { RouterLink } from '@angular/router';
import { SkillCategory } from '../../modules/SkillCategory';
import { SkillCategoryComponent } from '../skill-category/skill-category.component';
import { CommonModule } from '@angular/common';
import { Skill } from '../../modules/Skill';
import { SkillsComponent } from "../skills/skills.component";
import { SkillServiceService } from '../../Service/skill-service.service';

@Component({
  selector: 'app-home',
  imports: [SkillCategoryComponent, CommonModule,RouterLink],
  templateUrl: './home.component.html',
  styleUrl: './home.component.css'
})
export class HomeComponent {

  skillCategories: SkillCategory[] = [];

  onSkillCategoriesLoaded(categories: SkillCategory[]) {
    this.skillCategories = categories;
  }

  allSkills: Skill[] = [];      
  filteredSkills: Skill[] = []; 

  constructor(private skillService: SkillServiceService) {}

  ngOnInit(): void {
    this.skillService.getALLSkill().subscribe(data => {
      this.allSkills = data;
      this.filteredSkills = data; 
    });
  }

  onCategorySelected(categoryName: string): void {
    if (categoryName === 'All') {
      this.filteredSkills = this.allSkills;
    } else {
      this.filteredSkills = this.allSkills.filter(skill => skill.category.name === categoryName);
    }
  }
}

