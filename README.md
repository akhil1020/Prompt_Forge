# 🚀 PromptForge

PromptForge is a lightweight Python-based application designed to experiment with structured prompt engineering and modular LLM workflows.  
It allows users to test, compare, and refine prompt variations in a clean and reusable architecture.

---

## 📌 Objective

The goal of this project is to:

- Build a modular prompt experimentation framework
- Separate logic (LLM interaction) from prompt templates
- Make prompt testing structured and reusable
- Practice clean project structuring in Python
- Enable rapid iteration of prompt variants

---

## 🎯 Key Learnings

Through this project, you will understand:

- How to structure Python projects professionally
- How to modularize LLM logic
- How to separate prompt templates from execution logic
- How to use virtual environments
- How to manage dependencies properly
- How to prepare a project for GitHub deployment

---

## 🛠 Tech Stack

- Python 3.11+
- Virtual Environment (venv)
- LLM Integration (via API or local model)
- Modular Python Architecture

---

## 📂 Project Structure

```
PromptForge/
│
├── app.py                # Main entry point
├── llm.py                # LLM interaction logic
├── Helpers.py            # Utility/helper functions
├── prompt_variants.py    # Different prompt templates
├── requirements.txt      # Project dependencies
└── README.md
```

---

## ⚙️ Installation Guide (Step-by-Step)

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/akhil1020/Prompt_Forge.git
cd Prompt_Forge
```

---

### 2️⃣ Create Virtual Environment

Windows:

```bash
python -m venv env
env\Scripts\activate
```

Mac/Linux:

```bash
python3 -m venv env
source env/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

If you don't have a `requirements.txt`, create one:

```bash
pip freeze > requirements.txt
```

---

### 4️⃣ Set Environment Variables (If Required)


### ✅ Option 1: Using Streamlit Secrets (Recommended for Streamlit Apps)

If you're building a Streamlit app:

1️⃣ Create a folder named `.streamlit` in your project root.

2️⃣ Inside it, create a file called `secrets.toml`:

```
OPENAI_API_KEY = "your_api_key_here"
```

3️⃣ Access it in your Streamlit app:

```python
import streamlit as st

api_key = st.secrets["OPENAI_API_KEY"]
```

---

### ✅ Option 2: Using Streamlit Cloud (Deployment)

If deploying on Streamlit Cloud:

1. Go to your app dashboard  
2. Click on **Settings → Secrets**  
3. Add:

```
OPENAI_API_KEY = "your_api_key_here"
```

Then access it the same way:

```python
import streamlit as st

api_key = st.secrets["OPENAI_API_KEY"]
```

---

🔒 **Important:**  
Never commit API keys directly into your code or push them to GitHub.
Always use environment variables, `.env` files (ignored in `.gitignore`), or Streamlit secrets

## ▶️ Running the Application

```bash
streamlit run app.py
```

If everything is set up correctly, the application will start in your terminal.

---

## 🧪 Example Test Case

After running:

```
Enter your prompt:
```

Example input:

```
Explain the concept of edge computing in simple terms.
```

Expected Output:

- The system will process the prompt
- Apply a selected prompt template
- Send it to the LLM
- Return a structured response in the terminal

---

## 🔍 How It Works

1. `app.py` receives user input  
2. It calls a selected prompt from `prompt_variants.py`  
3. The formatted prompt is passed to `llm.py`  
4. The response is returned and displayed  
5. Helper utilities assist in formatting/logging  

---

## 🚀 Future Improvements

- Add web interface (Streamlit / FastAPI)
- Add prompt comparison mode
- Add logging dashboard
- Add prompt scoring system
- Add local LLM support (Ollama / LM Studio)

---



## 🤝 Contributing

Pull requests are welcome.  
For major changes, please open an issue first to discuss improvements.

---

## 📜 License

This project is open-source and available under the MIT License.

---

## 👨‍💻 Author

Developed as part of structured LLM experimentation and prompt engineering practice.

if you want to see this live. [Check Out Here](https://promptforge1.streamlit.app/)

---

⭐ If you found this helpful, consider giving the repo a star!
