import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { Skill } from '../../modules/Skill';
import { SkillCategory } from '../../modules/SkillCategory';
import { SkillServiceService } from '../../Service/skill-service.service';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-home',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {
  skillCategories: SkillCategory[] = [];
  allSkills: Skill[] = [];
  filteredSkills: Skill[] = [];

  searchTerm: string = '';
  selectedCategory: string = '';

  constructor(
    private skillService: SkillServiceService,
    private router: Router
  ) {}

  ngOnInit() {
    this.skillService.getSkillCategories()
      .subscribe(cats => this.skillCategories = cats);

    this.skillService.getALLSkill()
      .subscribe(skills => {
        this.allSkills = skills;
        this.filteredSkills = skills;
      });
  }

  applyFilters() {
    this.filteredSkills = this.allSkills.filter(s => {
      const matchesName = s.name.toLowerCase().includes(this.searchTerm.toLowerCase());
      const matchesCat = this.selectedCategory ? s.category?.name === this.selectedCategory : true;
      return matchesName && matchesCat;
    });
  }

  resetFilter() {
    this.searchTerm = '';
    this.selectedCategory = '';
    this.filteredSkills = [...this.allSkills];
  }

  viewDetail(id: number) {
    this.router.navigate(['/skill-detail', id]);
  }

  goToProfile() {
    this.router.navigate(['/profile']);
  }
}
