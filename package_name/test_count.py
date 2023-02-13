## Description: "Return the gene structure information of target gene"
## Author: Huan Chen
## May-2021

"""Test subfunction2."""
import pytest
from count import count_sequence

@pytest.mark.parametrize('seq, result',
                        [('ACGT',[1, 1, 1, 1]),
                         ('ACGTACGT',[2, 2, 2, 2]),
                         ('AAAACCCCGGGGTTTT',[4, 4, 4, 4])])


def test_count_sequence(seq, result):
    """unittest function"""
    assert count_sequence(seq) == result
