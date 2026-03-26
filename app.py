"""
Matrix Calculator Application
A secure matrix calculation tool with user authentication
"""

import streamlit as st
import json
from auth import (
    register_user, login_user, user_exists, 
    get_user_matrices, save_user_matrices,
    validate_password, validate_username
)
from matrix_ops import (
    validate_dimensions, validate_entry, create_matrix,
    determinant, transpose, inverse,
    add_matrices, subtract_matrices, multiply_matrices,
    scalar_multiply, update_matrix_entry
)

# Set page config
st.set_page_config(
    page_title="Secure Matrix Calculator",
    page_icon="🔢",
    layout="wide"
)

# Initialize session state
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.username = None
    st.session_state.matrices = []
    st.session_state.page = "login"


def display_login_page():
    """Display login/registration page."""
    st.title("🔢 Secure Matrix Calculator")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Login")
        login_username = st.text_input("Username", key="login_username")
        login_password = st.text_input("Password", type="password", key="login_password")
        
        if st.button("Login", key="login_btn"):
            if not login_username or not login_password:
                st.error("Please enter both username and password")
            else:
                success, message = login_user(login_username, login_password)
                if success:
                    st.session_state.logged_in = True
                    st.session_state.username = login_username
                    st.session_state.matrices = get_user_matrices(login_username)
                    st.session_state.page = "main"
                    st.success(message)
                    st.rerun()
                else:
                    st.error(message)
    
    with col2:
        st.subheader("Register New Account")
        register_username = st.text_input("Choose Username", key="register_username")
        register_password = st.text_input("Choose Password", type="password", key="register_password")
        register_password_confirm = st.text_input("Confirm Password", type="password", key="register_password_confirm")
        
        if st.button("Register", key="register_btn"):
            if not register_username or not register_password or not register_password_confirm:
                st.error("Please fill in all fields")
            elif register_password != register_password_confirm:
                st.error("Passwords do not match")
            else:
                success, message = register_user(register_username, register_password)
                if success:
                    st.success(message)
                    st.info("Please login with your new account")
                else:
                    st.error(message)
    
    # Display password requirements
    st.markdown("---")
    st.subheader("🔐 Password Requirements")
    st.markdown("""
    - **Length**: 8-50 characters
    - **Uppercase**: At least one uppercase letter
    - **Lowercase**: At least one lowercase letter
    - **Special Character**: At least one of: !@#$%^&*()-_=+[]{}|;:,.<>?/
    """)


def display_matrix_input(matrix_name: str, rows: int, cols: int, matrix_data: list) -> list:
    """Display matrix input grid."""
    st.subheader(f"Enter values for {matrix_name} ({rows}x{cols})")
    
    cols_display = st.columns(cols)
    updated_data = [row[:] for row in matrix_data]
    
    for r in range(rows):
        with st.container():
            cols_row = st.columns(cols)
            for c in range(cols):
                with cols_row[c]:
                    value = st.number_input(
                        f"[{r},{c}]",
                        value=float(matrix_data[r][c]),
                        step=0.01,
                        label_visibility="collapsed",
                        key=f"matrix_{matrix_name}_{r}_{c}"
                    )
                    updated_data[r][c] = float(value)
    
    return updated_data


def display_main_page():
    """Display main application page."""
    st.title("🔢 Secure Matrix Calculator")
    
    # Sidebar for user info and logout
    with st.sidebar:
        st.write(f"👤 Logged in as: **{st.session_state.username}**")
        if st.button("Logout"):
            st.session_state.logged_in = False
            st.session_state.username = None
            st.session_state.matrices = []
            st.session_state.page = "login"
            st.rerun()
        
        st.markdown("---")
        st.subheader("📊 Your Matrices")
        st.write(f"Stored: {len(st.session_state.matrices)}/10")
    
    # Main tabs
    tab1, tab2, tab3, tab4 = st.tabs(["Create Matrix", "View Matrices", "Operations", "Settings"])
    
    # Tab 1: Create Matrix
    with tab1:
        st.subheader("Create New Matrix")
        
        if len(st.session_state.matrices) >= 10:
            st.warning("⚠️ You have reached the maximum of 10 matrices. Delete one to create a new one.")
        else:
            col1, col2 = st.columns(2)
            
            with col1:
                rows_input = st.text_input("Number of Rows (1-15)", value="3")
            with col2:
                cols_input = st.text_input("Number of Columns (1-15)", value="3")
            
            # Validate dimensions
            if st.button("Create Matrix", key="create_matrix_btn"):
                is_valid, error_msg = validate_dimensions(rows_input, cols_input)
                
                if not is_valid:
                    st.error(f"❌ {error_msg}")
                else:
                    rows = int(rows_input)
                    cols = int(cols_input)
                    new_matrix = create_matrix(rows, cols)
                    st.session_state.matrices.append(new_matrix)
                    save_user_matrices(st.session_state.username, st.session_state.matrices)
                    st.success(f"✅ Matrix created: {new_matrix['name']}")
                    st.rerun()
    
    # Tab 2: View Matrices
    with tab2:
        st.subheader("View and Edit Matrices")
        
        if not st.session_state.matrices:
            st.info("No matrices created yet. Go to 'Create Matrix' to get started!")
        else:
            for idx, matrix in enumerate(st.session_state.matrices):
                with st.expander(f"📋 {matrix['name']} ({matrix['rows']}x{matrix['cols']})"):
                    col1, col2 = st.columns([4, 1])
                    
                    with col1:
                        # Display matrix input
                        updated_data = display_matrix_input(
                            matrix['name'],
                            matrix['rows'],
                            matrix['cols'],
                            matrix['data']
                        )
                        
                        # Display matrix
                        import pandas as pd
                        df = pd.DataFrame(updated_data, dtype=float)
                        st.write("**Current Matrix:**")
                        st.dataframe(df.round(4), use_container_width=True)
                    
                    with col2:
                        st.write("")
                        st.write("")
                        if st.button("📝 Update", key=f"update_{idx}"):
                            st.session_state.matrices[idx]['data'] = updated_data
                            save_user_matrices(st.session_state.username, st.session_state.matrices)
                            st.success("✅ Matrix updated!")
                            st.rerun()
                        
                        if st.button("🗑️ Delete", key=f"delete_{idx}"):
                            st.session_state.matrices.pop(idx)
                            save_user_matrices(st.session_state.username, st.session_state.matrices)
                            st.success("✅ Matrix deleted!")
                            st.rerun()
                        
                        # Rename
                        new_name = st.text_input("Rename", value=matrix['name'], key=f"rename_{idx}")
                        if st.button("✏️ Rename", key=f"rename_btn_{idx}"):
                            st.session_state.matrices[idx]['name'] = new_name
                            save_user_matrices(st.session_state.username, st.session_state.matrices)
                            st.success("✅ Matrix renamed!")
                            st.rerun()
    
    # Tab 3: Operations
    with tab3:
        st.subheader("Matrix Operations")
        
        if not st.session_state.matrices:
            st.info("No matrices available. Create matrices first!")
        else:
            operation = st.selectbox(
                "Select Operation",
                ["Determinant", "Transpose", "Inverse", "Add", "Subtract", "Multiply", "Scalar Multiply"]
            )
            
            # Single matrix operations
            if operation in ["Determinant", "Transpose", "Inverse"]:
                matrix_names = [m['name'] for m in st.session_state.matrices]
                selected_matrix_name = st.selectbox("Select Matrix", matrix_names)
                selected_matrix = next(m for m in st.session_state.matrices if m['name'] == selected_matrix_name)
                
                if st.button(f"Calculate {operation}", key="calc_single_op"):
                    if operation == "Determinant":
                        success, result = determinant(selected_matrix)
                        if success:
                            st.success(f"✅ Determinant: **{result:.6f}**")
                        else:
                            st.error(f"❌ {result}")
                    
                    elif operation == "Transpose":
                        success, result = transpose(selected_matrix)
                        if success:
                            import pandas as pd
                            df = pd.DataFrame(result['data'], dtype=float)
                            st.success(f"✅ Transposed Matrix ({result['rows']}x{result['cols']}):")
                            st.dataframe(df.round(4), use_container_width=True)
                            st.session_state.matrices.append(result)
                            save_user_matrices(st.session_state.username, st.session_state.matrices)
                            st.info(f"Matrix saved as: {result['name']}")
                        else:
                            st.error(f"❌ {result}")
                    
                    elif operation == "Inverse":
                        success, result = inverse(selected_matrix)
                        if success:
                            import pandas as pd
                            df = pd.DataFrame(result['data'], dtype=float)
                            st.success(f"✅ Inverse Matrix ({result['rows']}x{result['cols']}):")
                            st.dataframe(df.round(6), use_container_width=True)
                            st.session_state.matrices.append(result)
                            save_user_matrices(st.session_state.username, st.session_state.matrices)
                            st.info(f"Matrix saved as: {result['name']}")
                        else:
                            st.error(f"❌ {result}")
            
            # Two-matrix operations
            elif operation in ["Add", "Subtract", "Multiply"]:
                col1, col2 = st.columns(2)
                matrix_names = [m['name'] for m in st.session_state.matrices]
                
                with col1:
                    matrix1_name = st.selectbox("Select First Matrix", matrix_names, key="matrix1_select")
                with col2:
                    matrix2_name = st.selectbox("Select Second Matrix", matrix_names, key="matrix2_select")
                
                matrix1 = next(m for m in st.session_state.matrices if m['name'] == matrix1_name)
                matrix2 = next(m for m in st.session_state.matrices if m['name'] == matrix2_name)
                
                if st.button(f"Calculate {operation}", key="calc_double_op"):
                    if operation == "Add":
                        success, result = add_matrices(matrix1, matrix2)
                    elif operation == "Subtract":
                        success, result = subtract_matrices(matrix1, matrix2)
                    elif operation == "Multiply":
                        success, result = multiply_matrices(matrix1, matrix2)
                    
                    if success:
                        import pandas as pd
                        df = pd.DataFrame(result['data'], dtype=float)
                        st.success(f"✅ Result ({result['rows']}x{result['cols']}):")
                        st.dataframe(df.round(6), use_container_width=True)
                        st.session_state.matrices.append(result)
                        save_user_matrices(st.session_state.username, st.session_state.matrices)
                        st.info(f"Matrix saved as: {result['name']}")
                    else:
                        st.error(f"❌ {result}")
            
            # Scalar multiplication
            elif operation == "Scalar Multiply":
                matrix_names = [m['name'] for m in st.session_state.matrices]
                selected_matrix_name = st.selectbox("Select Matrix", matrix_names)
                scalar = st.number_input("Enter Scalar Value", value=2.0, step=0.1)
                
                selected_matrix = next(m for m in st.session_state.matrices if m['name'] == selected_matrix_name)
                
                if st.button("Calculate Scalar Multiply", key="calc_scalar_op"):
                    success, result = scalar_multiply(selected_matrix, scalar)
                    
                    if success:
                        import pandas as pd
                        df = pd.DataFrame(result['data'], dtype=float)
                        st.success(f"✅ Result ({result['rows']}x{result['cols']}):")
                        st.dataframe(df.round(6), use_container_width=True)
                        st.session_state.matrices.append(result)
                        save_user_matrices(st.session_state.username, st.session_state.matrices)
                        st.info(f"Matrix saved as: {result['name']}")
                    else:
                        st.error(f"❌ {result}")
    
    # Tab 4: Settings
    with tab4:
        st.subheader("Account Settings")
        
        st.write("**Change Password**")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            current_password = st.text_input("Current Password", type="password", key="current_pwd")
        with col2:
            new_password = st.text_input("New Password", type="password", key="new_pwd")
        with col3:
            confirm_password = st.text_input("Confirm New Password", type="password", key="confirm_pwd")
        
        if st.button("Change Password"):
            st.info("Password change feature coming soon!")
        
        st.markdown("---")
        st.subheader("ℹ️ Application Information")
        st.markdown("""
        **Secure Matrix Calculator**
        
        **Features:**
        - ✅ Secure user authentication with bcrypt hashing
        - ✅ Store up to 10 matrices
        - ✅ Matrix operations: Determinant, Transpose, Inverse
        - ✅ Matrix arithmetic: Add, Subtract, Multiply
        - ✅ Scalar multiplication
        - ✅ Input validation and error messages
        
        **Security:**
        - 🔐 Passwords hashed with bcrypt salt
        - 📏 Password requirements enforced
        - 🛡️ Input validation and limits
        - 💾 Secure data storage
        """)


# Main app logic
def main():
    if not st.session_state.logged_in:
        display_login_page()
    else:
        display_main_page()


if __name__ == "__main__":
    main()
