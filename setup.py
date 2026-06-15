from setuptools import setup, find_packages

setup(
    name="nft-floor-monitor",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "requests>=2.28",
        "rich>=13.0",
        "click>=8.0",
    ],
    entry_points={
        "console_scripts": [
            "nft-floor=nft_floor.cli:main",
        ],
    },
    author="Kabutoxyz",
    description="Monitor NFT floor prices with alerts",
    python_requires=">=3.9",
    license="MIT",
)
