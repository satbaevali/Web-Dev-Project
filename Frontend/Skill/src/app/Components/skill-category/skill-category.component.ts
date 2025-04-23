import { Component, inject, OnInit, Output, EventEmitter } from '@angular/core';
import { CommonModule } from '@angular/common';
import { SkillCategory } from '../../modules/SkillCategory';
import { SkillServiceService } from '../../Service/skill-service.service';

@Component({
  selector: 'app-skill-category',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './skill-category.component.html',
  styleUrls: ['./skill-category.component.css']
})
export class SkillCategoryComponent implements OnInit {
  private skillService = inject(SkillServiceService);
  @Output() skillCategoriesLoaded = new EventEmitter<SkillCategory[]>();

  ngOnInit(): void {
    this.skillService.getSkillCategories()
      .subscribe(data => this.skillCategoriesLoaded.emit(data));
  }
}
