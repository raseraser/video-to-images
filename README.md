# Video to Images Converter

這是一個 Python 腳本，用於將視頻轉換為一系列圖像，並可選擇性地去除背景。它提供了多種選項來控制輸出，包括去背、alpha matting 和後處理。

## 安裝

1. 確保您的系統已安裝 Python 3.6 或更高版本。

2. 克隆或下載此存儲庫到您的本地機器。

3. 進入項目目錄：
   ```
   cd path/to/video-to-images-converter
   ```

4. 安裝所需的依賴庫：
   ```
   pip install opencv-python pillow rembg
   ```

## 使用方式

基本用法：

```
python video-to-images.py <video_path> <output_dir> <fps> [options]
```

參數說明：
- `<video_path>`: 輸入視頻的路徑
- `<output_dir>`: 輸出圖像的目錄
- `<fps>`: 每秒要保存的圖像數量

選項：
- `--remove_bg`: 去除背景
- `--alpha_matting`: 使用 alpha matting 改善邊緣
- `--post_process`: 應用後處理來平滑邊緣
- `--alpha_matting_erode_size`: Alpha matting 的腐蝕大小（默認：10）
- `--alpha_matting_foreground_threshold`: Alpha matting 的前景閾值（默認：240）
- `--alpha_matting_background_threshold`: Alpha matting 的背景閾值（默認：10）

### 範例

1. 基本轉換（不去背）：
   ```
   python video-to-images.py input_video.mp4 output_folder 1
   ```

2. 轉換並去背：
   ```
   python video-to-images.py input_video.mp4 output_folder 1 --remove_bg
   ```

3. 轉換、去背，並使用 alpha matting：
   ```
   python video-to-images.py input_video.mp4 output_folder 1 --remove_bg --alpha_matting
   ```

4. 完整選項：
   ```
   python video-to-images.py input_video.mp4 output_folder 1 --remove_bg --alpha_matting --post_process --alpha_matting_erode_size 15 --alpha_matting_foreground_threshold 230 --alpha_matting_background_threshold 20
   ```

## 注意事項

- 去背和 alpha matting 可能會增加處理時間。
- 如果遇到性能警告，嘗試調整 alpha matting 的參數。
- 確保您有足夠的磁盤空間來存儲輸出的圖像。

## 貢獻

歡迎提出問題和改進建議！請開啟一個 issue 或提交一個 pull request。

## 許可證

[MIT License](https://opensource.org/licenses/MIT)
