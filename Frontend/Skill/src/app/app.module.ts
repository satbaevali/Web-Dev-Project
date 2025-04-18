import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { AppComponent } from './app.component';
import { SkillCategoryComponent } from './components/skill-category/skill-category.component';
import { SkillDetailComponent } from './components/skill-detail/skill-detail.component';
import { HttpClientModule } from '@angular/common/http'; // HTTP сұраныстарын жасау үшін
import { CommonModule } from '@angular/common'; // Жалпы Angular функциялар
import { AppRoutingModule } from './app.routes'; // Роутинг модулі

@NgModule({
  declarations: [
    AppComponent,
    SkillCategoryComponent,
    SkillDetailComponent, // Компоненттерді тіркеу
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    CommonModule, // Жалпы модуль
    AppRoutingModule, // Роутинг модулін қосу
  ],
  providers: [],
  bootstrap: [AppComponent],
})
export class AppModule {}
