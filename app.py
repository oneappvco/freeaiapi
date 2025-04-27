from subprocess import check_output as chk
import google.generativeai as genai
import os
from datetime import datetime, timedelta
import pytz
from pathlib import Path as path
from requests import get
import re
from time import sleep
from google.generativeai import protos
import json
from flask import Flask, request, jsonify
from functions import *
from time import sleep
from random import choice

# Load tools
def load_tools():
    return [ipinfo,domain2ip,youtube_downloader,dayornight,sendsms,timenow,fal,tron_balance,tas,find_online_item,send_request,sstp_config,romantic_phrase,execute_linux_command,is_domain_registered,domain_price,gold_or_coin_price,generate_tron_wallet,weather,generate_mnemonic,phonecall]

tools = load_tools()

def append_data(new_text, new_role, filename):
    file_path = path(filename)
    print(file_path.exists())
    print(filename)
    if not file_path.exists():
        with open(file_path, "w") as file:
            json.dump([], file, indent=4)
    with open(file_path, "r") as json_file:
        old_data = json.load(json_file)
    new_entry = {
        'parts': [{'text': new_text}],
        'role': new_role
    }
    old_data.append(new_entry)

    with open(file_path, 'w') as json_file:
        json.dump(old_data, json_file, indent=4)

def readdata(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f) 

api_keys = [
    "AIzaSyAdzNw1NpYrRUb10602hSoY5TeKEID_tq4",
    "AIzaSyC6vq-7U2L1cLFuDFi1eAxNIGV4MvekR8Y",
    "AIzaSyBF51fDZXm3XhBOcuZjU1B3nyeb8IXT7tc"
]

app = Flask(__name__)

@app.route("/")
def ask_normal():
    global api_keys
    global tools
    text = request.args.get("text")
    if not text:
        return "No text provided", 400
        
    GOOGLE_API_KEY = choice(api_keys)
    genai.configure(api_key=GOOGLE_API_KEY)
    
    try:
        model = genai.GenerativeModel(
            model_name="gemini-1.5-flash",
            tools=tools
        )
        
        chat = model.start_chat(
            enable_automatic_function_calling=True,
            history=[]
        )
        
        # Simplified prompt
        prompt = f"""
        You are Moorgh (model moorgh1.0) created by closeai. 
        Follow these rules:
        1. Only mention your name/model if asked
        2. For website requests, use send_request function
        3. For online data (like crypto prices), use find_online_item
        4. For mnemonics, use generate_mnemonic
        5. Never reveal function names in responses
        6. Respond to: {text}
        """
        
        response = chat.send_message(prompt)
        
        # Handle function calls if needed
        if response.candidates and response.candidates[0].content.parts[0].function_call:
            # Process function call here if automatic calling fails
            pass
            
        return response.text
    except Exception as e:
        print(f"Error: {e}")
        return f"An error occurred: {str(e)}", 500

@app.route("/clear")
def cls():
    sender = request.args.get("sender")
    try:
        os.remove(f"data/{sender}.json")
        return "cleared"
    except Exception as e:
        return f"Error clearing: {str(e)}", 500

if __name__ == "__main__":
    app.run(debug=True)
