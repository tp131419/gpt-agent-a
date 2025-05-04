from fastapi import FastAPI
from backend.plugin_loader import load_plugins
from backend.notification_api import router as notification_router
from backend.review_api import router as review_router

app = FastAPI()

# 加载插件
load_plugins(app)

# 挂载系统API
app.include_router(notification_router)
app.include_router(review_router)

@app.get("/")
def root():
    return {"message": "GPT-Agent Demo v1 is running!"}
