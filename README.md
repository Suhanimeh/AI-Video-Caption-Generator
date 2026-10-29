# AI Video Caption Generator

**AI-powered video captioning using BLIP, OpenCV, and FastAPI.**

The AI Video Caption Generator is a web application that generates natural-language descriptions of video content using the pretrained BLIP image-captioning model. It extracts selected frames from uploaded videos, processes them using computer vision techniques, and returns generated captions through a FastAPI backend.

## Live Demo

- **Frontend:** [Try the AI Video Caption Generator](https://glistening-bavarois-f92dd1.netlify.app/)
- **Backend API:** [View the Backend Service](https://video-captioning-app-pgo9.onrender.com)

## Overview

Videos contain large amounts of visual information that can be time-consuming to review manually. This project explores how computer vision and pretrained vision-language models can help describe visual content through automated caption generation.

The application combines a browser-based interface with a Python backend. Users upload a supported video file, OpenCV extracts selected frames, and BLIP generates natural-language descriptions of those frames.

The project demonstrates the integration of video processing, machine learning inference, REST API development, and frontend technologies in a practical AI application.

## Project Objectives

- Explore how pretrained vision-language models generate descriptions of visual content.
- Extract representative frames from videos using OpenCV.
- Integrate an AI model into a web application through a REST API.
- Present generated captions and processing information through a user-friendly interface.
- Understand practical challenges involving model loading, inference time, and video compatibility.

## Features

- **Video Upload:** Supports video uploads in `.mp4` and `.avi` formats, subject to backend validation and codec compatibility.
- **Automatic Frame Extraction:** Uses OpenCV to extract frames for caption generation.
- **AI-Powered Captioning:** Uses the pretrained BLIP model to generate descriptions of selected frames.
- **Confidence Information:** Displays a confidence score if supported by the application's implemented scoring method. This score should not be interpreted as a guarantee of caption accuracy.
- **Processing Time:** Reports processing time when supported by the application.
- **Responsive Interface:** Uses HTML, Vanilla JavaScript, and Tailwind CSS to provide a browser-based user experience.
- **REST API Integration:** Uses FastAPI to connect the frontend with the video-processing and caption-generation pipeline.
- **Cross-Origin Resource Sharing:** Configures CORS to support communication between the separately hosted frontend and backend.

## Technology Stack

| Component | Technologies |
|---|---|
| Backend API | Python, FastAPI, Uvicorn |
| AI Model | Salesforce BLIP, Hugging Face Transformers |
| Video Processing | OpenCV |
| Image Processing | Pillow |
| Machine Learning | PyTorch, NumPy |
| Frontend | HTML, Vanilla JavaScript, Tailwind CSS |
| Deployment | Netlify, Render |

*Ensure that every listed technology is included in the repository's actual implementation and dependencies.*

## How It Works

```text
       Video Upload
            |
            v
     Frontend Interface
            |
            v
       FastAPI Request
            |
            v
     Video Processing
          OpenCV
            |
            v
      Frame Extraction
            |
            v
      BLIP Caption Model
            |
            v
    Generated Captions
            |
            v
      Results Displayed
       in the Browser
```

### Processing Workflow

1. **Video Upload:** The user selects a supported video file through the frontend.
2. **API Request:** The frontend sends the uploaded video to the FastAPI caption-generation endpoint.
3. **Frame Extraction:** OpenCV reads the video and extracts frames using the sampling or scene-selection logic implemented in the backend.
4. **Caption Generation:** The extracted frames are processed by the pretrained BLIP model to generate natural-language descriptions.
5. **Result Display:** The backend returns the generated caption information and any supported processing metrics to the frontend.

**Important:** The generated captions describe selected video frames. They do not necessarily provide a complete summary of every event throughout the video.

## Project Structure

```text
video-caption-app/
├── backend/
│   ├── main.py              # FastAPI application and API endpoint
│   ├── model.py             # BLIP model loading and caption generation
│   ├── utils.py             # Frame extraction and video-processing utilities
│   └── requirements.txt     # Python dependencies
├── frontend/
│   └── index.html           # Frontend interface and JavaScript logic
└── README.md                # Project documentation
```

## Getting Started

### Prerequisites

Before running the application locally, ensure you have:

- Python 3.10 or another version compatible with your dependencies.
- pip for installing Python packages.
- Git for cloning the repository.
- A supported video file for testing.
- Sufficient memory and storage for PyTorch and the pretrained BLIP model.

### 1. Clone the Repository

Replace `YOUR_USERNAME` with your GitHub username and update the repository name if necessary.

```bash
git clone https://github.com/SuhaniMeh/video-caption-app.git
cd video-caption-app
```

### 2. Set Up the Backend

Navigate to the backend directory and create a virtual environment.

```bash
cd backend
python -m venv venv
```

Activate the virtual environment.

**Windows:**

```powershell
venv\Scripts\activate
```

**macOS/Linux:**

```bash
source venv/bin/activate
```

Install the required dependencies.

```bash
pip install -r requirements.txt
```

Start the FastAPI development server.

```bash
uvicorn main:app --reload
```

The backend should now be accessible at:

- **API:** `http://localhost:8000`
- **Interactive API documentation:** `http://localhost:8000/docs`

The first model initialization may take longer because the pretrained model may need to be downloaded and loaded into memory.

### 3. Configure and Open the Frontend

Open `frontend/index.html` in your browser.

Ensure the frontend's API URL points to the local backend:

```javascript
const API_URL = "http://localhost:8000/generate-caption";
```

The variable name and endpoint must match the implementation in your `index.html` and `main.py` files.

### 4. Test the API

You can test the caption-generation endpoint using `curl`:

```bash
curl -X POST http://localhost:8000/generate-caption \
  -F "file=@your_video.mp4"
```

Replace `your_video.mp4` with the path to your test video. This command assumes the endpoint accepts an uploaded file through a multipart form field named `file`.

## Deployment

The application uses separate hosting services for the frontend and backend.

### Backend Deployment with Render

1. Push the backend code to a GitHub repository.
2. Open [Render](https://render.com/) and create a new Web Service.
3. Connect the repository containing the backend.
4. Configure the backend root directory if the repository contains multiple application folders.
5. Set the build command:

   ```bash
   pip install -r requirements.txt
   ```

6. Set the start command:

   ```bash
   uvicorn main:app --host 0.0.0.0 --port $PORT
   ```

7. Configure the Python version and any required environment variables.
8. Deploy the service and verify that the API is accessible.

**Deployment consideration:** PyTorch and BLIP can require substantial memory, storage, and startup time. Confirm that the hosting plan supports the model's resource requirements and expected inference workload.

### Frontend Deployment with Netlify

1. Update the frontend's API URL to point to the deployed backend.
2. Open [Netlify](https://www.netlify.com/).
3. Deploy the `frontend/` directory containing `index.html`.
4. Upload a supported video and verify that captions are returned successfully.

For production deployments, configure CORS to allow only trusted frontend origins rather than permitting requests from every origin.

## Common Issues and Troubleshooting

| Issue | Possible Solution |
|---|---|
| CORS error | Check the backend CORS configuration and ensure the deployed frontend origin is permitted. |
| Slow dependency installation | PyTorch is a large dependency. Consider a compatible CPU-only installation if GPU support is unnecessary. |
| Slow first request | The pretrained model may need to download and initialize before generating captions. |
| Unsupported video | Verify the file format, codec compatibility, and whether OpenCV can read the file. |
| No frames extracted | Check the uploaded file and review the frame-extraction logic, video duration, and frame rate. |
| API timeout or deployment failure | Review server logs, memory usage, model initialization, and hosting resource limits. |
| Frontend cannot reach the backend | Verify the API URL, endpoint path, CORS settings, and backend availability. |

## Potential Applications

- **Accessibility Support:** Generate draft visual descriptions that can help users understand video content.
- **Media Organization:** Create descriptive metadata to support video cataloguing and indexing.
- **Content Management:** Assist in preparing initial descriptions for video assets.
- **Video Analysis Workflows:** Use frame-level captions as an initial step in a broader computer vision pipeline.
- **AI Research and Experimentation:** Explore the practical use of pretrained vision-language models for visual understanding.

These are potential applications rather than validated outcomes of the project. Generated descriptions should be reviewed before being used in accessibility-critical or other high-stakes settings.

## Limitations and Future Improvements

### Current Limitations

- Selected frames may not capture every important event in a video.
- BLIP generates image descriptions and does not inherently understand the complete temporal sequence of a video.
- Generated captions may omit details or incorrectly describe visual content.
- Processing time depends on video duration, frame selection, hardware, and model initialization.
- A confidence score does not necessarily indicate whether a caption is factually correct.
- Large video files may require additional validation, resource limits, and processing safeguards.

### Future Enhancements

- Introduce configurable frame-sampling intervals.
- Combine captions from multiple frames into a concise video-level summary.
- Evaluate caption quality using reference captions, text-based metrics, and human review.
- Add configurable file-size and video-duration limits.
- Improve error handling, loading indicators, and API response validation.
- Introduce asynchronous processing for longer videos.
- Explore temporal video models for better understanding of actions and events.

## Skills Demonstrated

- Python application development
- Computer vision and video-frame processing
- Pretrained vision-language model integration
- Machine learning inference using PyTorch
- REST API development with FastAPI
- Frontend and backend integration
- Application deployment and troubleshooting
- Technical documentation and communication

## Author

**Suhani Mehta**

- **GitHub:** [Suhanimeh](https://github.com/Suhanimeh)
- **Live Frontend:** [AI Video Caption Generator](https://glistening-bavarois-f92dd1.netlify.app/)
- **Backend API:** [FastAPI Backend](https://video-captioning-app-pgo9.onrender.com)

## License

This project is intended to be distributed under the MIT License. See the [`LICENSE`](LICENSE) file for the complete terms.

*Include this statement only if the repository contains the corresponding MIT `LICENSE` file.*
