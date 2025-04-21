import { Skill } from "./Skill";

export type LearningRequestStatus = 'active' | 'fulfilled' | 'archived';

export interface LearningRequest{
    skill:Skill,
    desired_level:string,
    status:string,
    created_at:string
}