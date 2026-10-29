import cv2
import numpy as np
from PIL import Image

def extract_key_frame(video_path: str) -> Image.Image | None:
    """Extract a representative key frame from a video."""
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        return None

    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    # Seek to 10% into the video for a meaningful scene
    target = max(0, int(total_frames * 0.10))
    cap.set(cv2.CAP_PROP_POS_FRAMES, target)

    ret, frame = cap.read()
    cap.release()

    if not ret or frame is None:
        return None

    return Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

def scene_changed(frame_a: np.ndarray, frame_b: np.ndarray, threshold: float = 30) -> bool:
    """Detect scene change between two frames."""
    g1 = cv2.cvtColor(frame_a, cv2.COLOR_BGR2GRAY)
    g2 = cv2.cvtColor(frame_b, cv2.COLOR_BGR2GRAY)
    return float(np.mean(cv2.absdiff(g1, g2))) > threshold
