import os
import json
import time
from flask import Flask, request, jsonify
from flask_cors import CORS
from google import genai
from PIL import Image

app = Flask(__name__)
CORS(app)

# --- CONFIGURATION ---
# Replace with your actual key
client = genai.Client(api_key="API_KEY_PLACEHOLDER") 
# We use 1.5-flash as it is stable and faster for this specific task
MODEL_ID = "gemini-2.5-flash"

@app.route('/api/evaluate', methods=['POST'])
def evaluate_interview():
    try:
        print("\n--- New Dual-Analysis Request ---")
        
        # 1. Get Data
        user_response = request.form.get('text_input', '')
        question_context = request.form.get('context_text', 'General Interview Question')
        
        camera_image = None
        if 'camera_frame' in request.files:
            camera_image = Image.open(request.files['camera_frame'])
            print("Snapshot received.")

        # 2. Dual-Analysis Prompt
        prompt = f"""
        You are an expert Interview Coach.
        
        INPUTS:
        1. CONTEXT: User is answering "{question_context}"
        2. AUDIO(Text): "{user_response}"
        3. VISUAL(Image): A snapshot of the user speaking.

        TASK:
        Perform two STRICTLY INDEPENDENT analyses. 
        - Do not let the text quality influence the visual score.
        - Do not let the facial expression influence the text score.

        Analysis A: VERBAL (Text Only)
        - Did they answer the specific question asked?
        - Was the answer structured (STAR method), relevant, and clear?
        
        Analysis B: NON-VERBAL (Visual Only)
        - Analyze facial micro-expressions.
        - Look for: Eye contact (looking at camera), genuine smiling, confidence.
        - Penalize: Frowning, looking away, boredom, or extreme stress.
        - If image is missing/black, return 0.

        OUTPUT:
        Return ONLY a JSON object with this exact structure:
        {{
            "verbal_score": <number 0-100>,
            "verbal_feedback": "<Critique of the words only>",
            "visual_score": <number 0-100>,
            "visual_feedback": "<Critique of the facial expression only>",
            "coaching_tip": "<One synthesis tip to combine both>"
        }}
        """

        # 3. Call Gemini
        content_payload = [prompt]
        if camera_image:
            content_payload.append(camera_image)

        # Simple Retry Logic for Rate Limits
        response = None
        for attempt in range(3):
            try:
                response = client.models.generate_content(
                    model=MODEL_ID,
                    contents=content_payload
                )
                break
            except Exception as e:
                if "429" in str(e):
                    time.sleep(2) # Wait 2s if busy
                else:
                    raise e
        
        if not response:
            return jsonify({"error": "Server busy"}), 429

        # 4. Return JSON
        clean_text = response.text.replace('```json', '').replace('```', '').strip()
        return jsonify(json.loads(clean_text))

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"verbal_score": 0, "verbal_feedback": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')