from fastapi import APIRouter

router = APIRouter()

@router.get("/plugin/generate_practice")
def generate_practice(subject: str):
    samples = {
        "物理": ["解释牛顿第一定律", "计算一个物体加速度"],
        "英语": ["用英文写一篇假期短文", "翻译：我喜欢学习人工智能"]
    }
    return {"practice_questions": samples.get(subject, ["暂无题目"])}

def register_plugin(app):
    app.include_router(router)
