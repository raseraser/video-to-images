import cv2
import os
import argparse

def extract_frames(video_path, output_dir, fps):
    # 創建輸出目錄（如果不存在）
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 打開影片檔案
    video = cv2.VideoCapture(video_path)

    # 獲取影片的幀率
    video_fps = video.get(cv2.CAP_PROP_FPS)
    
    # 計算需要跳過的幀數
    frame_interval = int(video_fps / fps)

    frame_count = 0
    saved_count = 0

    while True:
        # 讀取一幀
        success, frame = video.read()
        if not success:
            break

        # 每 frame_interval 幀保存一次
        if frame_count % frame_interval == 0:
            # 計算當前時間（秒）
            time = frame_count / video_fps
            # 保存圖片，檔名格式為 "時間_幀數.jpg"
            filename = f"{output_dir}/{time:.2f}_{saved_count:05d}.jpg"
            cv2.imwrite(filename, frame)
            saved_count += 1

        frame_count += 1

    video.release()
    print(f"已保存 {saved_count} 張圖片到 {output_dir}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="將影片轉換為序列圖片")
    parser.add_argument("video_path", help="輸入影片的路徑")
    parser.add_argument("output_dir", help="輸出圖片的目錄")
    parser.add_argument("fps", type=float, help="每秒要保存的圖片數")

    args = parser.parse_args()

    extract_frames(args.video_path, args.output_dir, args.fps)
