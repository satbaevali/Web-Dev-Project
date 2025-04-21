import { Component, inject, OnInit,Output,EventEmitter } from '@angular/core';
import { SkillCategory } from '../../modules/SkillCategory';
import { SkillServiceService } from '../../Service/skill-service.service';
import { Skill } from '../../modules/Skill';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-skill-category',
  imports: [CommonModule],
  templateUrl: './skill-category.component.html',
  styleUrl: './skill-category.component.css'
})
export class SkillCategoryComponent implements OnInit {
  
  
  skillService : SkillServiceService=inject(SkillServiceService)
  @Output() skillCategoriesLoaded = new EventEmitter<SkillCategory[]>()

  ngOnInit(): void {
    this.skillService.getSkillCategories().subscribe(data => {
      this.skillCategoriesLoaded.emit(data);
    })
  }



}
