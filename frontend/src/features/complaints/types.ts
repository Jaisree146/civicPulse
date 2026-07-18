export interface CreateComplaintRequest {
  title: string;
  description: string;
  latitude: number;
  longitude: number;
}

export interface Complaint {
  complaint_number: string;
  title: string;
  description: string;
 latitude: number;
 longitude: number;
 status: string;
 created_at: string;
}

export interface CreateComplaintResponse {
  complaint_number: string;
}

export type MyComplaintsResponse = Complaint[];

export type ComplaintDetailsResponse = Complaint;