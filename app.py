from flask import Flask, Response, request, jsonify
import asyncio
import edge_tts
import requests
from g4f.client import AsyncClient
app = Flask(__name__)

@app.route('/audiogen')
async def serve_audio():
    TEXT = request.args.get("text")
    if not TEXT:
        return jsonify({"error":"text parm is required"}),404
    VOICE = "fa-IR-FaridNeural" if request.args.get("sayas")=="man" else "fa-IR-DilaraNeural"
    OUTPUT_FILE = "test.mp3"
    communicate = edge_tts.Communicate(TEXT, VOICE)
    await communicate.save(OUTPUT_FILE)
    def generate_audio():
        with open(OUTPUT_FILE, 'rb') as audio_file:
            while chunk := audio_file.read(4096):
                yield chunk

    return Response(generate_audio(), mimetype='audio/mpeg')

@app.route('/imagegen')
async def serve_image():
    client = AsyncClient()
    text = request.args.get("prompt")
    if not text:
        return jsonify({"error":"prompt parm is required"}),404
    response = await client.images.generate(
        prompt=text,
        model="flux",
        response_format="url"
        # Add any other necessary parameters
    )
    
    image_url = requests.get(response.data[0].url)
    with open("img.png","wb") as f:
        f.write(image_url.content)
        f.close()
    
    image_file_path = 'img.png'  # Change this to your image file path

    def generate_image():
        with open(image_file_path, 'rb') as image_file:
            while chunk := image_file.read(4096):
                yield chunk

    return Response(generate_image(), mimetype='image/png')
@app.route("/chatgpt")
async def chat_with_gpt():
    text = request.args.get("text")
    if not text:
        return jsonify({"error":"text parm is required"}),404
    client = AsyncClient()
    search = True if request.args.get("websearch")=="on" else False
    response = await client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": text
            }
        ],
        web_search = search
    )
    
    return (response.choices[0].message.content)

