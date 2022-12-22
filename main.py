import sqlite3

# Connect to the database
conn = sqlite3.connect("tasks.db")

# Create the tasks table if it doesn't exist
conn.execute("CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY, task TEXT)")

def create_task(task):
    # Insert a new task into the tasks table
    conn.execute("INSERT INTO tasks (task) VALUES (?)", (task,))
    conn.commit()

def edit_task(task_id, task):
    # Update the task with the given ID in the tasks table
    conn.execute("UPDATE tasks SET task = ? WHERE id = ?", (task, task_id))
    conn.commit()

def delete_task(task_id):
    # Delete the task with the given ID from the tasks table
    conn.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()

def get_tasks():
    # Retrieve all tasks from the tasks table
    cursor = conn.execute("SELECT * FROM tasks")
    tasks = []
    for row in cursor:
        task_id = row[0]
        task = row[1]
        tasks.append((task_id, task))
    return tasks

# Test the functions
create_task("Take out the trash")
create_task("Do the dishes")

tasks = get_tasks()
print(tasks)  # [(1, "Take out the trash"), (2, "Do the dishes")]

edit_task(1, "Take out the garbage")

tasks = get_tasks()
print(tasks)  # [(1, "Take out the garbage"), (2, "Do the dishes")]

delete_task(2)

tasks = get_tasks()
print(tasks)  # [(1, "Take out the garbage")]

# Close the database connection
conn.close()
