#!/usr/bin/env python3
"""
CLI — Command-line interface for NFT floor monitoring.
"""
import json
import click
from rich.console import Console
from rich.table import Table
from .floor import FloorPriceFetcher

console = Console()


@click.command()
@click.argument("collection")
@click.option("--chain", "-c", default="ethereum", help="Blockchain")
@click.option("--output", "-o", type=click.Choice(["table", "json"]), default="table")
def main(collection, chain, output):
    """Monitor NFT floor prices."""
    fetcher = FloorPriceFetcher()
    data = fetcher.get_floor_price(collection)
    
    if not data:
        console.print(f"[red]Could not fetch data for {collection}[/red]")
        return
    
    if output == "json":
        console.print(json.dumps(data, indent=2))
        return
    
    table = Table(title=f"🖼️ {collection}", show_lines=True)
    table.add_column("Metric", style="cyan")
    table.add_column("Value", style="green")
    
    table.add_row("Floor Price", f"{data['floor_price']:.4f} {data['currency']}")
    table.add_row("Total Supply", f"{data['total_supply']:,}")
    table.add_row("Owners", f"{data['num_owners']:,}")
    table.add_row("Volume", f"{data['volume']:.2f} {data['currency']}")
    
    console.print(table)


if __name__ == "__main__":
    main()
