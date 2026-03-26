"""
Matrix Operations module for Matrix Calculator
Handles all matrix operations with validation
"""

import numpy as np
from typing import Tuple, Optional, Union


MAX_MATRIX_DIMENSION = 15
ENTRY_MAX_LENGTH = 50


def validate_dimensions(rows: Union[int, str], cols: Union[int, str]) -> Tuple[bool, Optional[str]]:
    """
    Validate matrix dimensions.
    
    Args:
        rows: Number of rows
        cols: Number of columns
        
    Returns:
        tuple: (is_valid, error_message)
    """
    try:
        rows = int(rows)
        cols = int(cols)
    except (ValueError, TypeError):
        return False, "Dimensions must be integers"
    
    if rows < 1 or cols < 1:
        return False, "Dimensions must be positive integers"
    
    if rows > MAX_MATRIX_DIMENSION or cols > MAX_MATRIX_DIMENSION:
        return False, f"Dimensions cannot exceed {MAX_MATRIX_DIMENSION}x{MAX_MATRIX_DIMENSION}"
    
    return True, None


def validate_entry(entry: str) -> Tuple[bool, Optional[str]]:
    """
    Validate matrix entry.
    
    Args:
        entry: String entry (should be numeric)
        
    Returns:
        tuple: (is_valid, error_message)
    """
    if len(entry) > ENTRY_MAX_LENGTH:
        return False, f"Entry exceeds {ENTRY_MAX_LENGTH} character limit"
    
    try:
        float(entry)
        return True, None
    except ValueError:
        return False, "Entry must be a number"


def create_matrix(rows: int, cols: int) -> dict:
    """Create empty matrix structure."""
    return {
        "rows": rows,
        "cols": cols,
        "data": [[0.0 for _ in range(cols)] for _ in range(rows)],
        "name": f"Matrix_R{rows}C{cols}"
    }


def list_to_np_array(matrix_data: list) -> np.ndarray:
    """Convert matrix list to numpy array."""
    try:
        return np.array(matrix_data, dtype=float)
    except (ValueError, TypeError):
        return None


def determinant(matrix_dict: dict) -> Tuple[bool, Union[float, str]]:
    """
    Calculate determinant of a square matrix.
    
    Returns:
        tuple: (success, result or error_message)
    """
    if matrix_dict["rows"] != matrix_dict["cols"]:
        return False, f"Determinant only works for square matrices. This is {matrix_dict['rows']}x{matrix_dict['cols']}"
    
    try:
        arr = list_to_np_array(matrix_dict["data"])
        if arr is None:
            return False, "Invalid matrix data"
        det = float(np.linalg.det(arr))
        return True, det
    except np.linalg.LinAlgError:
        return False, "Cannot compute determinant for this matrix"
    except Exception as e:
        return False, f"Error computing determinant: {str(e)}"


def transpose(matrix_dict: dict) -> Tuple[bool, Union[dict, str]]:
    """
    Transpose a matrix.
    
    Returns:
        tuple: (success, transposed_matrix or error_message)
    """
    try:
        arr = list_to_np_array(matrix_dict["data"])
        if arr is None:
            return False, "Invalid matrix data"
        
        transposed_arr = np.transpose(arr)
        result = {
            "rows": transposed_arr.shape[0],
            "cols": transposed_arr.shape[1],
            "data": transposed_arr.tolist(),
            "name": f"{matrix_dict['name']}_T"
        }
        return True, result
    except Exception as e:
        return False, f"Error transposing matrix: {str(e)}"


def inverse(matrix_dict: dict) -> Tuple[bool, Union[dict, str]]:
    """
    Calculate inverse of a square matrix.
    
    Returns:
        tuple: (success, inverse_matrix or error_message)
    """
    if matrix_dict["rows"] != matrix_dict["cols"]:
        return False, f"Inverse only works for square matrices. This is {matrix_dict['rows']}x{matrix_dict['cols']}"
    
    try:
        arr = list_to_np_array(matrix_dict["data"])
        if arr is None:
            return False, "Invalid matrix data"
        
        det = np.linalg.det(arr)
        if abs(det) < 1e-10:
            return False, "Matrix is singular (determinant is zero) and cannot be inverted"
        
        inverse_arr = np.linalg.inv(arr)
        result = {
            "rows": inverse_arr.shape[0],
            "cols": inverse_arr.shape[1],
            "data": inverse_arr.tolist(),
            "name": f"{matrix_dict['name']}_Inv"
        }
        return True, result
    except np.linalg.LinAlgError:
        return False, "Matrix is singular and cannot be inverted"
    except Exception as e:
        return False, f"Error computing inverse: {str(e)}"


def add_matrices(matrix1: dict, matrix2: dict) -> Tuple[bool, Union[dict, str]]:
    """
    Add two matrices.
    
    Returns:
        tuple: (success, result_matrix or error_message)
    """
    if matrix1["rows"] != matrix2["rows"] or matrix1["cols"] != matrix2["cols"]:
        return False, (
            f"Matrices must have same dimensions for addition. "
            f"Matrix 1: {matrix1['rows']}x{matrix1['cols']}, "
            f"Matrix 2: {matrix2['rows']}x{matrix2['cols']}"
        )
    
    try:
        arr1 = list_to_np_array(matrix1["data"])
        arr2 = list_to_np_array(matrix2["data"])
        
        if arr1 is None or arr2 is None:
            return False, "Invalid matrix data"
        
        result_arr = arr1 + arr2
        result = {
            "rows": result_arr.shape[0],
            "cols": result_arr.shape[1],
            "data": result_arr.tolist(),
            "name": f"{matrix1['name']}_+_{matrix2['name']}"
        }
        return True, result
    except Exception as e:
        return False, f"Error adding matrices: {str(e)}"


def subtract_matrices(matrix1: dict, matrix2: dict) -> Tuple[bool, Union[dict, str]]:
    """
    Subtract two matrices.
    
    Returns:
        tuple: (success, result_matrix or error_message)
    """
    if matrix1["rows"] != matrix2["rows"] or matrix1["cols"] != matrix2["cols"]:
        return False, (
            f"Matrices must have same dimensions for subtraction. "
            f"Matrix 1: {matrix1['rows']}x{matrix1['cols']}, "
            f"Matrix 2: {matrix2['rows']}x{matrix2['cols']}"
        )
    
    try:
        arr1 = list_to_np_array(matrix1["data"])
        arr2 = list_to_np_array(matrix2["data"])
        
        if arr1 is None or arr2 is None:
            return False, "Invalid matrix data"
        
        result_arr = arr1 - arr2
        result = {
            "rows": result_arr.shape[0],
            "cols": result_arr.shape[1],
            "data": result_arr.tolist(),
            "name": f"{matrix1['name']}_-_{matrix2['name']}"
        }
        return True, result
    except Exception as e:
        return False, f"Error subtracting matrices: {str(e)}"


def multiply_matrices(matrix1: dict, matrix2: dict) -> Tuple[bool, Union[dict, str]]:
    """
    Multiply two matrices.
    
    Returns:
        tuple: (success, result_matrix or error_message)
    """
    if matrix1["cols"] != matrix2["rows"]:
        return False, (
            f"For matrix multiplication, columns of first matrix must equal rows of second matrix. "
            f"Matrix 1: {matrix1['rows']}x{matrix1['cols']} (cols={matrix1['cols']}), "
            f"Matrix 2: {matrix2['rows']}x{matrix2['cols']} (rows={matrix2['rows']})"
        )
    
    try:
        arr1 = list_to_np_array(matrix1["data"])
        arr2 = list_to_np_array(matrix2["data"])
        
        if arr1 is None or arr2 is None:
            return False, "Invalid matrix data"
        
        result_arr = np.matmul(arr1, arr2)
        result = {
            "rows": result_arr.shape[0],
            "cols": result_arr.shape[1],
            "data": result_arr.tolist(),
            "name": f"{matrix1['name']}_*_{matrix2['name']}"
        }
        return True, result
    except Exception as e:
        return False, f"Error multiplying matrices: {str(e)}"


def scalar_multiply(matrix_dict: dict, scalar: Union[int, float, str]) -> Tuple[bool, Union[dict, str]]:
    """
    Multiply matrix by a scalar.
    
    Returns:
        tuple: (success, result_matrix or error_message)
    """
    try:
        scalar = float(scalar)
    except (ValueError, TypeError):
        return False, "Scalar must be a number"
    
    try:
        arr = list_to_np_array(matrix_dict["data"])
        if arr is None:
            return False, "Invalid matrix data"
        
        result_arr = arr * scalar
        result = {
            "rows": result_arr.shape[0],
            "cols": result_arr.shape[1],
            "data": result_arr.tolist(),
            "name": f"{scalar}*{matrix_dict['name']}"
        }
        return True, result
    except Exception as e:
        return False, f"Error with scalar multiplication: {str(e)}"


def update_matrix_entry(matrix_dict: dict, row: int, col: int, value: Union[int, float, str]) -> Tuple[bool, Optional[str]]:
    """
    Update a single entry in a matrix.
    
    Returns:
        tuple: (success, error_message if any)
    """
    try:
        value = float(value)
        if row < 0 or row >= matrix_dict["rows"] or col < 0 or col >= matrix_dict["cols"]:
            return False, "Row or column index out of bounds"
        
        matrix_dict["data"][row][col] = value
        return True, None
    except ValueError:
        return False, "Value must be a number"
    except Exception as e:
        return False, f"Error updating entry: {str(e)}"
