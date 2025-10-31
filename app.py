import streamlit as st
import nltk
import svgling
from parser_logic import load_grammar, parse_expression

st.set_page_config(page_title="CFG Arithmetic Parser", page_icon="🧩", layout="centered")

st.title("🧩 CFG-Based Arithmetic Expression Validator 🔍🧠")
st.markdown(
    "Enter an arithmetic expression (e.g., `a + b * c` or `(a+b)*c`) "
    "to check if it follows the grammar and view its parse tree."
)

expr = st.text_input("Enter Expression:", "(a+b)*c")

# --- Simplifier helper function ---
def simplify_tree(tree):
    """Remove grammar non-terminals (E, T, F) and keep only input tokens."""
    if isinstance(tree, str):
        return tree
    simplified_children = [simplify_tree(child) for child in tree if child]
    simplified_children = [c for c in simplified_children if c is not None]
    if len(simplified_children) == 1:
        return simplified_children[0]
    return tuple(simplified_children)


if st.button("Validate Expression"):
    grammar = load_grammar()
    is_valid, result = parse_expression(expr, grammar)

    if is_valid:
        st.success("✅ Expression is syntactically correct!")

        # ----------- 1️⃣ Textual Representation -----------
        st.markdown("### 🧾 Parse Tree (Full CFG Representation)")
        st.text(result.pformat())

        # ----------- 2️⃣ Simplified View -----------
        simplified = simplify_tree(result)
        st.markdown("### ✨ Simplified Parse (User View)")
        st.code(str(simplified))

        # ----------- 3️⃣ Visualization -----------
        st.markdown("### 🌳 Parse Tree Visualization")

        try:
            svg_obj = svgling.draw_tree(result)
            svg_str = svg_obj._repr_svg_()

            # Enhance contrast and appearance
            svg_with_style = f"""
            <style>
                svg text {{ fill: #ffffff !important; font-weight: 500; font-size: 14px; }}
                svg path, svg line {{ stroke: #00b4d8 !important; stroke-width: 1.5px; }}
            </style>
            <div style='background-color:#0e1117;
                        padding:20px;
                        border-radius:12px;
                        overflow-x:auto;
                        text-align:center;'>
                {svg_str}
            </div>
            """
            st.components.v1.html(svg_with_style, height=500)

        except Exception as e:
            st.error(f"Error displaying parse tree: {e}")

    else:
        st.error("❌ Invalid expression or grammar mismatch.")
        if result:
            st.warning(result)
        else:
            st.warning("Unknown parsing error — check your input expression.")
