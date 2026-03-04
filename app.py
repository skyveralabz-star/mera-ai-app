<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SmartKabadi AI</title>
    <style>
        /* Modern Dark Theme aur Basic Reset */
        body { 
            font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; 
            color: #ececec; 
            margin: 0; 
            display: flex; 
            flex-direction: column; 
            height: 100vh; 
            overflow: hidden;
        }

        /* --- Background Slideshow Container --- */
        #bg-slideshow {
            position: fixed;
            top: 0;
            left: 0;
            width: 100vw;
            height: 100vh;
            z-index: -2;
            background-color: #000;
        }

        .slide {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-size: cover;
            background-position: center;
            opacity: 0;
            animation: slideFadeZoom 36s infinite;
        }

        /* 6 slides x 6 seconds each = 36s duration */
        .slide:nth-child(1) { animation-delay: 0s; }
        .slide:nth-child(2) { animation-delay: 6s; }
        .slide:nth-child(3) { animation-delay: 12s; }
        .slide:nth-child(4) { animation-delay: 18s; }
        .slide:nth-child(5) { animation-delay: 24s; }
        .slide:nth-child(6) { animation-delay: 30s; }

        @keyframes slideFadeZoom {
            0% { opacity: 0; transform: scale(1); }
            4% { opacity: 1; transform: scale(1.02); }
            14.66% { opacity: 1; transform: scale(1.05); }
            18.66% { opacity: 0; transform: scale(1.07); }
            100% { opacity: 0; transform: scale(1); }
        }

        /* Dark Overlay ko halka kar diya taaki photos clear dikhein */
        #bg-overlay {
            position: fixed;
            top: 0;
            left: 0;
            width: 100vw;
            height: 100vh;
            z-index: -1;
            background: rgba(0, 0, 0, 0.45);
        }

        /* Clean Message Text Styling */
        .clean-msg {
            position: absolute;
            top: 40%;
            width: 100%;
            text-align: center;
            font-size: 36px;
            font-weight: 800;
            color: #fff;
            text-shadow: 0px 0px 20px rgba(74, 222, 128, 0.9), 3px 3px 15px #000;
            opacity: 0.95;
        }

        #header {
            text-align: center;
            padding: 12px 18px;
            background-color: rgba(15, 15, 15, 0.85);
            backdrop-filter: blur(8px);
            font-size: 24px;
            font-weight: 700;
            border-bottom: 1px solid rgba(255, 255, 255, 0.2);
            box-shadow: 0 4px 6px rgba(0,0,0,0.4);
            z-index: 10;
        }

        .tagline {
            font-size: 14px;
            font-weight: 400;
            color: #10a37f;
            display: block;
            margin-top: 4px;
            text-shadow: none;
        }

        #chat-container { 
            flex: 1; 
            overflow-y: auto; 
            padding: 20px; 
            display: flex; 
            flex-direction: column; 
            gap: 20px; 
            max-width: 800px;
            margin: 0 auto;
            width: 100%;
            scroll-behavior: smooth;
        }

        /* Message Box Styling aur Fade-in Animation */
        .message { 
            max-width: 80%; 
            padding: 15px 20px; 
            border-radius: 18px; 
            line-height: 1.6; 
            font-size: 16px;
            animation: fadeInSlideUp 0.4s ease-out forwards;
            opacity: 0;
            box-shadow: 0 4px 10px rgba(0,0,0,0.3);
            text-shadow: 1px 1px 3px rgba(0,0,0,0.8);
        }

        @keyframes fadeInSlideUp {
            from { opacity: 0; transform: translateY(15px); }
            to { opacity: 1; transform: translateY(0); }
        }

        /* User aur Bot ke messages ke alag colors */
        .user-msg { 
            background-color: rgba(43, 43, 43, 0.85); 
            backdrop-filter: blur(5px);
            align-self: flex-end; 
            border-bottom-right-radius: 4px; 
            border: 1px solid rgba(255,255,255,0.1);
        }

        .bot-msg { 
            background-color: rgba(30, 30, 30, 0.85); 
            backdrop-filter: blur(8px);
            border: 1px solid rgba(255,255,255,0.1);
            align-self: flex-start; 
        }

        .generated-img {
            max-width: 100%;
            border-radius: 12px;
            margin-top: 15px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.5);
            border: 2px solid #10a37f;
        }

        ol { margin-top: 5px; margin-bottom: 5px; padding-left: 20px; }
        li { margin-bottom: 8px; }

        /* Niche ka Input Area */
        #input-area { 
            display: flex; 
            padding: 20px; 
            background-color: rgba(20, 20, 20, 0.85); 
            backdrop-filter: blur(10px);
            border-top: 1px solid rgba(255, 255, 255, 0.1);
            gap: 12px; 
            max-width: 800px;
            margin: 0 auto;
            width: 100%;
            box-sizing: border-box;
            align-items: center;
        }

        input[type="text"] { 
            flex: 1; 
            padding: 16px 20px; 
            border-radius: 30px; 
            border: 1px solid #555; 
            background-color: rgba(40, 40, 40, 0.8); 
            color: white; 
            font-size: 16px; 
            outline: none;
            transition: all 0.3s;
        }

        input[type="text"]:focus {
            border-color: #10a37f;
            background-color: rgba(50, 50, 50, 0.9);
            box-shadow: 0 0 10px rgba(16, 163, 127, 0.3);
        }

        /* Buttons Styling */
        .icon-btn {
            background-color: rgba(43, 43, 43, 0.8); 
            cursor: pointer; 
            display: flex; 
            align-items: center; 
            justify-content: center;
            width: 50px;
            height: 50px;
            border-radius: 50%;
            border: 1px solid #555;
            font-size: 20px;
            transition: 0.3s;
        }

        .icon-btn:hover { background-color: #4d4d4d; }

        .send-btn { 
            padding: 0 25px; 
            height: 50px;
            border: none; 
            border-radius: 25px; 
            background-color: #10a37f; 
            color: white; 
            font-size: 16px; 
            font-weight: bold;
            cursor: pointer; 
            transition: 0.3s;
            box-shadow: 0 4px 10px rgba(16, 163, 127, 0.3);
        }

        .send-btn:hover { background-color: #0b8c6d; transform: scale(1.05); }

        /* Mic Recording Animation (Pulse) */
        .recording {
            background-color: #ff4757 !important;
            border-color: #ff4757 !important;
            color: white;
            animation: pulse 1.5s infinite;
        }

        @keyframes pulse {
            0% { box-shadow: 0 0 0 0 rgba(255, 71, 87, 0.7); }
            70% { box-shadow: 0 0 0 15px rgba(255, 71, 87, 0); }
            100% { box-shadow: 0 0 0 0 rgba(255, 71, 87, 0); }
        }

        /* Typing Dots Animation */
        .typing-indicator {
            display: flex;
            gap: 5px;
            padding: 10px 0;
            align-items: center;
        }

        .dot {
            width: 8px;
            height: 8px;
            background-color: #10a37f;
            border-radius: 50%;
            animation: bounce 1.4s infinite ease-in-out both;
        }

        .dot:nth-child(1) { animation-delay: -0.32s; }
        .dot:nth-child(2) { animation-delay: -0.16s; }
        
        @keyframes bounce {
            0%, 80%, 100% { transform: scale(0); }
            40% { transform: scale(1); }
        }
    </style>
</head>
<body>

    <!-- Animated Background Slideshow -->
    <div id="bg-slideshow">
        <div class="slide" style="background-image: url('https://images.unsplash.com/photo-1595278069441-2cf29f8005a4?q=80&w=2000&auto=format&fit=crop');"></div>
        <div class="slide" style="background-image: url('https://images.unsplash.com/photo-1528323273322-d81458248d40?q=80&w=2000&auto=format&fit=crop');"></div>
        <div class="slide" style="background-image: url('https://images.unsplash.com/photo-1605600659873-d808a13e4d2a?q=80&w=2000&auto=format&fit=crop');"></div>
        
        <div class="slide" style="background-image: url('https://images.unsplash.com/photo-1532996122724-e3c354a0b15b?q=80&w=2000&auto=format&fit=crop');">
            <div class="clean-msg">♻️ Kachra nahi, Sansadhan hai. Recycle karein!</div>
        </div>
        <div class="slide" style="background-image: url('https://images.unsplash.com/photo-1542601906990-b4d3fb778b09?q=80&w=2000&auto=format&fit=crop');">
            <div class="clean-msg">🌍 Ek Kadam Swachhata Ki Ore</div>
        </div>
        <div class="slide" style="background-image: url('https://images.unsplash.com/photo-1518005020951-eccb494ad742?q=80&w=2000&auto=format&fit=crop');">
            <div class="clean-msg">🌱 Clean City, Green City!</div>
        </div>
    </div>
    <div id="bg-overlay"></div>

    <!-- Header Section -->
    <div id="header">
        ♻️ SmartKabadi AI
        <span class="tagline">"Kachre Se Kalakriti"</span>
    </div>

    <!-- Chat Area -->
    <div id="chat-container">
        <div class="message bot-msg">
            <strong>🤖 SmartKabadi AI:</strong><br><br>
            Hello! I am your AI Scrap Assistant. ♻️<br>
            Upload a photo of your waste material or use the mic. I will provide:<br><br>
            ✔ Scrap material type<br>
            ✔ All India current resale rate 💰<br>
            ✔ Step-by-step DIY "Kalakriti" ideas 🎨<br>
            ✔ <strong>NEW: AI-generated images of your final Kalakriti! 🖼️</strong>
        </div>
    </div>

    <!-- Input Area -->
    <div id="input-area">
        <label class="icon-btn" title="Photo Upload">
            📎 <input type="file" id="file-input" style="display:none;" accept="image/*" onchange="handleFileUpload()">
        </label>
        
        <button id="mic-btn" class="icon-btn" title="Voice Typing" onclick="toggleRecording()">🎙️</button>
        <input type="text" id="user-input" placeholder="Type here or use voice..." onkeypress="handleKeyPress(event)">
        <button class="send-btn" onclick="sendMessage()">Send</button>
    </div>

    <script>
        const chatContainer = document.getElementById("chat-container");
        const inputField = document.getElementById("user-input");
        const micBtn = document.getElementById("mic-btn");
        const fileInput = document.getElementById("file-input");

        // --- Voice Recognition Setup ---
        let recognition;
        let isRecording = false;

        if ('webkitSpeechRecognition' in window) {
            recognition = new webkitSpeechRecognition();
            recognition.continuous = false; 
            recognition.interimResults = false;
            recognition.lang = 'en-IN'; // Set to English (India) since bot replies in English

            recognition.onstart = function() {
                isRecording = true;
                micBtn.classList.add("recording");
                inputField.placeholder = "Listening...";
            };

            recognition.onresult = function(event) {
                const transcript = event.results[0][0].transcript;
                inputField.value = transcript;
            };

            recognition.onerror = function(event) {
                console.error("Speech error", event.error);
                stopRecording();
            };

            recognition.onend = function() {
                stopRecording();
            };
        } else {
            console.log("Speech Recognition not supported.");
        }

        function toggleRecording() {
            if (!recognition) {
                alert("Browser mic not supported. Please use Chrome.");
                return;
            }
            if (isRecording) {
                recognition.stop();
            } else {
                recognition.start();
            }
        }

        function stopRecording() {
            isRecording = false;
            micBtn.classList.remove("recording");
            inputField.placeholder = "Type here or use voice...";
        }

        // --- Text to Speech Setup ---
        function speakText(text) {
            if ('speechSynthesis' in window) {
                const plainText = text.replace(/<[^>]*>?/gm, ''); 
                const utterance = new SpeechSynthesisUtterance(plainText);
                utterance.lang = 'en-IN'; // English Accent
                utterance.rate = 1; 
                utterance.pitch = 1; 
                speechSynthesis.speak(utterance);
            }
        }

        // --- Asli AI API Setup (Google Gemini & Imagen) ---
        const apiKey = ""; // Canvas auto-injects key
        const textModelUrl = `https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-preview-09-2025:generateContent?key=${apiKey}`;
        const imageModelUrl = `https://generativelanguage.googleapis.com/v1beta/models/imagen-4.0-generate-001:predict?key=${apiKey}`;

        // Auto-retry helper
        async function fetchWithBackoff(url, options) {
            const delays = [1000, 2000, 4000, 8000, 16000];
            for (let i = 0; i <= delays.length; i++) {
                try {
                    const response = await fetch(url, options);
                    if (response.ok) return response;
                    if (i === delays.length) throw new Error("API failed");
                } catch (err) {
                    if (i === delays.length) throw err;
                }
                if (i < delays.length) {
                    await new Promise(res => setTimeout(res, delays[i]));
                }
            }
        }

        function fileToBase64(file) {
            return new Promise((resolve, reject) => {
                const reader = new FileReader();
                reader.readAsDataURL(file);
                reader.onload = () => resolve(reader.result.split(',')[1]);
                reader.onerror = error => reject(error);
            });
        }

        function handleKeyPress(event) {
            if (event.key === "Enter") sendMessage();
        }

        function handleFileUpload() {
            if (fileInput.files.length > 0) {
                inputField.value = "📷 Photo attached: " + fileInput.files[0].name;
            }
        }

        function appendMessage(htmlContent, className) {
            const msgDiv = document.createElement("div");
            msgDiv.className = `message ${className}`;
            msgDiv.innerHTML = htmlContent;
            chatContainer.appendChild(msgDiv);
            chatContainer.scrollTop = chatContainer.scrollHeight;
            return msgDiv; // Return element to append generated image later if needed
        }

        function showTypingIndicator(customText = "Analyzing scrap...") {
            const id = "typing-" + Date.now();
            const typingHtml = `
                <strong>🤖 SmartKabadi AI:</strong><br>
                <em>${customText}</em>
                <div class="typing-indicator">
                    <div class="dot"></div><div class="dot"></div><div class="dot"></div>
                </div>
            `;
            const msgDiv = document.createElement("div");
            msgDiv.id = id;
            msgDiv.className = `message bot-msg`;
            msgDiv.innerHTML = typingHtml;
            chatContainer.appendChild(msgDiv);
            chatContainer.scrollTop = chatContainer.scrollHeight;
            return id;
        }

        function removeMessage(id) {
            const element = document.getElementById(id);
            if (element) chatContainer.removeChild(element);
        }

        async function sendMessage() {
            const text = inputField.value.trim();
            const file = fileInput.files[0];

            if (text === "" && !file) return;

            appendMessage(text || `📷 Photo attached: ${file.name}`, "user-msg");
            inputField.value = "";
            fileInput.value = ""; 

            const typingId = showTypingIndicator("Scanning material & preparing English report...");

            try {
                const parts = [];
                
                // Prompt strictly asking for JSON output in English
                let promptText = `You are an expert AI Scrap Dealer and DIY Craft Artist in India. Analyze the uploaded photo/text. Provide details for the All India market in ENGLISH.
                Return ONLY a valid JSON object with the exact following structure (do not include markdown \`\`\`json block, just raw json):
                {
                    "is_scrap": boolean (true if the image/text is scrap or recyclable waste, false otherwise),
                    "message": "Friendly English message if it is not scrap. Empty string if it is scrap.",
                    "type": "Scrap material type (e.g., PET Plastic, Iron, Cardboard)",
                    "resale_value": "Approximate resale value in ₹ (All India Average)",
                    "diy_title": "Creative title for the DIY Kalakriti",
                    "diy_steps": "<ol><li>Step 1 description</li><li>Step 2 description</li></ol>",
                    "pro_tip": "A useful recycling tip",
                    "image_prompt": "A highly detailed, beautiful, photorealistic prompt for an AI image generator to create the FINAL finished DIY product (Kalakriti) made from this scrap. Describe the lighting, colors, and the background."
                }`;
                
                let userQuery = text.replace(/📷 Photo attached: .*/, '').trim();
                if (userQuery) promptText += `\n\nUser Message: ${userQuery}`;

                parts.push({ text: promptText });

                if (file) {
                    const base64Data = await fileToBase64(file);
                    parts.push({
                        inlineData: { mimeType: file.type, data: base64Data }
                    });
                }

                // Call Gemini Text Model
                const textResponse = await fetchWithBackoff(textModelUrl, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({
                        contents: [{ role: "user", parts: parts }],
                        generationConfig: { responseMimeType: "application/json" }
                    })
                });

                const data = await textResponse.json();
                let aiText = data.candidates?.[0]?.content?.parts?.[0]?.text;
                
                removeMessage(typingId); 

                if(!aiText) throw new Error("No response from AI");

                // Parse the AI's JSON response
                let aiData;
                try {
                    // Clean up potential markdown formatting from AI output
                    const cleanText = aiText.replace(/```json/gi, '').replace(/```/g, '').trim();
                    aiData = JSON.parse(cleanText);
                } catch (e) {
                    console.error("Failed to parse JSON", e, aiText);
                    appendMessage("<strong>🤖 SmartKabadi AI:</strong><br><br>Error formatting the response. Please try again.", "bot-msg");
                    return;
                }

                // Check if it's not scrap
                if (!aiData.is_scrap) {
                    appendMessage("<strong>🤖 SmartKabadi AI:</strong><br><br>" + aiData.message, "bot-msg");
                    speakText(aiData.message);
                    return;
                }

                // 1. Display the Text Report & Steps
                const htmlContent = `
                    👉 <strong>Type:</strong> ${aiData.type}<br>
                    💰 <strong>Resale Value (All India):</strong> ${aiData.resale_value}<br><br>
                    🎨 <strong>Kalakriti Idea: ${aiData.diy_title}</strong><br>
                    <strong>Step-by-step Process:</strong>
                    ${aiData.diy_steps}<br>
                    💡 <strong>Pro Tip:</strong> ${aiData.pro_tip}
                `;
                
                appendMessage("<strong>🤖 SmartKabadi AI:</strong><br><br>" + htmlContent, "bot-msg");
                speakText(`I have analyzed the scrap. It is ${aiData.type}. Here is a step-by-step guide to make ${aiData.diy_title}. I am now generating an image of the final product.`);

                // 2. Generate the AI Image (Kalakriti)
                const imgLoadingId = showTypingIndicator("🎨 Generating AI image of your Kalakriti...");

                try {
                    const imgResponse = await fetchWithBackoff(imageModelUrl, {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify({
                            instances: [{ prompt: aiData.image_prompt }],
                            parameters: { sampleCount: 1 }
                        })
                    });
                    
                    const imgData = await imgResponse.json();
                    removeMessage(imgLoadingId);

                    if (imgData.predictions && imgData.predictions[0]) {
                        const imageUrl = `data:image/png;base64,${imgData.predictions[0].bytesBase64Encoded}`;
                        const imgHtml = `Here is how your finished Kalakriti will look! ✨<br><img src="${imageUrl}" class="generated-img" alt="Generated Kalakriti">`;
                        appendMessage("<strong>🤖 SmartKabadi AI:</strong><br><br>" + imgHtml, "bot-msg");
                    } else {
                        appendMessage("<strong>🤖 SmartKabadi AI:</strong><br><em>Sorry, I couldn't generate the image right now, but you can follow the steps above!</em>", "bot-msg");
                    }

                } catch (imgError) {
                    removeMessage(imgLoadingId);
                    console.error("Image generation failed", imgError);
                    appendMessage("<strong>🤖 SmartKabadi AI:</strong><br><em>Sorry, AI image generation failed. Please follow the text instructions above.</em>", "bot-msg");
                }

            } catch (error) { 

int main ()
int a= (12,error) 
float  = (11, find)if = (00,fix)

               removeMessage(typingId);
                console.error("API Error: ", error);
                const errorMsg = "Sorry, network error or server is busy. Please try again later.";
                appendMessage("<strong>🤖 SmartKabadi AI:</strong><br><br>" + errorMsg, "bot-msg");
                speakText(errorMsg);
            }
        }
    </script>
</body>
</html>
