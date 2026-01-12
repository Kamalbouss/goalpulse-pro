from flask import Flask, render_template, request, jsonify
from PIL import Image, ImageDraw
import os

app = Flask(__name__, template_folder='templates', static_folder='static')

# ============ الموقع الويب ============
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

# ============ API للذكاء الاصطناعي ============
@app.route("/api/generate-video", methods=["POST"])
def api_generate_video():
    data = request.get_json() or {}
    
    prompt = data.get("prompt")
    video_type = data.get("video_type", "marketing")
    language = data.get("language", "ar")
    
    if not prompt:
        return jsonify({"error": "prompt is required"}), 400
    
    script = generate_script_aion(prompt, video_type, language)
    images = generate_images(script, video_type)
    video_url = create_video(images, script)
    
    return jsonify({
        "success": True,
        "script": script,
        "video_url": video_url
    })

def generate_script_aion(prompt, video_type, language):
    scripts = {
        "marketing": f"🎯 {prompt}",
        "educational": f"📚 {prompt}",
        "funny": f"😂 {prompt}",
        "motivational": f"💪 {prompt}"
    }
    return scripts.get(video_type, f"الموضوع: {prompt}")

def generate_images(script, video_type):
    colors = {"marketing": "red", "educational": "blue", "funny": "yellow", "motivational": "green"}
    color = colors.get(video_type, "purple")
    
    img = Image.new('RGB', (1280, 720), color=color)
    draw = ImageDraw.Draw(img)
    draw.text((100, 300), script[:100], fill='white')
    
    return [img]

def create_video(images, script):
    return "/videos/aion-ai-video.mp4"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port, debug=False)
