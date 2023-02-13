"""Test subfunction1."""
import pytest
from download import download_sequence

@pytest.mark.parametrize('genename, link, result',
                        [('ADF4','https://www.arabidopsis.org/servlets/\
TairObject?type=sequence&id=2002976339',1565),
                         ('ADF9','https://www.arabidopsis.org/servlets/\
TairObject?type=sequence&id=2503952629',1252),
                         ('ADF1','https://www.arabidopsis.org/servlets/\
TairObject?type=sequence&id=2002970347',1452)])

def test_download_sequence(genename, link, result):
    """unittest function"""
    assert download_sequence(genename, link) == result
