import { Component, inject,Output,EventEmitter, OnInit } from '@angular/core';
import { SkillServiceService } from '../../Service/skill-service.service';
import { Skill } from '../../modules/Skill';

@Component({
  selector: 'app-skills',
  imports: [],
  templateUrl: './skills.component.html',
  styleUrl: './skills.component.css'
})
export class SkillsComponent implements OnInit {
  
  skillService : SkillServiceService = inject(SkillServiceService)
  @Output() SeeAllSkills = new EventEmitter<Skill[]>()

  ngOnInit(): void {
    this.skillService.getALLSkill().subscribe(data=>{
      this.SeeAllSkills.emit(data)
    })
  }
  
}
