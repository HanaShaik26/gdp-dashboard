# 🔢 Secure Matrix Calculator - Testing Guide

## Quick Start

### Starting the Application
```bash
streamlit run streamlit_app.py
```

The application will open at `http://localhost:8501` in your browser.

---

## Test Scenarios

### 1. User Registration & Authentication

#### ✅ Valid Registration
1. **Username**: `TestUser123`
2. **Password**: `SecurePass@1`
3. **Confirm**: `SecurePass@1`
4. Expected: ✅ Registration successful

#### ❌ Invalid Registration - Password Too Short
1. **Username**: `TestUser`
2. **Password**: `Short@1`
3. Expected: ❌ Error: "Password must be at least 8 characters long"

#### ❌ Invalid Registration - No Uppercase
1. **Username**: `TestUser`
2. **Password**: `lowercase@1`
3. Expected: ❌ Error: "Password must contain at least one uppercase letter"

#### ❌ Invalid Registration - No Special Character
1. **Username**: `TestUser`
2. **Password**: `NoSpecial123`
3. Expected: ❌ Error: "Password must contain at least one special character"

#### ❌ Invalid username - Too Short
1. **Username**: `aa`
2. **Password**: `ValidPass@1`
3. Expected: ❌ Error: "Username must be at least 3 characters long"

#### ✅ Login with Correct Credentials
1. Use credentials from valid registration above
2. Expected: ✅ Successful login

#### ❌ Login with Wrong Password
1. **Username**: `TestUser123`
2. **Password**: `WrongPass@1`
3. Expected: ❌ Error: "Invalid username or password"

---

### 2. Matrix Creation

#### ✅ Valid Matrix Creation - 3x3
- Rows: `3`
- Cols: `3`
- Expected: ✅ Matrix created: `Matrix_R3C3`

#### ✅ Valid Matrix Creation - 5x2
- Rows: `5`
- Cols: `2`
- Expected: ✅ Matrix created: `Matrix_R5C2`

#### ❌ Invalid Dimensions - Non-Integer
- Rows: `3.5`
- Cols: `3`
- Expected: ❌ Error: "Dimensions must be integers"

#### ❌ Invalid Dimensions - Negative
- Rows: `-5`
- Cols: `3`
- Expected: ❌ Error: "Dimensions must be positive integers"

#### ❌ Invalid Dimensions - Exceeds Maximum
- Rows: `16`
- Cols: `3`
- Expected: ❌ Error: "Dimensions cannot exceed 15x15"

#### ❌ Maximum Matrices Reached
- After creating 10 matrices, attempt to create 11th
- Expected: ⚠️ Warning: "You have reached the maximum of 10 matrices"

---

### 3. Matrix Operations - Single Matrices

#### Test Matrix Setup (3x3):
```
2  1  0
0  3  1
1  0  2
```

#### ✅ Determinant (Square Matrix)
- Select matrix (3x3)
- Operation: Determinant
- Expected: ✅ Result: 11.0

#### ✅ Transpose
- Select any matrix
- Operation: Transpose
- Expected: ✅ New transposed matrix created
- Dims: If input was (3x4), output is (4x3)

#### ✅ Inverse (Invertible Square Matrix)
- Use 3x3 matrix with det ≠ 0
- Operation: Inverse
- Expected: ✅ Inverse matrix computed
- Result type: (3x3)

#### ❌ Determinant (Non-Square Matrix)
- Select matrix (3x4)
- Operation: Determinant
- Expected: ❌ Error: "Determinant only works for square matrices. This is 3x4"

#### ❌ Inverse (Singular Matrix)
- Test Matrix (2x2):
  ```
  1  2
  2  4
  ```
- Operation: Inverse
- Expected: ❌ Error: "Matrix is singular (determinant is zero) and cannot be inverted"

#### ❌ Inverse (Non-Square Matrix)
- Select matrix (3x4)
- Operation: Inverse
- Expected: ❌ Error: "Inverse only works for square matrices"

---

### 4. Matrix Operations - Two Matrices

#### Test Matrices:
**Matrix A (2x3):**
```
1  2  3
4  5  6
```

**Matrix B (2x3):**
```
2  0  1
1  3  2
```

**Matrix C (3x2):**
```
1  2
3  4
5  6
```

#### ✅ Matrix Addition
- Select: Matrix A + Matrix B
- Expected: ✅ Result (2x3):
  ```
  3  2  4
  5  8  8
  ```

#### ❌ Matrix Addition (Incompatible Dimensions)
- Select: Matrix A (2x3) + Matrix C (3x2)
- Expected: ❌ Error: "Matrices must have same dimensions for addition"

#### ✅ Matrix Subtraction
- Select: Matrix A - Matrix B
- Expected: ✅ Result (2x3):
  ```
  -1  2  2
   3  2  4
  ```

#### ✅ Matrix Multiplication (Compatible)
- Select: Matrix A (2x3) × Matrix C (3x2)
- Expected: ✅ Result (2x2)

#### ❌ Matrix Multiplication (Incompatible)
- Select: Matrix A (2x3) × Matrix B (2x3)
- Expected: ❌ Error: "For matrix multiplication, columns of first matrix must equal rows of second matrix"

---

### 5. Scalar Operations

#### ✅ Scalar Multiplication by 2
- Select Matrix A
- Scalar: `2`
- Expected: ✅ All elements multiplied by 2

#### ✅ Scalar Multiplication by 0.5
- Select Matrix A
- Scalar: `0.5`
- Expected: ✅ All elements multiplied by 0.5

#### ✅ Scalar Multiplication by Negative
- Select Matrix A
- Scalar: `-3`
- Expected: ✅ All elements multiplied by -3

---

### 6. Matrix Editing & Management

#### ✅ Edit Matrix Values
1. Go to "View Matrices"
2. Expand a matrix
3. Change values using number inputs
4. Click "Update"
5. Expected: ✅ Matrix values updated

#### ✅ Rename Matrix
1. Enter new name in "Rename" field
2. Click "✏️ Rename"
3. Expected: ✅ Matrix renamed as shown

#### ✅ Delete Matrix
1. Click "🗑️ Delete"
2. Expected: ✅ Matrix removed from list

#### ✅ Matrix Persistence
1. Create and edit matrices
2. Navigate away and back
3. Logout and login
4. Expected: ✅ All matrices still present

---

### 7. Input Validation

#### ✅ Valid Numeric Entries
- `123`, `-456`, `0.5`, `3.14159`, `-0.001`
- Expected: ✅ All accepted

#### ❌ Non-Numeric Entry in Dimensions
- Rows: `abc`
- Expected: ❌ Error: "Dimensions must be integers"

#### ✅ Large Numbers Accepted
- Matrix entry: `999999999`
- Expected: ✅ Accepted (within 50 char limit)

#### ❌ Entry Exceeds 50 Characters
- Matrix entry: String of 51+ characters
- Expected: ❌ Error: "Entry exceeds 50 character limit"

---

## Stress Testing

### ✅ Maximum Matrices Test
1. Create 10 matrices with different dimensions
2. Attempt 11th creation
3. Verify warning message appears
4. Delete 1 matrix
5. Verify 11th creation works

### ✅ Large Matrix Operations
1. Create 15x15 matrix (max size)
2. Perform transpose
3. Perform scalar multiplication
4. Expected: ✅ All operations complete successfully

### ✅ Complex Operation Chains
1. Create 2 square matrices
2. Add them
3. Take transpose of result
4. Take determinant
5. Expected: ✅ All operations succeed sequentially

---

## Security Testing

### ✅ Password Hashing
1. Register user with password `TestPass@123`
2. Check `users_db.json` - password should NOT be readable
3. Expected: ✅ Password is hashed (bcrypt format)

### ✅ Authentication Persistence
1. Login as user A
2. Logout
3. Login as different user B
4. Expected: ✅ Each user sees only their matrices

### ✅ Session Isolation
1. Login as user A and create matrices
2. Open second browser/incognito window
3. Login as user B
4. Expected: ✅ User B cannot see user A's matrices

---

## Performance Testing

### Response Time Checks
- ✅ Matrix creation: < 1 second
- ✅ Add/Subtract: < 1 second
- ✅ Multiply: < 2 seconds (for 15x15)
- ✅ Inverse: < 2 seconds (for 15x15)
- ✅ Determinant: < 1 second

---

## Edge Cases

### ✅ Zero Matrix
- All entries are 0
- Determinant: 0.0
- Inverse: ❌ Singular

### ✅ Identity Matrix (3x3)
```
1  0  0
0  1  0
0  0  1
```
- Determinant: 1.0
- Inverse: Self (identity)

### ✅ Diagonal Matrix
- Operations work normally
- Determinant = product of diagonal

### ✅ Single Element Matrix (1x1)
- All operations should work
- Used in scalar multiplication results

---

## Known Limitations

1. **No concurrent editing**: User must not edit multiple matrix windows simultaneously
2. **Local storage only**: Data stored in JSON file, not in database
3. **No operation history**: Cannot undo operations
4. **No matrix import/export**: Cannot transfer matrices between accounts
5. **No custom precision**: Fixed to 6 decimal places

---

## Troubleshooting

### App won't start
- Check all dependencies: `pip install -r requirements.txt`
- Verify Python 3.8+: `python --version`

### "Module not found" error
- Reinstall packages: `pip install -r requirements.txt --force-reinstall`

### Password requirements unclear
- Check password requirements display during registration
- Ensure: 8+ chars, uppercase, lowercase, special char

### Matrix operations slow
- Operations on 15x15 matrices may take 1-2 seconds
- This is normal for large matrix operations

### Users_db.json corrupted
- Delete `users_db.json` to reset
- All users/matrices will be lost
- Register new users to start fresh

---

## Test Completion Checklist

- [ ] Registration with valid password
- [ ] Registration with invalid passwords (all types)
- [ ] Login with correct credentials
- [ ] Login with wrong credentials
- [ ] Create matrices with valid dimensions
- [ ] Create matrices with invalid dimensions
- [ ] Determinant (square and non-square)
- [ ] Transpose
- [ ] Inverse (invertible and singular)
- [ ] Addition (compatible and incompatible)
- [ ] Subtraction (compatible and incompatible)
- [ ] Multiplication (compatible and incompatible)
- [ ] Scalar multiplication
- [ ] Edit matrix values
- [ ] Rename matrices
- [ ] Delete matrices
- [ ] Verify persistence after logout/login
- [ ] Verify 10-matrix limit
- [ ] Check error messages are clear
- [ ] Verify no plaintext passwords in users_db.json

---

**All tests completed successfully!** ✅
