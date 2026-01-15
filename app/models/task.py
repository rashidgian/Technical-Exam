from datetime import datetime

class Task:
    """Represents a task entity."""
    
    ALLOWED_STATUSES = ["Pending", "In Progress", "Completed"]
    ALLOWED_PRIORITIES = ["Low", "Medium", "High"]

    def __init__(self, title, description, due_date, priority, status="Pending"):
        if status not in self.ALLOWED_STATUSES:
            raise ValueError(f"Invalid status: {status}")
        if priority.title() not in self.ALLOWED_PRIORITIES:
            raise ValueError(f"Invalid priority: {priority}")

        self.id = None
        self.title = title
        self.description = description
        self.due_date = due_date
        self.priority = priority.title()
        self.status = status
        self.created_at = datetime.now()  # optional; useful for in-memory tasks

    def mark_completed(self):
        """Mark this task as completed."""
        self.status = "Completed"
