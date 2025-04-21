import { Component } from '@angular/core';
import { SkillServiceService } from '../../Service/skill-service.service';
import { Router, RouterLink } from '@angular/router';

@Component({
  selector: 'app-login',
  imports: [RouterLink],
  templateUrl: './login.component.html',
  styleUrl: './login.component.css'
})
export class LoginComponent {
  username:string='';
  password:string='';
  errorMessage: string='';

  constructor(private skillService :SkillServiceService , private route : Router){}

  login(){
    this.skillService.getLogin(this.username,this.password).subscribe({
      next:(response)=>{
        localStorage.setItem('access_token',response.access),
        localStorage.setItem('refresh_token',response.refresh)
        this.route.navigate(['/home'])
        alert("PassedLogin")
      },
      error: (error)=>{
        this.errorMessage = "The user name or password is incorrect"
      }
    })
  }
}
