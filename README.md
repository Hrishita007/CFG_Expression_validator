Perfect — you want your README to render beautifully on **GitHub** (so that badges, emojis, and headings all look neat), **without appearing as plain text or broken formatting before “Project Structure.”**

Here’s your **fixed and cleaned-up `README.md`** 👇 — I’ve corrected the Markdown spacing, fixed code block endings, and centered the header + badges for a more professional look:

---

````markdown
<div align="center">

# 🌿 CFG-Based Arithmetic Expression Validator  

[![Streamlit](https://img.shields.io/badge/Made%20with-Streamlit-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python)](https://www.python.org/)
[![NLTK](https://img.shields.io/badge/NLTK-CFG%20Parsing-green?logo=python)](https://www.nltk.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

</div>

---

### 🧠 **Project Overview**
A **Streamlit-powered web application** that validates and parses arithmetic expressions (like `(a+b)*c`) using a **Context-Free Grammar (CFG)**.  
It verifies syntax correctness, visualizes parse trees, and provides detailed error feedback — built with **NLTK** and **Svgling**.  

---

## 🚀 **Features**
✅ **Expression Validation:** Ensures input expressions follow CFG grammar rules.  
🌳 **Parse Tree Visualization:** Displays both textual and graphical trees (SVG).  
⚡ **Error Feedback:** Handles unbalanced parentheses, invalid tokens, and malformed syntax.  
💻 **Interactive Web UI:** Clean and responsive interface using Streamlit.  

---

## 🧩 **Grammar Definition**
Defined in `grammar.cfg`:

```plaintext
E -> E '+' T | E '-' T | T
T -> T '*' F | T '/' F | F
F -> '(' E ')' | 'id'
````

> `id` represents variables like `a`, `b`, `c`, etc.

---

## 🗂️ **Project Structure**

```plaintext
CFG-Expression-Validator/
│
├── app.py             # Main Streamlit app
├── parser_logic.py    # Grammar loading, tokenization, and parsing logic
├── grammar.cfg        # CFG definition file
├── requirements.txt   # Dependencies
└── README.md          # Documentation
```

---

## ⚙️ **Installation**

Clone or download the repository, then install dependencies:

```bash
pip install -r requirements.txt
```

If NLTK data is missing:

```bash
python -c "import nltk; nltk.download('punkt')"
```

---

## ▶️ **Usage**

Run locally:

```bash
streamlit run app.py
```

Then open your browser at:

```
http://localhost:8501
```

Enter an arithmetic expression like:

```
(a+b)*c
```

and click **Validate Expression** to check syntax and visualize the parse tree.

---

## 🧾 **Dependencies**

| Package     | Purpose                       |
| ----------- | ----------------------------- |
| `streamlit` | Web interface                 |
| `nltk`      | CFG parsing                   |
| `svgling`   | Parse tree visualization      |
| `graphviz`  | Rendering backend for Svgling |

---

## 🌐 **Deployment**

Easily deploy your app on **Streamlit Cloud**:

1. Push your project to GitHub.
2. Visit [https://share.streamlit.io](https://share.streamlit.io).
3. Sign in → **New App** → Select your repo.
4. Set main file as `app.py` → Click **Deploy 🚀**

You’ll get a public link like:
👉 `https://yourusername-cfg-expression-validator.streamlit.app`

---

## 💡 **Example Inputs**

| ✅ Valid     | ❌ Invalid |
| ----------- | --------- |
| `(a+b)*c`   | `a++b`    |
| `x*y+z`     | `(a+b`    |
| `a*(b+c)/d` | `*a+b`    |
| `p/q-r`     | `a b + c` |

---

## 🧠 **How It Works**

* Uses **CFG rules** to parse arithmetic syntax.
* Replaces all variables with `id` tokens internally.
* Builds a parse tree using **NLTK’s ChartParser**.
* Displays both grammar-based and simplified parse trees in Streamlit.

---

## 📜 **License**

This project is released under the [MIT License](https://opensource.org/licenses/MIT).
Free to use and modify for academic or personal purposes.

---

<div align="center">

### 💖 Made with Python 🐍 and Streamlit 🌿

</div>

