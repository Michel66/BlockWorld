# test_blockworld.py
"""
Tests for BlockWorld module.
"""

import unittest
from blockworld import BlockWorld

class TestBlockWorld(unittest.TestCase):
    """Test cases for BlockWorld class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = BlockWorld()
        self.assertIsInstance(instance, BlockWorld)
        
    def test_run_method(self):
        """Test the run method."""
        instance = BlockWorld()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
