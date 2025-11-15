export type UserRole = 'super_admin' | 'university_admin';

export interface Token {
  access_token: string;
  token_type: string;
}

export interface University {
  id: number;
  name: string;
}

export interface UniversityCreate {
  name: string;
}

export interface UserCreate {
  username: string;
  password: string;
  role: UserRole;
  university_id?: number | null;
}

export interface UserInDB {
  id: number;
  username: string;
  role: UserRole;
  university?: University | null;
}

export interface Group {
  id: number;
  name: string;
  university_id: number;
}

export interface GroupBase {
  name: string;
}

export interface Teacher {
  id: number;
  full_name: string;
  university_id: number;
}

export interface TeacherBase {
  full_name: string;
}

export interface Subject {
  id: number;
  name: string;
  university_id: number;
}

export interface SubjectBase {
  name: string;
}

export interface ScheduleEvent {
  id: number;
  start_time: string;
  end_time: string;
  classroom: string;
  subject_id: number;
  teacher_id: number;
  group_id: number;
  university_id: number;
  subject: Subject;
  teacher: Teacher;
  group: Group;
}

export interface ScheduleEventCreate {
  start_time: string;
  end_time: string;
  classroom: string;
  subject_id: number;
  teacher_id: number;
  group_id: number;
}

export interface ValidationError {
  loc: (string | number)[];
  msg: string;
  type: string;
}

export interface HTTPValidationError {
  detail: ValidationError[];
}

