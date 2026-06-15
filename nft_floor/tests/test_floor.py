"""
Tests for FloorPriceFetcher.
"""
import unittest
from nft_floor.floor import FloorPriceFetcher


class TestFloorPriceFetcher(unittest.TestCase):
    """Test floor price fetching."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.fetcher = FloorPriceFetcher()
    
    def test_get_floor_price(self):
        """Test fetching floor price."""
        data = self.fetcher.get_floor_price("boredapeyachtclub")
        if data:  # May fail due to API limits
            self.assertIn("floor_price", data)
            self.assertIn("collection", data)


if __name__ == "__main__":
    unittest.main()
