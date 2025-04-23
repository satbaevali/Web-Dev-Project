import { Component } from '@angular/core';
import { SkillServiceService } from '../../Service/skill-service.service';
import { Router, RouterLink } from '@angular/router';
import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-login',
  standalone: true,
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css'],
  imports: [FormsModule,CommonModule,RouterLink],
})
export class LoginComponent {
  username: string = '';
  password: string = '';
  errorMessage: string = '';

  constructor(private skillService: SkillServiceService, private router: Router) {}

  login() {
    this.skillService.getLogin(this.username, this.password).subscribe({
      next: (response) => {
        if (response.access && response.refresh) {
          localStorage.setItem('access_token', response.access);
          localStorage.setItem('refresh_token', response.refresh);
          this.router.navigate(['/home']);
          console.log('Успешный вход!', response);
        } else {
          this.errorMessage = 'Ошибка авторизации';
        }
      },
      error: () => {
        this.errorMessage = 'Wrong password or login';
      }
    });
  }
}
