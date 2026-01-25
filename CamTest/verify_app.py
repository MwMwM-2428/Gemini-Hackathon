import os
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
# Enable CORS so your browser (Frontend) can talk to this WSL Server
CORS(app)

SAVE_PATH = "test_capture.jpg"

@app.route('/verify', methods=['POST'])
def verify_capture():
    try:
        print("\n--- Incoming Data ---")
        
        # 1. Check if image file exists in request
        if 'camera_frame' not in request.files:
            print("Error: No 'camera_frame' found in request.")
            return jsonify({"status": "fail", "message": "No image found"}), 400

        file = request.files['camera_frame']
        
        # 2. Save the file to disk locally
        file.save(SAVE_PATH)
        file_size = os.path.getsize(SAVE_PATH)
        
        print(f"Success! Image saved to: {os.path.abspath(SAVE_PATH)}")
        print(f"File Size: {file_size} bytes")

        return jsonify({
            "status": "success",
            "message": "WSL received the image successfully!",
            "saved_at": os.path.abspath(SAVE_PATH),
            "size_bytes": file_size
        })

    except Exception as e:
        print(f"Server Error: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    # host='0.0.0.0' allows access from Windows host if needed
    print(f"Server listening. Waiting for camera data...")
    app.run(debug=True, port=5000, host='0.0.0.0')