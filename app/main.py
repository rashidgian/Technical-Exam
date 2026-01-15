from app.services.task_manager import TaskManager
from app.models.task import Task
from app.utils.validators import validate_date
import sys
import os

# Ensure current directory is in sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))


def main():
    manager = TaskManager()

    while True:
        print("\n--- Task Manager ---")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Mark Task Completed")
        print("4. Update Task")
        print("5. Delete Task")
        print("6. Exit")
        
        choice = input("Choose an option: ").strip()

        try:
            # -------------------- ADD TASK --------------------
            if choice == "1":
                title = input("Title: ").strip()
                description = input("Description: ").strip()
                due_date = validate_date(input("Due date (YYYY-MM-DD): ").strip())
                priority = input("Priority (Low/Medium/High): ").strip().title()
                if priority not in ["Low", "Medium", "High"]:
                    print("Invalid priority. Defaulting to 'Low'.")
                    priority = "Low"

                task = Task(title, description, due_date, priority)
                manager.add_task(task)
                print("Task added successfully.")

            # -------------------- LIST TASKS --------------------
            elif choice == "2":
                filter_by_input = input("Filter by (due_date / priority / status / leave blank): ").strip()
                filter_value = None
                if filter_by_input:
                    filter_value = input(f"Value for {filter_by_input}: ").strip()
                tasks = manager.list_tasks(filter_by=filter_by_input or None, filter_value=filter_value or None)

                if not tasks:
                    print("No tasks found.")
                else:
                    print("\n--- Tasks ---")
                    for t in tasks:
                        print(f"[{t['task_id']}] {t['title']} - {t['description']} - {t['status']} - Due: {t['due_date']} - Priority: {t['priority']}")

            # -------------------- MARK COMPLETED --------------------
            elif choice == "3":
                tasks = manager.list_tasks()
    
                if not tasks:
                    print("No tasks found to update.")
                    continue

                # Display tasks
                print("\n--- Tasks ---")
                for t in tasks:
                    print(f"[{t['task_id']}] {t['title']} - {t['description']} - {t['status']} - Due: {t['due_date']} - Priority: {t['priority']}")
                task_id_input = input("Task ID to mark as completed: ").strip()
                try:
                    task_id = int(task_id_input)
                    manager.mark_completed(task_id)
                    print("Task marked as completed.")
                except ValueError:
                    print("Task ID must be a number.")

            # -------------------- UPDATE TASK --------------------
            elif choice == "4":
                tasks = manager.list_tasks()
    
                if not tasks:
                    print("No tasks found to update.")
                    continue

                # Display tasks
                print("\n--- Tasks ---")
                for t in tasks:
                    print(f"[{t['task_id']}] {t['title']} - {t['description']} - {t['status']} - Due: {t['due_date']} - Priority: {t['priority']}")
                task_id_input = input("Task ID to update: ").strip()
                try:
                    task_id = int(task_id_input)
                except ValueError:
                    print("Task ID must be a number.")
                    continue

                print("Leave field blank if no change")
                title = input("New Title: ").strip() or None
                description = input("New Description: ").strip() or None

                due_date_input = input("New Due Date (YYYY-MM-DD): ").strip()
                due_date = validate_date(due_date_input) if due_date_input else None

                priority_input = input("New Priority (Low/Medium/High): ").strip()
                priority = priority_input.title() if priority_input else None

                status_input = input("New Status (Pending/In Progress/Completed): ").strip()
                status = status_input.title() if status_input else None

                try:
                    manager.update_task(task_id, title, description, due_date, priority, status)
                    print("Task updated successfully.")
                except ValueError as ve:
                    print(f"Error: {ve}")

            # -------------------- DELETE TASK --------------------
            elif choice == "5":
                tasks = manager.list_tasks()
                if not tasks:
                    print("No tasks to delete.")
                    continue

                print("\n--- Tasks ---")
                for t in tasks:
                    print(f"[{t['task_id']}] {t['title']} - {t['description']} - {t['status']} - Due: {t['due_date']} - Priority: {t['priority']}")

                task_id_input = input("Task ID to delete: ").strip()
                try:
                    task_id = int(task_id_input)
                    manager.delete_task(task_id)
                    print("Task deleted successfully.")
                except ValueError:
                    print("Task ID must be a number.")


            # -------------------- EXIT --------------------
            elif choice == "6":
                print("Exiting Task Manager!")
                break

            else:
                print("Invalid option. Please choose a number from 1 to 6.")

        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
