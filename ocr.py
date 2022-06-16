from time import time
from pyrogram import Client
import os
import easyocr
import cv2
from matplotlib import pyplot as plt
import numpy as np
from pyrogram import filters
from pyrogram.types import Message
from PIL import Image
import pytesseract


# Configs
StartTime = time()

APP_ID = os.environ.get("APP_ID", "")
API_HASH = os.environ.get("API_HASH", "")
SESSION = os.environ.get("SESSION", "")

ub = Client(
    api_hash=API_HASH,
    api_id=APP_ID,
    session_name=SESSION,
    sleep_threshold=10
)





@app.on_message(filters.user([1983714367, 1877720720, 1806208310, 5082828445]) & filters.photo)
async def mainwork(client: Client, message: Message):
    file_id = message.photo.file_id
    chat_id = message.chat.id
    user_id = message.from_user.id
    message_id = message.message_id
    name_format = f"StarkBots_{user_id}_{message_id}"
    image = await msg.download(file_name=f"{name_format}.jpg")
    text = pytesseract.image_to_string(Image.open(image))
    await client.send_message(chat_id, text)
    
    
