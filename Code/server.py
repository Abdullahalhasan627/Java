# from PIL import Image
# import pyscreenshot as ImageGrab  # لأخذ لقطة شاشة كاملة

# # قم بأخذ لقطة شاشة كاملة
# screenshot = ImageGrab.grab()

# # حفظ الصورة في ملف
# screenshot.save('screenshot.png')

# print('تم أخذ الصورة وحفظها كـ screenshot.png')


# import cv2

# # تهيئة كاميرا الويب
# cap = cv2.VideoCapture(0)  # رقم 0 يشير إلى الكاميرا الافتراضية

# # التقاط صورة
# ret, frame = cap.read()

# if ret:
#     # حفظ الصورة في ملف
#     cv2.imwrite('webcam_capture.png', frame)
#     print('تم أخذ صورة من كاميرا الويب وحفظها كـ webcam_capture.png')
# else:
#     print('فشل في التقاط صورة من كاميرا الويب')

# # إغلاق كاميرا الويب
# cap.release()


# import sounddevice as sd
# import wavio
# import numpy as np

# # تعيين معلمات التسجيل
# duration = 10  # المدة بالثواني
# sample_rate = 44100  # معدل العينات (عينة في الثانية)

# # تسجيل الصوت
# print("بدء التسجيل...")
# audio_data = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=2)
# sd.wait()
# print("انتهى التسجيل!")

# # حفظ الصوت في ملف WAV
# output_file = "C:\\Users\\alhas\\Desktop\\recorded_audio.wav"
# print(f"حفظ الصوت في {output_file}...")
# wavio.write(output_file, audio_data, sample_rate, sampwidth=3)
# print(f"تم حفظ الصوت في {output_file}")

# from pynput.keyboard import Key, Listener

# # تعريف متغير لتخزين السجل
# log = ""

# # دالة تسجيل الضغطات
# def on_press(key):
#     global log
#     try:
#         log += str(key.char)
#     except AttributeError:
#         if key == Key.space:
#             log += " "
#         else:
#             log += f"[{key}]"

#     if key == Key.esc:
#         # إذا تم الضغط على مفتاح الخروج (Esc)، احفظ السجل في ملف وقم بإيقاف التسجيل
#         with open("keylog.txt", "w") as file:
#             file.write(log)
#         return False

# # تكوين واستماع لحدث الضغط على لوحة المفاتيح
# with Listener(on_press=on_press) as listener:
#     listener.join()

# from pynput.keyboard import Controller, Key
# import time

# keyboard = Controller()

# # تعطيل لوحة المفاتيح
# def disable_keyboard():
#     while True:
#         keyboard.press(Key.enter)  # يمكنك استبدال Key.enter بأي مفتاح آخر مثل Key.esc
#         keyboard.release(Key.enter)  # نقوم بالضغط ثم الإطلاق للمفتاح
#         time.sleep(0.1)  # توقف لمدة 100 مللي ثانية بين كل ضغطة وإطلاق

# # لإيقاف تعطيل لوحة المفاتيح، يمكنك إيقاف تشغيل البرنامج
# disable_keyboard()

# from pynput.mouse import Controller
# import time

# mouse = Controller()

# # تعطيل الماوس
# def disable_mouse():
#     while True:
#         mouse.position = (0, 0)  # تعيين مؤشر الماوس إلى إحداثيات مكان غير مرئي
#         time.sleep(0.1)  # توقف لمدة 100 مللي ثانية بين كل تعيين لإحداثيات الماوس

# # لإيقاف تعطيل الماوس، يمكنك إيقاف تشغيل البرنامج
# disable_mouse()


# import socket

# def get_local_ip_addresses():
#     host_name = socket.gethostname()
#     ip_addresses = socket.gethostbyname_ex(host_name)
#     return ip_addresses

# if __name__ == "__main__":
#     ip_addresses = get_local_ip_addresses()
#     print("عناوين IP على الشبكة:")
#     for ip in ip_addresses[2]:
#         print(ip)

import requests

# url = 'https://www.facebook.com'
# response = requests.get(url)

# print(response.text)  # يطبع محتوى الصفحة الواردة في الرد
########################
# url = 'https://www.facebook.com'
# data = {'key1': 'value1', 'key2': 'value2'}
# response = requests.post(url, data=data)

# print(response.text)  # يطبع الرد من الخادم
########################
# url = 'https://www.facebook.com'
# headers = {'User-Agent': 'My Custom User Agent'}
# response = requests.get(url, headers=headers)

# print(response.text)
#######################
# URL لملف الفيديو
# video_url = 'https://www.example.com/video.mp4'

# # إرسال طلب GET لجلب الملف
# response = requests.get(video_url)

# # التحقق من أن الاستجابة ناجحة (رمز الاستجابة 200)
# if response.status_code == 200:
#     # افتح ملف جديد للكتابة وحفظ المحتوى فيه
#     with open('video.mp4', 'wb') as video_file:
#         video_file.write(response.content)
#     print('تم تنزيل الفيديو بنجاح.')
# else:
#     print('حدث خطأ أثناء تنزيل الفيديو.')
###########################
# from pytube import YouTube

# # URL لمقطع الفيديو على YouTube
# video_url = 'https://youtu.be/ntCv3wWAvTI?si=VPPLmGsbICXWR9jh'

# # إنشاء كائن YouTube
# yt = YouTube(video_url)

# # اختيار دقة الفيديو (اختياري)
# stream = yt.streams.get_highest_resolution()

# # تنزيل الفيديو إلى ملف
# stream.download(output_path='downloaded_videos/')

# print('تم تنزيل الفيديو بنجاح.')


# from pytube import YouTube
# from moviepy.editor import *

# # URL لمقطع الفيديو على YouTube
# video_url = 'https://youtu.be/WpK5jYSz9HQ?si=c8bUqtsa2Ro0TEzj'

# # إنشاء كائن YouTube
# yt = YouTube(video_url)

# # اختيار دقة الفيديو (اختياري)
# stream = yt.streams.get_highest_resolution()

# #تنزيل الفيديو إلى ملف مؤقت
# temp_video_path = 'temp_video.mp4'
# stream.download(output_path=temp_video_path)

# # تحويل ملف الفيديو إلى ملف صوتي MP3
# video_clip = VideoFileClip('./temp_video.mp4/music.mp4')
# audio_clip = video_clip.audio

# # ملف الإخراج للصوت
# output_audio_path = 'output_audio.mp3'

# # حفظ الملف الصوتي MP3
# audio_clip.write_audiofile(output_audio_path)

# # إغلاق المقاطع
# audio_clip.close()
# video_clip.close()

# print('تم تحويل الفيديو إلى MP3 بنجاح.')




# from pytube import YouTube
# from moviepy.editor import *

# # URL لمقطع الفيديو على YouTube
# video_url = 'https://www.youtube.com/watch?v=your_video_id_here'

# # إنشاء كائن YouTube
# yt = YouTube(video_url)

# # اختيار دقة الفيديو (اختياري)
# stream = yt.streams.get_highest_resolution()

# # تنزيل الفيديو إلى ملف مؤقت
# temp_video_path = 'temp_video.mp4'
# stream.download(output_path=temp_video_path)

# # تحويل ملف الفيديو إلى ملف صوتي MP3
# video_clip = VideoFileClip(temp_video_path)
# audio_clip = video_clip.audio

# # ملف الإخراج للصوت
# output_audio_path = 'output_audio.mp3'

# # حفظ الملف الصوتي MP3
# audio_clip.write_audiofile(output_audio_path)

# # إغلاق المقاطع
# audio_clip.close()
# video_clip.close()

# print('تم تحويل الفيديو إلى MP3 بنجاح.')

# from pytube import YouTube

# # رابط مقطع الفيديو على YouTube
# video_url = 'https://youtu.be/a7G6jXr65Ek?si=7UgpxsmAkwwCiIH8'

# # إنشاء كائن YouTube
# link = YouTube(video_url)

# # اختيار دقة الفيديو
# stream = link.streams.filter(res='144p').first()

# # تحديد مجلد الإخراج
# output_path = 'downloads_video/'

# # تنزيل الفيديو
# stream.download(output_path=output_path)

# print('تم تنزيل الفيديو بجودة 144p بنجاح.')

# import webbrowser

# url = "https://www.google.com"

# webbrowser.open(url)
<<<<<<< HEAD

# import tkinter as tk
# from tkinter import filedialog
# from moviepy.editor import VideoFileClip

# def convert_video_to_audio():
#     # اختيار ملف الفيديو
#     video_file_path = filedialog.askopenfilename(title="اختر ملف الفيديو", filetypes=[("ملفات الفيديو", "*.mp4 *.avi *.mkv")])

#     if not video_file_path:
#         return

#     # اختيار مكان حفظ ملف الصوت
#     audio_file_path = filedialog.asksaveasfilename(title="اختر مكان حفظ ملف الصوت", defaultextension=".mp3", filetypes=[("ملفات MP3", "*.mp3")])

#     if not audio_file_path:
#         return

#     try:
#         # قراءة الفيديو واستخراج الصوت
#         video_clip = VideoFileClip(video_file_path)
#         audio_clip = video_clip.audio

#         # حفظ ملف الصوت
#         audio_clip.write_audiofile(audio_file_path)

#         # إعلام المستخدم بأن العملية تمت بنجاح
#         message_label.config(text="تم تحويل الفيديو إلى ملف صوتي بنجاح!")
#     except Exception as e:
#         # إعلام المستخدم في حالة حدوث خطأ
#         message_label.config(text=f"حدث خطأ: {str(e)}")

# # إعداد نافذة التطبيق
# root = tk.Tk()
# root.title("تحويل الفيديو إلى صوت")

# # إنشاء زر لتحويل الفيديو إلى صوت
# convert_button = tk.Button(root, text="تحويل الفيديو إلى صوت", command=convert_video_to_audio)
# convert_button.pack(pady=20)

# # إنشاء علامة لعرض رسائل الحالة
# message_label = tk.Label(root, text="")
# message_label.pack()

# # إنشاء زر للإغلاق
# close_button = tk.Button(root, text="إغلاق", command=root.destroy)
# close_button.pack()

# root.mainloop()
=======
>>>>>>> cb7387f97b610a242f7d1d0cdc17746a22e573fc



# from cryptography.fernet import Fernet

# # إنشاء مفتاح سري
# key = Fernet.generate_key()

# # إنشاء كائن Fernet باستخدام المفتاح السري
# fernet = Fernet(key)

# # افتح الملف الأصلي للقراءة
# with open('ملف_المدخلات.txt', 'rb') as file:
#     original_data = file.read()

# # قم بتشفير البيانات
# encrypted_data = fernet.encrypt(original_data)

# # احفظ البيانات المشفرة في ملف آخر
# with open('ملف_المخرجات.txt', 'wb') as file:
#     file.write(encrypted_data)

# print("تم تشفير الملف بنجاح.")



# import paramiko

# def run_host(ip, username, password, rport, verbosity) :

#     client = paramiko.SSHClient()
#     client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

#     client.connect(ip=ip, username=username, password=password, port=rport, timeout=30)

#     if verbosity:
#         print(f'نجاح: {username}@{ip}:{rport} - كلمة المرور: {password}')
#     # سجل النجاحات في قاعدة البيانات وتابع معالجة النجاحات
#     # استبدل هذه الجمل بالشيفرة التي تستخدمها للتسجيل في قاعدة البيانات


# ip = "192.168.1.170"
# username = "alhas"
# password = "A2005.m1979"
# rport = 22
# verbosity = True

# run_host(ip, username, password, rport, verbosity)


