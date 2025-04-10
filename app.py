import streamlit as st

# Function to calculate T
def calculate_T(X_1, X_2):
    T = 15.5832 * ((8.7087 * X_1) ** 0.2184) * ((2.0952 * X_2) ** 0.0590)
    return T

# Page config
st.set_page_config(page_title="T Calculator", layout="centered")

# Title
st.title("T Value Calculator")
#st.markdown("**Formula:** T = 15.5832 × (8.7087×X₁)^0.2184 × (2.0952×X₂)^0.0590")

# Number of inputs
n = st.number_input("Enter the number of input sets:", min_value=1, step=1)

results = []

# Input Fields
for i in range(n):
    st.subheader(f"Input Set {i + 1}")
    col1, col2 = st.columns(2)

    with col1:
        x1_input = st.text_input(f"Enter X₁ (Set {i+1})", key=f"x1_{i}")
    with col2:
        x2_input = st.text_input(f"Enter X₂ (Set {i+1})", key=f"x2_{i}")

    if x1_input and x2_input:
        try:
            X_1 = float(x1_input)
            X_2 = float(x2_input)

            if X_1 > 0 and X_2 > 0:
                T = calculate_T(X_1, X_2)
                if round(T, 4) not in [0.0000, 1.0000]:
                    results.append((i + 1, X_1, X_2, T))
        except ValueError:
            st.warning(f"Set {i+1}: Please enter valid numeric values for X₁ and X₂.")

# Results
if results:
    st.subheader("Results")
    for set_no, x1, x2, T_val in results:
        st.success(f"Set {set_no}: X₁ = {x1}, X₂ = {x2} → T = {T_val:.4f}")
else:
    st.info("Enter values above to calculate T.")
