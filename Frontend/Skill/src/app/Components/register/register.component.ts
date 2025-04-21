import { Component } from '@angular/core';
import { SkillServiceService } from '../../Service/skill-service.service';
import { Router, RouterLink } from '@angular/router';

@Component({
  selector: 'app-register',
  imports: [RouterLink],
  templateUrl: './register.component.html',
  styleUrl: './register.component.css'
})
export class RegisterComponent {
  username:string='';
  password:string='';
  email:string=''
  errorMessage:string=''

  constructor(private skillService:SkillServiceService,private route:Router){}
  Register(){
    this.skillService.getRegister(this.username,this.password).subscribe({
      next: response =>{
        console.log("Registration success",response)
        alert("Cәтті кірді");
        this.route.navigate(['/home'])
      },
      error: error =>{
        console.log("Error",error)
        this.errorMessage="Тіркелу сәтсіз болды "
      }
    })
  }
}
