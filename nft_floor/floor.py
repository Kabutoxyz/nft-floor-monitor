"""
Floor — Fetch NFT floor prices from OpenSea API.
"""
import requests
from typing import Dict, Optional


class FloorPriceFetcher:
    """Fetch NFT floor prices from OpenSea."""
    
    BASE_URL = "https://api.opensea.io/api/v2"
    
    def __init__(self, api_key: Optional[str] = None):
        """Initialize fetcher with optional API key.
        
        Args:
            api_key: OpenSea API key for higher rate limits.
        """
        self.session = requests.Session()
        if api_key:
            self.session.headers["X-API-KEY"] = api_key
    
    def get_floor_price(self, collection_slug: str) -> Optional[Dict]:
        """Get floor price for an NFT collection.
        
        Args:
            collection_slug: OpenSea collection slug (e.g., 'boredapeyachtclub').
        
        Returns:
            Dict with floor_price, currency, and collection info.
        """
        try:
            resp = self.session.get(
                f"{self.BASE_URL}/collections/{collection_slug}/stats",
                timeout=15,
            )
            resp.raise_for_status()
            data = resp.json()
            
            return {
                "collection": collection_slug,
                "floor_price": data.get("floor_price", 0),
                "currency": "ETH",
                "total_supply": data.get("total_supply", 0),
                "num_owners": data.get("num_owners", 0),
                "volume": data.get("total_volume", 0),
            }
        except Exception as e:
            print(f"Error fetching floor price: {e}")
            return None
