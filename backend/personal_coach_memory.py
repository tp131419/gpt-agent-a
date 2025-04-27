import json
import os

MEMORY_FILE = "coach_memory.json"

def load_memory():
    if not os.path.exists(MEMORY_FILE):
        return {}
    with open(MEMORY_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_memory(data):
    with open(MEMORY_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def get_student_profile(user_id):
    data = load_memory()
    return data.get(user_id, {
        "兴趣领域": [],
        "喜欢的风格": "温柔鼓励",
        "易错领域": [],
        "学习习惯": "晚上学习",
        "连续对话历史": [],
        "语言偏好": "中文"
    })

def update_student_profile(user_id, key, value):
    data = load_memory()
    if user_id not in data:
        data[user_id] = {
            "兴趣领域": [],
            "喜欢的风格": "温柔鼓励",
            "易错领域": [],
            "学习习惯": "晚上学习",
            "连续对话历史": [],
            "语言偏好": "中文"
        }
    data[user_id][key] = value
    save_memory(data)

def append_chat_history(user_id, user_message, assistant_reply):
    data = load_memory()
    profile = data.setdefault(user_id, {
        "兴趣领域": [],
        "喜欢的风格": "温柔鼓励",
        "易错领域": [],
        "学习习惯": "晚上学习",
        "连续对话历史": [],
        "语言偏好": "中文"
    })
    profile["连续对话历史"].append({"用户": user_message, "AI回复": assistant_reply})
    profile["连续对话历史"] = profile["连续对话历史"][-5:]
    save_memory(data)
