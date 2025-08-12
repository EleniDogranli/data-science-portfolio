# 🏠 AI Rental Assistant

**AI Rental Assistant** is a lightweight AI-powered web application that generates professional rental listings based on property details.  
It uses **Python**, **Streamlit**, and **OpenAI GPT-3.5** to help landlords and real estate platforms automate the listing process.

---

## ✨ Features

- GPT-powered rental listing generation  
- User inputs: location, property type, size (sqm), and features  
- Provides rent estimate, listing title, and detailed description  
- Clean, interactive web interface built with Streamlit  
- Instant results in a few seconds  

---

## 📸 Screenshot

<img width="834" height="585" alt="create" src="https://github.com/user-attachments/assets/a30bb1f0-6c6e-483c-a41e-b39a51c16058" />
<img width="764" height="531" alt="done" src="https://github.com/user-attachments/assets/73dea98e-ed53-47b0-9d01-05361a30e4d2" />

---

## 🚀 How to Run the Project Locally

**1. Clone the repository**

git clone https://github.com/EleniDogranli/data-science-portfolio.git
cd "data-science-portfolio/Generate AI-powered rental listings with GPT & Streamlit"

---

**2. Install dependencies**

Install the required packages using:

pip install -r requirements.txt

---

**3. Add your OpenAI API key**

Open the rental_assistant.py file and replace:

openai.api_key = "your_api_key_here"

with your actual API key from https://platform.openai.com

---

**4. Run the app**

streamlit run rental_assistant.py


Then open your browser and visit: http://localhost:8501

---


💬 Example Output
Rent Estimate: €600–€800  
Title: Cozy Studio with Balcony in Koukaki, Athens  
Description: Welcome to this charming studio apartment located in the popular Koukaki neighborhood of Athens. This 48 sqm space features a lovely balcony, perfect for enjoying a morning coffee or evening glass of wine. Pets are allowed, making this apartment perfect for animal lovers. Don’t miss out on this cozy and convenient living space in the heart of Athens!

---

📁 Project Structure
Generate AI-powered rental listings with GPT & Streamlit/
├── rental_assistant.py     # Main app logic

├── .env                    # API key (not tracked by Git)

├── .gitignore              # Git exclusions

├── requirements.txt        # Dependencies

├── screenshot.png          # Screenshot (optional)

└── README.md               # Project documentation

---

💡 Future Improvements
Export listings to PDF / .txt

Add support for multiple languages (e.g. Greek, English)

Connect to rental platforms like Airbnb or Spitogatos

Enable a chatbot for tenant questions

Save listings locally or to a database

---

👩‍💻 Author
Eleni Dogranli
Data Scientist & AI Developer

LinkedIn https://www.linkedin.com/in/eleni-dogranli/

GitHub https://github.com/EleniDogranli/



