
# TikTok Video Generator

This project generates TikTok-style videos using OpenAI's GPT-3.5-turbo for script generation, DALL-E for image generation, and MoviePy for video editing and assembly. The script combines text-to-speech (TTS) audio, generated images, and background music to create a complete video in portrait orientation (720x1280).

## Features

- **Script Generation**: Automatically generates a script based on a given topic using GPT-3.5-turbo.
- **Image Generation**: Generates images that correspond to the key points of the script using DALL-E.
- **Text-to-Speech**: Converts the script to speech using Google Text-to-Speech (gTTS).
- **Video Creation**: Combines the generated images, speech audio, and background music into a TikTok-style video.
- **Captions**: Adds captions synchronized with the spoken script.
- **Portrait Orientation**: Outputs video in a 720x1280 resolution to match TikTok's portrait format.

## Requirements

- Python 3.x
- OpenAI API Key
- Required Python libraries:
  - `openai`
  - `moviepy`
  - `requests`
  - `gtts`

Install the required libraries using pip:

```bash
pip install openai moviepy requests gtts
```

## Usage

1. **Set Up OpenAI API Key**: Ensure you have your OpenAI API key set up in your environment.

2. **Replace File Paths**:
   - Replace `"path/to/your/music.mp3"` in the script with the path to your background music file.

3. **Run the Script**:
   - Run the Python script `create_tiktok_video.py` and specify the topic for the video.

4. **Output**:
   - The script will generate a video file named `tiktok_video.mp4` in the current directory.

## Example

```python
# Example usage
topic = "artificial intelligence"
background_music = "path/to/your/music.mp3"
create_tiktok_video(topic, background_music)
```

## Customization

- **Text Styles**: You can customize the font size, color, and background of the captions by modifying the `create_video` function in the script.
- **Video Effects**: Additional video effects such as fade-in and fade-out can be added in the `add_effects` function.

## License

This project is licensed under the MIT License.
