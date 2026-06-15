# nft-floor-monitor

Monitor NFT floor prices across collections with price alerts.

## Installation

```bash
pip install -e .
```

## Usage

```bash
# Check floor prices
nft-floor monitor boredapeyachtclub --chain ethereum

# Set price alert
nft-floor alert boredapeyachtclub --below 20

# View alerts
nft-floor alerts
```

## Features

- Real-time floor price tracking
- Price alerts (above/below thresholds)
- Multi-chain support
- Rich terminal output

## License

MIT
