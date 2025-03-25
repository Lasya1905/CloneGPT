# **CloneGPT - A Simple AI Chatbot Using Streamlit & Gemini API**  

CloneGPT is an interactive chatbot built with **Streamlit** that integrates Google's **Gemini AI API** to generate responses in real-time. It provides a simple yet powerful way to interact with AI, maintaining a chat history for a seamless user experience.  

## **🚀 Features**  
✅ **Real-time AI responses** using Gemini API  
✅ **Chat history management** with Streamlit session state  
✅ **Minimal UI** with an interactive chat interface  
✅ **User-friendly input system** for smooth conversations  

## **📌 Installation & Setup**  
### 1️⃣ Clone this repository:  
```bash
git clone https://github.com/Lasya1905/CloneGPT.git  
cd CloneGPT
```  
### 2️⃣ Install dependencies:  
```bash
pip install streamlit requests  
```  
### 3️⃣ Run the chatbot:  
```bash
streamlit run chatbot.py  
```  

## **🛡️ Security Notice**  
🚨 **Do not expose your API key** in the script. Instead, store it securely in **Streamlit secrets** or environment variables:  
```python
import os  
API_KEY = os.getenv("GEMINI_API_KEY")  
```  

## **📜 License**  
This project is open-source and available under the **MIT License**.  
