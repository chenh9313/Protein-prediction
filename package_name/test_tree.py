## Description: "Return the gene structure information of target gene"
## Author: Huan Chen
## May-2021

"""Test subfunction6."""
import pytest
from tree import tree_builder

@pytest.mark.parametrize('num1, num2, result',
                        [(3,[("ADF1","ADF2"),("ADF1","ADF3")],'1.3333'),
                         (4,[("ADF1","ADF2"),("ADF1","ADF3"),("ADF1","ADF4")],'1.5000'),
(5,[("ADF1","ADF2"),("ADF1","ADF3"),("ADF1","ADF4"),("ADF1","ADF5")],'1.6000')]) 
def test_tree_builder(num1, num2, result):
    """unittest function"""
    assert tree_builder(num1, num2) == result
