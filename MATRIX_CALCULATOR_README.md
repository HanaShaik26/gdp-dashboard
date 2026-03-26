# 🔢 Secure Matrix Calculator

A feature-rich matrix calculator application with user authentication and security features built with Streamlit.

## Features

### 🔐 Security
- **Password Hashing**: Uses bcrypt with salt for secure password storage
- **Strong Password Requirements**:
  - 8-50 characters length
  - At least one uppercase letter
  - At least one lowercase letter
  - At least one special character (!@#$%^&*()-_=+[]{}|;:,.<>?/)

### 📊 Matrix Management
- Store up to 10 matrices per user account
- Create matrices with custom dimensions (1-15 x 1-15)
- Edit and rename matrices
- Delete matrices
- Display matrices in formatted tables

### 🧮 Matrix Operations

#### Single Matrix Operations:
- **Determinant**: Calculate determinant of square matrices
- **Transpose**: Flip matrix along diagonal
- **Inverse**: Calculate matrix inverse (for invertible square matrices)

#### Two-Matrix Operations:
- **Addition**: Add matrices of same dimensions
- **Subtraction**: Subtract matrices of same dimensions
- **Multiplication**: Multiply matrices (when compatible dimensions)

#### Scalar Operations:
- **Scalar Multiplication**: Multiply matrix by a scalar value

### ✅ Input Validation
- Dimension validation (1-15 x 1-15)
- Entry length limit (50 characters max)
- Type checking (numeric values only)
- Clear error messages explaining why operations won't work

## Installation

1. **Clone or navigate to the project directory**:
   ```bash
   cd /workspaces/gdp-dashboard
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

1. **Start the Streamlit app**:
   ```bash
   streamlit run streamlit_app.py
   ```

2. **Access the application**:
   - Local URL: http://localhost:8501
   - The app will open in your default browser

## Usage Guide

### Registration
1. Enter a desired username (3-50 characters, alphanumeric + underscore)
2. Create a strong password meeting all requirements
3. Confirm your password
4. Click "Register"

### Login
1. Enter your username and password
2. Click "Login"

### Creating Matrices
1. Go to "Create Matrix" tab
2. Enter number of rows and columns (1-15 each)
3. Click "Create Matrix"
4. Edit the matrix values in the "View Matrices" tab

### Performing Operations
1. Go to "Operations" tab
2. Select the desired operation
3. Select the required matrices
4. Click the calculate button
5. Results are automatically saved as new matrices

### Matrix Naming
- Automatically named as: `Matrix_R{rows}C{cols}`
- Operation results named as: `{Operation}_{Matrix1}_{Matrix2}`
- Manually rename matrices in "View Matrices" tab

## Project Structure

```
gdp-dashboard/
├── streamlit_app.py      # Main Streamlit application
├── auth.py              # User authentication module
├── matrix_ops.py        # Matrix operations module
├── requirements.txt     # Python dependencies
└── users_db.json        # User database (created on first registration)
```

## File Descriptions

### `streamlit_app.py`
Main application file containing:
- Login/Registration UI
- Matrix creation and management
- Matrix operations interface
- Account settings page

### `auth.py`
Authentication module featuring:
- User registration with validation
- Secure login
- Password hashing with bcrypt
- Username and password validation
- User database management

### `matrix_ops.py`
Matrix operations module with:
- Dimension validation
- Entry validation
- All matrix operations
- Comprehensive error handling
- Result formatting

## Security Considerations

### Password Security
- Passwords are hashed using bcrypt with 12 rounds of salting
- Password validation enforces strong requirements
- Plaintext passwords are never stored

### Data Protection
- User data stored locally in `users_db.json`
- Matrix data associated with user accounts
- Input validation prevents overflow and injection attacks

### Error Handling
- Clear error messages for invalid operations
- Dimension checking before operations
- Invertibility checking before inverse calculation
- Comprehensive validation of all inputs

## Limitations & Constraints

- **Maximum Matrices**: 10 per user
- **Matrix Dimensions**: 1-15 x 1-15
- **Entry Length**: 50 characters maximum
- **Numeric Only**: Matrix entries must be valid numbers

## Error Messages

The application provides clear feedback:

- **"Dimensions must be integers"**: Row/Col input must be whole numbers
- **"Dimensions cannot exceed 15x15"**: Matrix size limit exceeded
- **"Matrix is singular and cannot be inverted"**: Determinant is zero
- **"Inverse only works for square matrices"**: Non-square matrix inversion attempted
- **"Matrices must have same dimensions for addition"**: Incompatible dimensions
- **"For matrix multiplication, columns of first matrix must equal rows of second matrix"**: Incompatible dimensions for multiplication

## Technology Stack

- **Frontend**: Streamlit
- **Backend**: Python, NumPy
- **Authentication**: bcrypt
- **Data Storage**: JSON
- **Matrix Computations**: NumPy

## Future Enhancements

- [ ] Change password functionality
- [ ] Matrix import/export (CSV, JSON)
- [ ] Advanced operations (eigenvalues, eigenvectors)
- [ ] Matrix decomposition (LU, QR, SVD)
- [ ] Graphical matrix representation
- [ ] Operation history
- [ ] Matrix sharing between users

## Support

For issues or questions, please refer to the application's built-in help in the "Settings" tab or review the password requirements section during registration.

---

**Created for secure matrix calculations with user authentication**
