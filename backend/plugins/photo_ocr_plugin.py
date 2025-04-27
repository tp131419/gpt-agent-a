from fastapi import APIRouter, File, UploadFile
import easyocr
import os

router = APIRouter()

ocr_reader = easyocr.Reader(["ch_sim", "en"], gpu=False)

@router.post("/plugin/ocr_image")
async def ocr_image(file: UploadFile = File(...)):
    upload_dir = "uploads"
    os.makedirs(upload_dir, exist_ok=True)
    file_path = os.path.join(upload_dir, file.filename)

    with open(file_path, "wb") as f:
        f.write(await file.read())

    results = ocr_reader.readtext(file_path, detail=0)
    extracted_text = "\\n".join(results)

    return {"recognized_text": extracted_text}
    
def register_plugin(app):
    app.include_router(router)
