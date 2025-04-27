from fastapi import APIRouter
import sqlite3
from datetime import datetime

router = APIRouter()

DB_FILE = "gpt_agent.db"

@router.get("/api/notifications")
def get_notifications(user_id: str):
    today = datetime.now().strftime("%Y-%m-%d")
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()

    c.execute("SELECT COUNT(*) FROM review_tasks WHERE user_id = ? AND review_date = ? AND status = 'pending'", (user_id, today))
    review_count = c.fetchone()[0]

    c.execute("SELECT COUNT(*) FROM learning_plan WHERE user_id = ? AND date = ?", (user_id, today))
    plan_count = c.fetchone()[0]

    conn.close()

    notifications = []
    if review_count > 0:
        notifications.append(f"📚 今日待复习 {review_count} 条")
    if plan_count > 0:
        notifications.append("📝 今日有新的学习计划")

    return {"notifications": notifications}
