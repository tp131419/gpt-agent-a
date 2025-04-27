import sqlite3
from datetime import datetime, timedelta

DB_FILE = "gpt_agent.db"

REVIEW_INTERVALS = [0, 1, 2, 4, 7, 15, 30]

def add_new_learning(user_id, content):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    today = datetime.now().date()
    for interval in REVIEW_INTERVALS:
        review_day = today + timedelta(days=interval)
        c.execute("""
        INSERT INTO review_tasks (user_id, content, review_date, status)
        VALUES (?, ?, ?, 'pending')
        """, (user_id, content, review_day.strftime("%Y-%m-%d")))
    conn.commit()
    conn.close()

def get_today_reviews(user_id):
    today = datetime.now().strftime("%Y-%m-%d")
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("""
    SELECT id, content FROM review_tasks
    WHERE user_id = ? AND review_date = ? AND status = 'pending'
    """, (user_id, today))
    tasks = [{"id": row[0], "content": row[1]} for row in c.fetchall()]
    conn.close()
    return tasks

def complete_review_task(task_id):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("""
    UPDATE review_tasks SET status = 'completed' WHERE id = ?
    """, (task_id,))
    conn.commit()
    conn.close()
