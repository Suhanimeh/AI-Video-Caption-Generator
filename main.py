from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import tempfile, os, time
from model import load_model, generate_caption
from utils import extract_key_frame

app = FastAPI(title="AI Video Caption Generator")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

processor, model = load_model()

@app.post("/generate-caption")
async def caption_video(file: UploadFile = File(...)):
    if not file.filename.endswith((".mp4", ".avi")):
        raise HTTPException(status_code=400, detail="Invalid file type. Only .mp4 and .avi allowed.")
    if file.size == 0:
        raise HTTPException(status_code=400, detail="Uploaded file is empty.")

    start = time.time()
    with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(file.filename)[1]) as tmp:
        tmp.write(await file.read())
        tmp_path = tmp.name

    try:
        frame = extract_key_frame(tmp_path)
        if frame is None:
            raise HTTPException(status_code=422, detail="Could not extract frames from video.")
        caption, confidence = generate_caption(processor, model, frame)
        elapsed = round(time.time() - start, 2)
        return {"caption": caption, "confidence": confidence, "processing_time": elapsed}
    finally:
        os.unlink(tmp_path)
