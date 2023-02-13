"""Test subfunction6."""
import pytest
from partThree.py import BuildTree

class TestCase(unittest.TestCase):
    def test(self):
        tree_builder = BuildTree()
        self.asserEqual(BuildTree.tree_builder(4,[("ADF1","ADF2"),("ADF1","ADF3"),("ADF1","ADF4")]),'1.5000')

if _name_ == '_main_':
    unittest.main()
