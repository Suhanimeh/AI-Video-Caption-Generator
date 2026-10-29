AI Video Caption Generator

AI-powered video captioning using BLIP, OpenCV, and FastAPI.

The AI Video Caption Generator is a web application that analyzes video frames and generates natural-language descriptions using the BLIP image-captioning model. It extracts representative frames from an uploaded video, processes them with a pretrained vision-language model, and returns captions through a FastAPI backend.

Live Demo

Frontend: https://glistening-bavarois-f92dd1.netlify.app/

Backend API: https://video-captioning-app-pgo9.onrender.com

Overview

Videos contain large amounts of visual information that can be difficult to review manually. This project explores how computer vision and pretrained AI models can help summarize visual content by generating descriptive captions from selected video frames.

The application combines a browser-based interface with a Python backend. Users upload a supported video, the backend extracts frames using OpenCV, and BLIP generates descriptions of the selected images.

The project demonstrates an applied workflow involving video processing, machine learning inference, API development, and frontend integration.

Project Objectives

Explore how pretrained vision-language models can describe visual content.

Extract representative frames from video files using OpenCV.

Connect an AI model to a web application through a REST API.

Present generated captions and processing information in a user-friendly interface.

Understand practical considerations such as model loading, inference time, and video compatibility.

Features

Video Upload: Accepts supported .mp4 and .avi video files.

Frame Extraction: Uses OpenCV to extract frames for analysis.

AI Caption Generation: Uses the pretrained BLIP model to generate natural-language image descriptions.

Confidence Information: Displays a confidence score when provided by the application's implemented scoring method. This score should not automatically be interpreted as a measure of factual accuracy.

Processing Time: Reports the processing time for caption generation.

Web Interface: Provides a responsive frontend built with HTML, Vanilla JavaScript, and Tailwind CSS.

REST API: Uses FastAPI to handle requests between the frontend and the caption-generation pipeline.

Cross-Origin Support: Configures CORS to allow communication between the separately hosted frontend and backend.

Technology Stack

Component

Technologies

Backend API

Python, FastAPI, Uvicorn

AI Model

Salesforce BLIP, Hugging Face Transformers

Video Processing

OpenCV

Image Processing

Pillow

Machine Learning

PyTorch, NumPy

Frontend

HTML, Vanilla JavaScript, Tailwind CSS

Deployment

Netlify, Render

The table describes the technologies listed for the project. Keep each dependency in the final README only if it is actually used in your codebase.

How It Works

User Uploads a Video
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
   Key-Frame Extraction
         |
         v
    BLIP Caption Model
         |
         v
  Generated Frame Captions
         |
         v
   Results in the Browser

Processing Workflow

Upload: The user selects a supported video file through the frontend.

API Request: The frontend sends the video to the FastAPI caption-generation endpoint.

Frame Extraction: OpenCV reads the video and extracts frames according to the implemented sampling or scene-selection strategy.

Caption Generation: The extracted frames are passed to the pretrained BLIP model, which generates descriptions of their visual content.

Result Display: The application returns the generated caption information and any supported processing metrics to the frontend.

The output describes the selected frames rather than necessarily providing a complete, continuous summary of the entire video.

Project Structure

video-caption-app/
├── backend/
│   ├── main.py              # FastAPI application and API endpoint
│   ├── model.py             # BLIP model loading and caption generation
│   ├── utils.py             # Frame extraction and scene processing
│   └── requirements.txt     # Python dependencies
├── frontend/
│   └── index.html           # Web interface and JavaScript logic
└── README.md                # Project documentation

Run Locally

Prerequisites

Python 3.10 or a compatible version supported by your dependencies

pip

Git

A compatible video file

Sufficient memory and storage for PyTorch and the pretrained BLIP model

1. Clone the Repository

Replace YOUR_USERNAME with your GitHub username and use the actual repository name if it differs.

git clone https://github.com/YOUR_USERNAME/video-caption-app.git
cd video-caption-app

2. Set Up the Backend

cd backend
python -m venv venv

Activate the virtual environment.

Windows:

venv\Scripts\activate

macOS/Linux:

source venv/bin/activate

Install the dependencies:

pip install -r requirements.txt

Start the API server:

uvicorn main:app --reload

The backend should now be available at:

http://localhost:8000

FastAPI's interactive API documentation is typically available at:

http://localhost:8000/docs

3. Start the Frontend

Open frontend/index.html in your browser.

Ensure the API_URL value in the frontend points to the local backend endpoint:

const API_URL = "http://localhost:8000/generate-caption";

The exact variable name and endpoint should match your implementation.

4. Test the API

You can test the endpoint using curl:

curl -X POST http://localhost:8000/generate-caption \
  -F "file=@your_video.mp4"

Replace your_video.mp4 with the path to an actual video file. The request format assumes the endpoint accepts an uploaded file through a multipart form field named file.

Deployment

The project uses separate hosting services for its frontend and backend.

Backend Deployment — Render

Push the backend code to a GitHub repository.

Create a new Web Service in Render.

Connect the repository and configure the backend's root directory if needed.

Set the build command to:

pip install -r requirements.txt

Set the start command to:

uvicorn main:app --host 0.0.0.0 --port $PORT

Configure the Python version and any required environment variables.

Deploy the service and verify that the API responds.

Deployment consideration: PyTorch and the BLIP model can require substantial memory, storage, and startup time. Confirm that the selected hosting plan supports the application's actual resource requirements.

Frontend Deployment — Netlify

Update the frontend's API_URL to the deployed backend endpoint.

Open Netlify.

Deploy the frontend/ directory containing index.html.

Test the live application by uploading a supported video.

For production use, configure CORS to allow only the frontend origins you trust instead of allowing every origin.

Common Issues

Issue

Possible Solution

CORS error

Check the backend CORS configuration and confirm that the deployed frontend origin is allowed.

Slow dependency installation

PyTorch is a large dependency. Use a compatible CPU-only installation when GPU support is unnecessary.

Slow first request

The model may need to download and load before the first prediction.

Unsupported video

Check the file format, video codec, and whether OpenCV can read the file.

No frames extracted

Verify that the uploaded file is readable and that the extraction logic can process its duration and frame rate.

API timeout or deployment failure

Review server logs, resource limits, model-loading time, and the hosting plan's constraints.

Frontend cannot reach the backend

Verify the deployed API URL, endpoint path, and network accessibility.

Potential Applications

Accessibility support: Generate draft visual descriptions that may help users understand video content.

Media organization: Produce descriptive metadata to support video cataloguing and indexing.

Content management: Assist with creating initial descriptions for video assets.

Video analysis workflows: Use frame-level captions as an initial step in a broader computer vision pipeline.

Research and experimentation: Explore the use of pretrained vision-language models for visual understanding.

These are potential applications rather than validated outcomes of this project. Generated captions should be reviewed before being used in accessibility-critical or high-stakes settings.

Limitations and Future Improvements

Current Limitations

Captions describe selected frames and may miss important events occurring between them.

BLIP generates image descriptions; it does not inherently understand the full temporal sequence of a video.

Generated captions can omit details or describe visual content incorrectly.

Processing time depends on video duration, frame sampling, hardware, and model-loading overhead.

Confidence scores, if displayed, do not necessarily measure whether a caption is factually correct.

Large videos may require additional validation, resource limits, and processing safeguards.

Possible Future Enhancements

Add configurable frame-sampling intervals.

Combine captions from multiple frames into a concise video-level summary.

Evaluate caption quality against reference captions using suitable text-based metrics and human review.

Add file-size and video-duration limits.

Improve error handling, loading feedback, and API response validation.

Introduce asynchronous processing for longer videos.

Explore temporal video models for better understanding of actions and events.

Skills Demonstrated

Python application development

Computer vision and video-frame processing

Pretrained vision-language model integration

Machine learning inference using PyTorch

REST API development with FastAPI

Frontend and backend integration

Model deployment and troubleshooting

Technical documentation and project communication

Author

Suhani Mehta

GitHub: https://github.com/Suhanimeh

Live Frontend: https://glistening-bavarois-f92dd1.netlify.app/

Backend API: https://video-captioning-app-pgo9.onrender.com

License

This project is intended to be distributed under the MIT License. See the LICENSE file for the full terms.
