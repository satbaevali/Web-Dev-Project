import { SkillCategory } from "./SkillCategory";

export interface Review {
  user: string;
  comment: string;
}

export interface Skill {
  id: number;
  name: string;
  description: string;
  price: number;
  image?: string;
  category: SkillCategory;


  rating: number;
  reviews: Review[];
}
