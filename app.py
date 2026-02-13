import streamlit as st
from prompt_variants import zero_shot, few_shot, chain_of_thought, role_based
from llm import generate_response
from Helpers import count_tokens

# --------------------------------------------------
# Page Config
# --------------------------------------------------

st.set_page_config(
    page_title="PromptForge",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 PromptForge – Smart Prompt Playground")
st.markdown("Experiment with different prompting strategies and compare outputs.")

# --------------------------------------------------
# User Inputs
# --------------------------------------------------

task = st.text_area(
    "Enter your task",
    placeholder="Example: Explain quantum computing to a 10-year-old",
    height=120
)

col1, col2 = st.columns(2)

with col1:
    temperature = st.slider("Temperature", 0.0, 2.0, 0.7, 0.1)

with col2:
    deterministic = st.checkbox("Deterministic Mode (Temperature = 0)")

if deterministic:
    temperature = 0.0

# --------------------------------------------------
# Run Button
# --------------------------------------------------

if st.button("🚀 Run Experiment"):

    if not task.strip():
        st.warning("Please enter a task before running the experiment.")
        st.stop()

    prompts = {
        "Zero-shot": zero_shot(task),
        "Few-shot": few_shot(task),
        "Chain-of-thought": chain_of_thought(task),
        "Role-based": role_based(task),
    }

    st.divider()

    # Display results in 2-column layout
    cols = st.columns(2)

    for idx, (name, prompt) in enumerate(prompts.items()):
        col = cols[idx % 2]

        with col:
            st.subheader(name)

            with st.expander("📜 View Prompt"):
                st.code(prompt)

            # Local token count
            prompt_tokens = count_tokens(prompt)
            st.caption(f"🧮 Prompt Tokens (local estimate): {prompt_tokens}")

            with st.spinner("Generating response..."):
                result = generate_response(prompt, temperature)

            if result["success"]:
                st.markdown("### 🧠 Output")
                st.write(result["content"])

                if result["usage"]:
                    usage = result["usage"]
                    st.caption(
                        f"🔢 API Usage → Prompt: {usage.get('prompt_tokens', '-')}, "
                        f"Completion: {usage.get('completion_tokens', '-')}, "
                        f"Total: {usage.get('total_tokens', '-')}"
                    )
            else:
                st.error(result["error"])

    st.divider()
    st.success("Experiment completed!")
