import openai
import requests
from moviepy.editor import *
from gtts import gTTS
import os

def create_tiktok_video(topic, background_music):
    # Step 1: Generate script using ChatGPT
    script = generate_script(topic)
    
    # Step 2: Extract 5 major points from the script
    major_points = extract_major_points(script)
    
    # Step 3: Generate images using DALL-E (using placeholder images for now)
    images = generate_images(major_points)
    
    # Step 4: Generate speech from script using Google TTS
    audio_file = generate_speech(script)
    
    # Step 5: Combine elements into a video
    video = create_video(major_points, images, audio_file, background_music, script)
    
    # Step 6: Add effects and edit the video (optional effects can be added here)
    edited_video = add_effects(video)
    
    # Step 7: Export and save the video locally
    export_video(edited_video)

def generate_script(topic):
    # Use OpenAI API to generate script
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a TikTok script writer."},
            {"role": "user", "content": f"Write a script for a TikTok video about {topic}"}
        ]
    )
    return response.choices[0].message['content']

def extract_major_points(script):
    # This function would analyze the script and extract 5 major points
    sentences = script.split('.')
    return [sentences[i].strip() for i in range(0, len(sentences), max(1, len(sentences)//5))][:5]

def generate_images(major_points):
    images = []
    for point in major_points:
        # Use OpenAI API to generate image using DALL-E
        response = openai.Image.create(
            prompt=point,
            n=1,
            size="1024x1024"
        )
        image_url = response['data'][0]['url']
        image_path = download_image(image_url, point)
        images.append(image_path)
    return images

def download_image(url, description):
    img_data = requests.get(url).content
    img_filename = f"{description[:10]}.jpg"
    with open(img_filename, 'wb') as handler:
        handler.write(img_data)
    return img_filename

def generate_speech(script):
    # Use gTTS to generate speech from the script
    tts = gTTS(text=script, lang='en')
    audio_file = "speech.mp3"
    tts.save(audio_file)
    return audio_file

def create_video(major_points, images, audio_file, background_music, script):
    clips = []
    text_clips = []
    
    # Create image clips with duration
    for i, img_path in enumerate(images):
        img_clip = ImageClip(img_path).set_duration(3).resize(height=1280).resize(width=720)  # 3 seconds per clip
        txt_clip = TextClip(major_points[i], fontsize=40, color='white', bg_color='black').set_position('bottom').set_duration(3).resize(width=700)
        img_clip = CompositeVideoClip([img_clip, txt_clip])
        clips.append(img_clip)
    
    # Concatenate all the clips
    video = concatenate_videoclips(clips, method="compose")
    
    # Add the generated speech audio
    audio = AudioFileClip(audio_file)
    
    # Add captions (matching the script text) to the video
    caption_clips = []
    duration_per_sentence = video.duration / len(script.split('.'))
    start_time = 0
    for sentence in script.split('.'):
        if sentence.strip() == "":
            continue
        caption_clip = TextClip(sentence.strip(), fontsize=35, color='white', bg_color='black', size=(video.w, 100)).set_position(('center', 'bottom')).set_start(start_time).set_duration(duration_per_sentence)
        caption_clips.append(caption_clip)
        start_time += duration_per_sentence
    
    video = CompositeVideoClip([video, *caption_clips])
    
    # Add background music
    background_music = AudioFileClip(background_music).subclip(0, video.duration)
    final_audio = CompositeAudioClip([audio.volumex(0.7), background_music.volumex(0.3)])
    video = video.set_audio(final_audio)
    
    return video

def add_effects(video):
    # Add additional effects like fade-in, fade-out, etc.
    video = video.fx(vfx.fadein, 1).fx(vfx.fadeout, 1)
    return video

def export_video(video):
    # Export the video and save it locally
    video.write_videofile("tiktok_video.mp4", fps=24)

# Usage
topic = "artificial intelligence"
background_music = "path/to/your/music.mp3"
create_tiktok_video(topic, background_music)
