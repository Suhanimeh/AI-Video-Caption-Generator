#  AI Video Caption Generator

> Smart video understanding powered by BLIP Transformer — upload any video, get an intelligent natural-language caption instantly.
>
> LIVE LINKS
> FRONTEND : https://glistening-bavarois-f92dd1.netlify.app/
> BACKEND: https://video-captioning-app-pgo9.onrender.com

##  Features

- Upload `.mp4` / `.avi` video files
- Automatic key-frame extraction via OpenCV
- AI caption generation with BLIP (Bootstrapping Language-Image Pre-training)
- Confidence score per caption
- Processing time reporting
- Responsive, modern Vanilla JS + Tailwind CSS frontend
- FastAPI backend with CORS support

---

##  Tech Stack

| Layer       | Technology                        |
|-------------|-----------------------------------|
| Backend     | Python, FastAPI, Uvicorn          |
| ML Model    | Salesforce BLIP (HuggingFace)     |
| Vision      | OpenCV, Pillow                    |
| Numerics    | PyTorch, NumPy                    |
| Frontend    | HTML, Vanilla JS, Tailwind CSS    |

---

##  Project Structure

```
video-caption-app/
├── backend/
│   ├── main.py          # FastAPI app & /generate-caption endpoint
│   ├── model.py         # BLIP model loading & caption generation
│   ├── utils.py         # Frame extraction & scene change detection
│   └── requirements.txt
├── frontend/
│   └── index.html       # Full SaaS-style UI (self-contained)
└── README.md
```

---

##  Run Locally

### 1. Backend

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
# API available at http://localhost:8000
```

Test the endpoint directly:
```bash
curl -X POST http://localhost:8000/generate-caption \
  -F "file=@your_video.mp4"
```

### 2. Frontend

```bash
cd frontend
open index.html   # macOS
# or just double-click index.html in Windows/Linux
```

> Make sure `API_URL` in `index.html` points to `http://localhost:8000/generate-caption`.

---

##  Deployment Guide

### Backend → Render

1. Push `backend/` to a GitHub repo
2. Go to [render.com](https://render.com) → **New Web Service**
3. Connect your GitHub repo
4. Set:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`
   - **Environment**: Python 3.11
5. Deploy. Copy the public URL, e.g. `https://your-app.onrender.com`

### Frontend → Netlify / GitHub Pages

1. Edit `index.html` line with `API_URL`:
   ```js
   const API_URL = "https://your-app.onrender.com/generate-caption";
   ```
2. **Netlify**: Drag & drop the `frontend/` folder at [app.netlify.com/drop](https://app.netlify.com/drop)
3. **GitHub Pages**: Push `frontend/index.html` to a repo → Settings → Pages → Deploy from `main`

---

## 🔧 Common Issues

| Issue | Fix |
|-------|-----|
| CORS error in browser | Backend has CORS enabled for `*`; confirm backend is running |
| `torch` install slow | Use `pip install torch --index-url https://download.pytorch.org/whl/cpu` for CPU-only |
| Model download on first run | BLIP downloads ~1GB on first use; subsequent runs use cache |
| Empty video error | Ensure video has at least 10 frames; check codec compatibility |

---

##  Industry Use Cases

- **Accessibility**: Auto-captioning for visually impaired users
- **Media indexing**: Tag and search video libraries by content
- **Surveillance**: Intelligent event summarization
- **Content platforms**: Automatic metadata generation
- **Video analytics**: Scene understanding pipelines

---

##  License

MIT — see `LICENSE` for details.
