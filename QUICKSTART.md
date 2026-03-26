# 🔢 Secure Matrix Calculator - Quick Start Guide

## TL;DR - 3 Steps to Get Started

### 1️⃣ Install Dependencies
```bash
cd /workspaces/gdp-dashboard
pip install -r requirements.txt
```

### 2️⃣ Start the App
```bash
streamlit run streamlit_app.py
```

### 3️⃣ Create an Account
- Register with a strong password (8+ chars, uppercase, lowercase, special char)
- Start creating matrices!

---

## First Time Setup

### Register Your Account

1. **Open the app** at `http://localhost:8501`
2. **Fill in Registration Form**:
   - **Username**: Choose something like `MyUser123` (3-50 characters, letters/numbers/underscore)
   - **Password**: Create strong password like `MyPass@2024` (must have):
     - ✅ 8-50 characters
     - ✅ At least one uppercase letter (A-Z)
     - ✅ At least one lowercase letter (a-z)
     - ✅ At least one special character (!@#$%^&*()-_=+[]{}|;:,.<>?/)
   - **Confirm Password**: Re-enter the same password
3. **Click Register** ✅

### Login
- Use your username and password
- Click Login ✅

---

## Create Your First Matrix

### Step-by-Step

1. **Go to "Create Matrix" Tab**
2. **Enter Dimensions**:
   - Rows: `3` (any number 1-15)
   - Cols: `3` (any number 1-15)
3. **Click "Create Matrix"** ✅
4. **Go to "View Matrices" Tab**
5. **Expand Your Matrix** and enter values
6. **Click "Update"** to save

---

## Perform Operations

### Example: Add Two Matrices

1. **Create two matrices** (same dimensions, e.g., 2x2)
2. **Go to "Operations" Tab**
3. **Select "Add"** from dropdown
4. **Pick both matrices**
5. **Click "Calculate Add"** ✅
6. **Result automatically saved!**

### Other Operations Available
- ➕ **Addition** (same dimensions)
- ➖ **Subtraction** (same dimensions)
- ✖️ **Multiplication** (compatible dimensions)
- 🔄 **Transpose** (any matrix)
- ➗ **Inverse** (square matrices only)
- 📊 **Determinant** (square matrices only)
- **Scalar Multiply** (any matrix by number)

---

## Important Rules

### Matrix Constraints
| Rule | Limit |
|------|-------|
| Max matrices per account | 10 |
| Matrix dimensions | 1-15 rows × 1-15 cols |
| Entry length | 50 characters |
| Number entries only | Yes |

### Password Rules
| Requirement | Example |
|-------------|---------|
| Length | 8-50 characters |
| Uppercase | At least one (A-Z) |
| Lowercase | At least one (a-z) |
| Special Char | At least one (!@#$%^&*) |

---

## Common Operations

### Matrix Addition
```
Matrix A       Matrix B       Result
[1, 2]    +    [3, 4]    =    [4, 6]
[3, 4]         [1, 2]         [4, 6]
```
✅ Works when dimensions match (both 2×2)

### Matrix Transpose
```
Original (2×3)        Transposed (3×2)
[1, 2, 3]             [1, 5]
[4, 5, 6]       →     [2, 6]
                      [3, 0]
```
✅ Always works, swaps rows and columns

### Matrix Multiplication
```
Matrix A (2×3)  ×  Matrix B (3×2)  =  Result (2×2)
[1, 2, 3]           [1, 4]
[4, 5, 6]     ×     [2, 5]       =  Valid!
                    [3, 6]
```
✅ Works when: A columns = B rows

### Scalar Multiplication
```
3 × [1, 2]  =  [3, 6]
    [3, 4]     [9, 12]
```
✅ Multiply every element by the scalar

---

## Troubleshooting

### ❌ "Password must contain at least one uppercase letter"
**Solution**: Add uppercase letters (A-Z) to password

### ❌ "Dimensions cannot exceed 15x15"
**Solution**: Use smaller dimensions (max 15×15)

### ❌ "Matrix is singular and cannot be inverted"
**Solution**: Singular matrices (det=0) can't be inverted. Try a different matrix.

### ❌ "Matrices must have same dimensions for addition"
**Solution**: Both matrices must be same size (e.g., both 3×3)

### ❌ "For matrix multiplication, columns of first matrix must equal rows of second matrix"
**Solution**: First matrix columns must equal second matrix rows (A: m×n, B: n×p)

---

## Tips & Tricks

### 💡 Keep Track of Matrices
- Matrices are named like `Matrix_R3C3` (3 rows, 3 cols)
- Rename them for easy identification
- Results auto-named like `Matrix_A_+_Matrix_B`

### 💡 Test Operations Safely
- Create test matrices first
- Original matrices are preserved after operations
- Result saved as new matrix automatically

### 💡 Use Scalar Multiplication
- Multiply by 0.5 to divide all elements by 2
- Multiply by -1 to negate all elements
- Great for scaling data

### 💡 Check Determinant First
- Before inverting a square matrix, check determinant
- If determinant = 0, matrix is singular and non-invertible

---

## Security Reminders

🔒 **Your Data is Safe**:
- Passwords stored as hashes (bcrypt), never readable
- Each user's matrices are private
- No sharing between accounts without manual export

🛡️ **Strong Passwords**:
- Use unique passwords for this app
- Combine uppercase, lowercase, and special characters
- 8 characters minimum, 50 maximum

---

## Next Steps

### After You're Comfortable:
1. ✅ Create multiple matrices (up to 10)
2. ✅ Practice different operations
3. ✅ Try complex chains (Add → Transpose → Multiply)
4. ✅ Test edge cases (singular matrices, identity matrices)
5. ✅ Explore error messages to understand limitations

### Advanced Usage:
- Use determinant to check invertibility before inverse
- Chain operations to create complex calculations
- Use scalar multiplication for data scaling
- Practice matrix algebra concepts

---

## Example Workflow

### Mini-Project: Matrix Algebra Exercise

1. **Create Identity Matrix (3×3)**
   ```
   [1, 0, 0]
   [0, 1, 0]
   [0, 0, 1]
   ```

2. **Create Test Matrix A (3×3)**
   ```
   [2, 1, 0]
   [0, 3, 1]
   [1, 0, 2]
   ```

3. **Calculate Determinant**: Should be 11

4. **Calculate Inverse**: Get A⁻¹

5. **Multiply**: A × A⁻¹ ≈ Identity ✅

---

## Get Help

### Inside the App:
- **Settings tab** → "Application Information"
- **Register tab** → "Password Requirements"
- **Operations tab** → Clear error messages

### Common Error Messages:
| Error | Meaning | Fix |
|-------|---------|-----|
| "Singular matrix" | Determinant = 0 | Can't invert |
| "Dimensions don't match" | Size mismatch | Use same-sized matrices |
| "Incompatible dimensions" | Operation needs specific sizes | Check requirements |

---

**Ready to calculate? Start with registering an account!** 🚀
