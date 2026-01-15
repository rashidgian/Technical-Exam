from app.db.database import Database
from app.models.task import Task

class TaskManager:
    # Task Related Operations

    ALLOWED_STATUSES = ["Pending", "In Progress", "Completed"]

    def __init__(self):
        self.db = Database()

    # -------------------- ADD TASK --------------------
    def add_task(self, task: Task):
        query = """
        INSERT INTO tasks (title, description, due_date, priority, status)
        VALUES (%s, %s, %s, %s, %s)
        """
        self.db.execute(query, (
            task.title,
            task.description,
            task.due_date,
            task.priority,
            task.status
        ))

    # -------------------- LIST TASKS WITH OPTIONAL FILTER --------------------
    def list_tasks(self, filter_by=None, filter_value=None):
        query = "SELECT * FROM tasks"
        params = ()

        if filter_by and filter_value:
            # Ensure filter_by matches actual column names
            if filter_by not in ["due_date", "priority", "status"]:
                raise ValueError("Invalid filter field")
            query += f" WHERE {filter_by}=%s"
            params = (filter_value,)

        query += " ORDER BY task_id ASC" # If left blank, order by task_id
        return self.db.execute(query, params)

    # -------------------- MARK TASK AS COMPLETED --------------------
    def mark_completed(self, task_id):
        task_id = int(task_id)
        query = "UPDATE tasks SET status='Completed' WHERE task_id=%s"
        self.db.execute(query, (task_id,))

    # -------------------- UPDATE TASK DETAILS --------------------
    def update_task(self, task_id, title=None, description=None, due_date=None, priority=None, status=None):
        fields = []
        params = []

        if title:
            fields.append("title=%s")
            params.append(title)
        if description:
            fields.append("description=%s")
            params.append(description)
        if due_date:
            fields.append("due_date=%s")
            params.append(due_date)
        if priority:
            fields.append("priority=%s")
            params.append(priority)
        if status:
            if status not in self.ALLOWED_STATUSES:
                raise ValueError("Invalid status")
            fields.append("status=%s")
            params.append(status)

        if not fields:
            print("Nothing to update")
            return

        task_id = int(task_id)
        params.append(task_id)

        # Use task_id to match DB column
        query = f"UPDATE tasks SET {', '.join(fields)} WHERE task_id=%s"
        print("Executing query:", query)
        print("With params:", params)
        self.db.execute(query, tuple(params))
        
    # -------------------- DELETE TASK --------------------
    def delete_task(self, task_id):
        """Delete a task by its task_id."""
        task_id = int(task_id)
        query = "DELETE FROM tasks WHERE task_id=%s"
        self.db.execute(query, (task_id,))

