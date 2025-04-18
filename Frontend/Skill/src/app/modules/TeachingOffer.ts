import { Skill } from "./Skill";

export enum Level{
    Beginner = 'beginner',
    Intermediate = 'intermediate',
    Advanced = 'advanced',
    Expert = 'expert'
}

export enum Status{
    Active = 'active',
    Inactive = 'inactive',
    Archived = 'archived'
}


export interface TeachingOffer{
    skill:Skill,
    description:string,
    experience_level:string,
    choices:Level,
    status:string,
    created_at:string,
    updated_at:string
}