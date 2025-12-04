from gtts import gTTS
import pygame
import io
import os

def play_farsi_audio(text):
    try:
        # ایجاد صوت در memory
        tts = gTTS(text=text, lang='fa', slow=False)
        
        # ذخیره در memory به جای فایل
        audio_file = io.BytesIO()
        tts.write_to_fp(audio_file)
        audio_file.seek(0)
        
        # پخش با pygame
        pygame.mixer.init()
        pygame.mixer.music.load(audio_file)
        pygame.mixer.music.play()
        
        # منتظر ماندن تا پخش تمام شود
        while pygame.mixer.music.get_busy():
            pygame.time.wait(100)
            
        print("✅ پخش صوت کامل شد!")
        
    except Exception as e:
        print(f"❌ خطا در پخش صوت: {e}")

# استفاده
user_text = input("لطفاً متن فارسی خود را وارد کنید: ")
play_farsi_audio(user_text)