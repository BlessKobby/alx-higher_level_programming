#!/usr/bin/python3.5
"""

Module composed by a function that multiplies two matrices.

"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """ Function that multiplies two  matrices

    Args:
        m_a: matrix a
        m_b: matrix b

    Returns:
        result of the multiplication


    """

    return (np.matmul(m_a, m_b))
