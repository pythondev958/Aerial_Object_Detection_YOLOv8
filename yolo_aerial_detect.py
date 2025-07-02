import os
import cv2
from ultralytics import YOLO

def process_videos(input_folder='videos', output_folder='outputs', model_path='yolov8l.pt'):
    # Load YOLOv8 model (larger = more accurate, try custom trained model if needed)
    model = YOLO(model_path)

    # Create output folder if not exists
    os.makedirs(output_folder, exist_ok=True)

    # Process each video in input folder
    for video_file in os.listdir(input_folder):
        if not video_file.lower().endswith(('.mp4', '.avi', '.mov')):
            continue

        input_path = os.path.join(input_folder, video_file)
        output_path = os.path.join(output_folder, f'annotated_{video_file}')

        cap = cv2.VideoCapture(input_path)
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        fps = cap.get(cv2.CAP_PROP_FPS)
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

        print(f'Processing {video_file}...')

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            # YOLOv8 inference on frame
            results = model(frame)

            # Render detections on frame
            annotated_frame = results[0].plot()

            out.write(annotated_frame)

            # Optional: display live window
            cv2.imshow('Aerial Object Detection', annotated_frame)
            if cv2.waitKey(1) & 0xFF == 27:  # ESC to quit early
                break

        cap.release()
        out.release()
        print(f'Saved annotated video to {output_path}')

    cv2.destroyAllWindows()

if __name__ == '__main__':
    # You can replace this with a model trained to detect tractors
    process_videos(model_path='yolov8l.pt')
