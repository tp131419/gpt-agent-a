import sqlite3

DB_FILE = "gpt_agent.db"

def init_db():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()

    # 学习计划表
    c.execute("""
    CREATE TABLE IF NOT EXISTS learning_plan (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id TEXT,
        date TEXT,
        today_task TEXT,
        weekly_focus TEXT,
        monthly_goal TEXT
    )
    """)

    # 错题记录表
    c.execute("""
    CREATE TABLE IF NOT EXISTS mistakes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id TEXT,
        question TEXT,
        correct_answer TEXT,
        user_answer TEXT,
        category TEXT,
        timestamp TEXT
    )
    """)

    # 成就积分表
    c.execute("""
    CREATE TABLE IF NOT EXISTS achievements (
        user_id TEXT PRIMARY KEY,
        score INTEGER,
        streak INTEGER,
        last_check TEXT,
        badges TEXT
    )
    """)

    # 复习任务表
    c.execute("""
    CREATE TABLE IF NOT EXISTS review_tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id TEXT,
        content TEXT,
        review_date TEXT,
        status TEXT DEFAULT 'pending'
    )
    """)

    conn.commit()
    conn.close()
