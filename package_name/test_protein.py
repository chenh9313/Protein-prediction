## Description: "Return the gene structure information of target gene"
## Author: Huan Chen
## May-2021

"""Test subfunction4."""
import pytest
from protein import protein_sequence

@pytest.mark.parametrize('seq, result',
                        [('GAAATGATTACGAAGAAAATAAAT','ITKKIN'),
                         ('GAAATGATTACGAAGAAAATAAATAAAAAAAAAAAATTTTTGGGG','ITKKINKKKKFLG'),
                         ('GAAATGAGGGGC','RG')])
def test_protein_sequence(seq, result):
    """unittest function"""
    assert protein_sequence(seq) == result
