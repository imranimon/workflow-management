export interface Task {
  id: number;
  title: string;
  description: string;
  isDone: boolean;
  workflowId: number;
  order: number;
  userId: number; // User assigned to this task
  prerequisiteTaskId?: number; // Optional prerequisite task ID
}
