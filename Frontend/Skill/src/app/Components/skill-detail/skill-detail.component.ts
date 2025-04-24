import { Component, OnInit } from '@angular/core';
import {ActivatedRoute, RouterLink} from '@angular/router';
import { SkillServiceService } from '../../Service/skill-service.service';
import { Skill } from '../../modules/Skill';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-skill-detail',
  standalone: true,
  imports: [CommonModule, RouterLink],
  templateUrl: './skill-detail.component.html',
  styleUrls: ['./skill-detail.component.css']
})
export class SkillDetailComponent implements OnInit {
  skillId!: number;
  skill!: Skill;

  constructor(
    private route: ActivatedRoute,
    private skillService: SkillServiceService
  ) {}

  ngOnInit(): void {
    this.skillId = Number(this.route.snapshot.paramMap.get('id'));
    this.skillService.getSkillById(this.skillId).subscribe((skill: any) => {
      this.skill = skill;
    });
  }
}
