from fastapi import APIRouter

router = APIRouter()

@router.get("/plugin/knowledge_recommend")
def recommend_topic(base_topic: str):
    related = {
        "牛顿定律": ["惯性", "加速度", "质量"],
        "光合作用": ["叶绿体", "太阳能", "葡萄糖合成"]
    }
    return {"related_topics": related.get(base_topic, ["暂无推荐"])}

def register_plugin(app):
    app.include_router(router)
