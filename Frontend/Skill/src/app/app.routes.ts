import { Routes } from '@angular/router';
import { HomeComponent } from './Components/home/home.component';
import { RouterLink } from '@angular/router';
import { LoginComponent } from './Components/login/login.component';
import { RegisterComponent } from './Components/register/register.component';
import { SkillCategoryComponent } from './Components/skill-category/skill-category.component';
import { ProfileComponent } from './Components/profile/profile.component';

export const routes: Routes = [
    {
        path:'home',component:HomeComponent
    },
   {path:'',component:LoginComponent},
   {path:'register',component:RegisterComponent},
   {path:'',component:SkillCategoryComponent},
   {path:'profile',component:ProfileComponent}
];
