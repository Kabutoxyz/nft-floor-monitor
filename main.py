#!/usr/bin/env python3
"""NFT Floor Price Monitor — Track collection floors."""
import requests, json, sys, time
from datetime import datetime

# Collection contract addresses
COLLECTIONS = {
    'BAYC': '0xBC4CA0EdA7647A8aB7C2061c2E118A18a936f13D',
    'CryptoPunks': '0xb47e3cd837dDF8e4c57F05d70Ab865de6e193BBB',
    'Azuki': '0xED5AF388653567Af2F388E6224dC7C4b3241C544',
    'Pudgy Penguins': '0xBd3531dA5CF5857e7CfAA92426877b022e612cf8',
    'Moonbirds': '0x23581767a106ae21c074b2276D25e5C3e136a68b',
}

def get_floor_price(contract):
    """Get floor price from Reservoir (free API)."""
    url = f'https://api.reservoir.tools/collections/v7?id={contract}'
    try:
        resp = requests.get(url, timeout=10, headers={'x-api-key': 'demo'})
        if resp.status_code == 200:
            collections = resp.json().get('collections', [])
            if collections:
                c = collections[0]
                return {
                    'floor': c.get('floorAsk', {}).get('price', {}).get('amount', {}).get('decimal', 0),
                    'top_bid': c.get('topBid', {}).get('price', {}).get('amount', {}).get('decimal', 0),
                    'volume_24h': c.get('volume', {}).get('24h', 0),
                    'count': c.get('tokenCount', 0),
                }
    except:
        pass
    return None

if __name__ == '__main__':
    print(f"🖼️ NFT Floor Monitor")
    print(f"⏰ {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    
    for name, contract in COLLECTIONS.items():
        data = get_floor_price(contract)
        if data:
            floor = data['floor']
            bid = data['top_bid']
            spread = ((floor - bid) / floor * 100) if floor > 0 and bid > 0 else 0
            print(f"  {name:18s} | Floor: {floor:>8.2f} ETH | Bid: {bid:>8.2f} ETH | Spread: {spread:.1f}%")
        else:
            print(f"  {name:18s} | Error fetching data")
        time.sleep(1)
