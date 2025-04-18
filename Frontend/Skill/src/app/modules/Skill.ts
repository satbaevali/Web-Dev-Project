import { SkillCategory } from "./SkillCategory"

export interface Skill{
    id:number,
    name:string,
    description:string,
    category:SkillCategory
}