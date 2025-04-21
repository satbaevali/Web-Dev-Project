import { Routes } from '@angular/router';
import { HomeComponent } from './Components/home/home.component';
import { RouterLink } from '@angular/router';
import { LoginComponent } from './Components/login/login.component';
import { RegisterComponent } from './Components/register/register.component';
import { SkillCategoryComponent } from './Components/skill-category/skill-category.component';

export const routes: Routes = [
    {
        path:'',component:HomeComponent
    },
   {path:'login',component:LoginComponent},
   {path:'register',component:RegisterComponent},
   {path:'',component:SkillCategoryComponent}
];
