import { Component, inject, OnInit } from '@angular/core';
import { SkillServiceService } from '../../Service/skill-service.service';
import { Skill } from '../../modules/Skill';
import { ActivatedRoute } from '@angular/router';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-skill-detail',
  imports: [CommonModule],
  templateUrl: './skill-detail.component.html',
  styleUrl: './skill-detail.component.css'
})
export class SkillDetailComponent {
  
  skillService : SkillServiceService=inject(SkillServiceService)
  route:ActivatedRoute=inject(ActivatedRoute)
  skillId!:number;
  skill! :Skill
  islike?:boolean

  constructor(){
    this.skillId =Number(this.route.snapshot.paramMap.get('id'));
    this.skillService.getSkillDetail(this.skillId).subscribe(data=>this.skill=data)
  }
  
}
