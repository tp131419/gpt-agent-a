from fastapi import APIRouter

router = APIRouter()

@router.post("/plugin/essay_grader")
def grade_essay(content: str):
    word_count = len(content.split())
    score = min(100, word_count // 2 + 60)
    return {"word_count": word_count, "estimated_score": score}

def register_plugin(app):
    app.include_router(router)
