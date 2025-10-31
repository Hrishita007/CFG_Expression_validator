
# 🌿 CFG-Based Arithmetic Expression Validator

---

### 🧠 **Project Overview**

A **Streamlit-powered web application** that validates and parses arithmetic expressions (like `(a+b)*c`) using a **Context-Free Grammar (CFG)**.
It verifies syntax correctness, visualizes parse trees, and provides detailed error feedback — built with **NLTK** and **Svgling**.

---

## 🚀 **Features**

* ✅ **Expression Validation:** Ensures input expressions follow CFG grammar rules.
* 🌳 **Parse Tree Visualization:** Displays both textual and graphical trees (SVG).
* ⚡ **Error Feedback:** Handles unbalanced parentheses, invalid tokens, and malformed syntax.
* 💻 **Interactive Web UI:** Clean and responsive interface using Streamlit.

---

## 🧩 **Grammar Definition**

Defined in `grammar.cfg`:

```plaintext
E -> E '+' T | E '-' T | T
T -> T '*' F | T '/' F | F
F -> '(' E ')' | 'id'
```

> `id` represents variables like `a`, `b`, `c`, etc.



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

The app is live and deployed on Streamlit Cloud! 🚀
You can explore it here:

 <p align="center">
  <a href="https://cfg-expression-validator.streamlit.app/" target="_blank">
    <img src="https://img.shields.io/badge/🚀%20Open%20App-Streamlit%20Cloud-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Open Streamlit App"/>
  </a>
</p>



Simply visit the link, enter any arithmetic expression like (a+b)*c, and visualize its parse tree instantly.

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

This project is created for educational and demonstration purposes.
Not released under any specific open-source license.

---

<div align="center">

### 💖 Made with Python 🐍 and Streamlit 🌿

</div>

