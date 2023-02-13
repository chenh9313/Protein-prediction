"""Test subfunction3."""
import pytest
from structure import structure_gene

@pytest.mark.parametrize('locus, result',
                        [('AT5G59890',4),
                         ('AT5G59880',6),
                         ('AT1G59880',0)])
def test_structure_gene(locus, result):
    """unittest function"""
    assert structure_gene(locus) == result
