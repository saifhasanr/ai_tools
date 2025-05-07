# import os
# import subprocess
# from pdf2docx import Converter
# from docx import Document
# import pytesseract
# from pdf2image import convert_from_path
# import speech_recognition as sr
# from pydub import AudioSegment
# import whisper
# import fitz  # PyMuPDF
# from PyPDF2 import PdfReader, PdfWriter
# from gtts import gTTS
# # from moviepy.editor import VideoFileClip
# from moviepy import *
# from PIL import Image
#
# # Load Whisper Model for Audio Transcription
# model = whisper.load_model("base")
#
# # ==================== Conversion Features ====================
#
# def convert_docx_to_pdf(docx_path, pdf_path):
#     try:
#         subprocess.run(["libreoffice", "--headless", "--convert-to", "pdf", docx_path, "--outdir", os.path.dirname(pdf_path)])
#     except Exception as e:
#         print("Error converting DOCX to PDF:", e)
#
# def convert_pdf_to_docx(pdf_path, docx_path):
#     try:
#         cv = Converter(pdf_path)
#         cv.convert(docx_path)
#         cv.close()
#     except Exception as e:
#         print("Error converting PDF to DOCX:", e)
#
# # ==================== Text Extraction Features ====================
#
# def extract_text_from_pdf(pdf_path):
#     text = ""
#     try:
#         pdf_document = fitz.open(pdf_path)
#         for page in pdf_document:
#             text += page.get_text()
#         return text.strip()
#     except Exception as e:
#         print("Error extracting text from PDF:", e)
#         return ""
#
# def extract_text_from_audio(audio_path):
#     try:
#         result = model.transcribe(audio_path)
#         return result["text"]
#     except Exception as e:
#         print("Error extracting text from audio:", e)
#         return ""
#
# def extract_text_from_image(image_path):
#     try:
#         return pytesseract.image_to_string(Image.open(image_path))
#     except Exception as e:
#         print("Error extracting text from image:", e)
#         return ""
#
# # ==================== PDF Manipulation Features ====================
#
# def compress_pdf(input_path, output_path):
#     try:
#         pdf_document = fitz.open(input_path)
#         pdf_document.save(output_path, deflate=True)
#     except Exception as e:
#         print("Error compressing PDF:", e)
#
# def split_pdf(input_path):
#     output_paths = []
#     try:
#         reader = PdfReader(input_path)
#         for i, page in enumerate(reader.pages):
#             writer = PdfWriter()
#             writer.add_page(page)
#             output_path = f"{input_path}_part_{i + 1}.pdf"
#             with open(output_path, 'wb') as f:
#                 writer.write(f)
#             output_paths.append(os.path.basename(output_path))
#         return output_paths
#     except Exception as e:
#         print("Error splitting PDF:", e)
#         return []
#
# def merge_pdfs(input_paths, output_path):
#     try:
#         writer = PdfWriter()
#         for path in input_paths:
#             reader = PdfReader(path)
#             for page in reader.pages:
#                 writer.add_page(page)
#         with open(output_path, 'wb') as f:
#             writer.write(f)
#     except Exception as e:
#         print("Error merging PDFs:", e)
#
# def encrypt_pdf(input_path, output_path, password):
#     try:
#         reader = PdfReader(input_path)
#         writer = PdfWriter()
#
#         for page in reader.pages:
#             writer.add_page(page)
#
#         writer.encrypt(password)
#         with open(output_path, 'wb') as f:
#             writer.write(f)
#     except Exception as e:
#         print("Error encrypting PDF:", e)
#
# # ==================== New Features ====================
#
# # PDF to Image Conversion
# def pdf_to_image(pdf_path):
#     try:
#         images = convert_from_path(pdf_path)
#         output_paths = []
#         for i, img in enumerate(images):
#             output_path = f"{pdf_path}_page_{i + 1}.png"
#             img.save(output_path, 'PNG')
#             output_paths.append(output_path)
#         return output_paths
#     except Exception as e:
#         print("Error converting PDF to images:", e)
#         return []
#
# # Image to PDF Conversion
# def images_to_pdf(image_files, output_path):
#     try:
#         images = [Image.open(image) for image in image_files]
#         images[0].save(output_path, save_all=True, append_images=images[1:])
#     except Exception as e:
#         print("Error converting images to PDF:", e)
#
# # Text Summarization
# def summarize_text(file_path):
#     try:
#         with open(file_path, 'r') as file:
#             content = file.read()
#         # Simple summarization logic (You can improve this further)
#         summary = " ".join(content.split()[:100]) + "..."
#         return summary
#     except Exception as e:
#         print("Error summarizing text:", e)
#         return "Error in summarizing the text."
#
# # Video to Audio Extraction
# def video_to_audio(video_path, audio_path):
#     try:
#         video_clip = VideoFileClip(video_path)
#         audio_clip = video_clip.audio
#         audio_clip.write_audiofile(audio_path)
#     except Exception as e:
#         print("Error extracting audio from video:", e)
#
# # Audio Translation
# def audio_translation(audio_path):
#     try:
#         recognizer = sr.Recognizer()
#         with sr.AudioFile(audio_path) as source:
#             audio = recognizer.record(source)
#         text = recognizer.recognize_google(audio)
#         return text
#     except Exception as e:
#         print("Error translating audio:", e)
#         return "Error in audio translation."

import os
import subprocess
from pdf2docx import Converter
from docx import Document
import pytesseract
from pdf2image import convert_from_path
import speech_recognition as sr
from pydub import AudioSegment
import whisper
import fitz  # PyMuPDF
from PyPDF2 import PdfReader, PdfWriter
from PIL import Image

model = whisper.load_model("base")

# ==================== Conversion Functions ====================

def convert_docx_to_pdf(docx_path, pdf_path):
    subprocess.run(["libreoffice", "--headless", "--convert-to", "pdf", docx_path, "--outdir", os.path.dirname(pdf_path)])

def convert_pdf_to_docx(pdf_path, docx_path):
    subprocess.run(["libreoffice", "--headless", "--convert-to", "docx", pdf_path, "--outdir", os.path.dirname(docx_path)])

def pdf_to_image(pdf_path):
    images = convert_from_path(pdf_path)
    output_paths = []
    for i, img in enumerate(images):
        output_path = f"{pdf_path}_page_{i + 1}.jpg"
        img.save(output_path, "JPEG")
        output_paths.append(os.path.basename(output_path))
    return output_paths

def images_to_pdf(image_files, output_path):
    image_list = [Image.open(file) for file in image_files]
    image_list[0].save(output_path, save_all=True, append_images=image_list[1:])

# ==================== Text Extraction Functions ====================

def extract_text_from_pdf(pdf_path):
    text = ""
    pdf_document = fitz.open(pdf_path)
    for page in pdf_document:
        text += page.get_text()
    return text

def extract_text_from_image(image_path):
    return pytesseract.image_to_string(Image.open(image_path))

def extract_text_from_audio(audio_path):
    try:
        result = model.transcribe(audio_path)
        return result["text"]
    except Exception as e:
        print("Error extracting text from audio:", e)
        return ""

# ==================== Text Summarization ====================

def summarize_text(text_file_path):
    with open(text_file_path, 'r') as file:
        text = file.read()
    summarized_text = text[:500] + "..." if len(text) > 500 else text  # Basic summarization logic
    return summarized_text

# ==================== PDF Manipulation Functions ====================

def compress_pdf(input_path, output_path):
    pdf_document = fitz.open(input_path)
    pdf_document.save(output_path, deflate=True)

def split_pdf(input_path):
    output_paths = []
    reader = PdfReader(input_path)
    for i, page in enumerate(reader.pages):
        writer = PdfWriter()
        writer.add_page(page)
        output_path = f"{input_path}_part_{i + 1}.pdf"
        with open(output_path, 'wb') as f:
            writer.write(f)
        output_paths.append(os.path.basename(output_path))
    return output_paths

def merge_pdfs(input_paths, output_path):
    writer = PdfWriter()
    for path in input_paths:
        reader = PdfReader(path)
        for page in reader.pages:
            writer.add_page(page)
    with open(output_path, 'wb') as f:
        writer.write(f)

def encrypt_pdf(input_path, output_path, password):
    reader = PdfReader(input_path)
    writer = PdfWriter()

    for page in reader.pages:
        writer.add_page(page)

    writer.encrypt(password)
    with open(output_path, 'wb') as f:
        writer.write(f)

# ==================== Audio & Video Functions ====================

def video_to_audio(video_path, audio_path):
    audio = AudioSegment.from_file(video_path)
    audio.export(audio_path, format="wav")

def audio_translation(audio_path):
    try:
        result = model.transcribe(audio_path)
        return result["text"]
    except Exception as e:
        print("Error translating audio:", e)
        return ""
