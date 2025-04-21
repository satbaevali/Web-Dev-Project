import { TeachingOffer } from "./TeachingOffer";

export type SwapRequestStatus='pending' | 'accepted' | 'rejected' | 'completed' | 'cancelled';

export interface SwapRequest {
    requester :number,
    provider :string,
    offer:TeachingOffer,
    message:string,
    status:string,
    created_at :string,
    updated_at:string

}