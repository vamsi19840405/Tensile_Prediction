import streamlit as st

# Function to calculate T
def calculate_T(X_1, X_2):
    T = 15.5832 * ((8.7087 * X_1) ** 0.2184) * ((2.0952 * X_2) ** 0.0590)
    return T

# Streamlit App UI
st.title("T Value Calculator")
#st.markdown("Calculate T using the formula:**T = 15.5832 × (8.7087×X₁)^0.2184 × (2.0952×X₂)^0.0590**")

# Number of input sets
n = st.number_input("Enter the number of input sets:", min_value=1, step=1)

# Initialize list to store results
results = []

# Create input fields for each set
for i in range(n):
    st.subheader(f"Input Set {i+1}")
    col1, col2 = st.columns(2)
    
    with col1:
        X_1 = st.number_input(f"Enter value of X₁ (Set {i+1})", key=f"x1_{i}", format="%.4f")
    with col2:
        X_2 = st.number_input(f"Enter value of X₂ (Set {i+1})", key=f"x2_{i}", format="%.4f")
    
    # Calculate T when both X_1 and X_2 are greater than 0
    if X_1 > 0 and X_2 > 0:
        T = calculate_T(X_1, X_2)
        results.append((i+1, X_1, X_2, T))
    else:
        results.append((i+1, X_1, X_2, "Invalid (X₁ and X₂ must be > 0)"))

# Display results
if results:
    st.subheader("Results")
    for res in results:
        set_no, x1, x2, T_val = res
        if isinstance(T_val, float):
            st.success(f"Set {set_no}: X₁ = {x1}, X₂ = {x2} → T = {T_val:.4f}")
        else:
            st.warning(f"Set {set_no}: X₁ = {x1}, X₂ = {x2} → {T_val}")
