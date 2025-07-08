from explorer import BlockChaining
from colorama import init, Fore, Back, Style
import random
import time
from rich.console import Console
from rich.text import Text
from rainbow import print_rainbow

def show_summary(bc: BlockChaining) -> None:
    print_rainbow(f"\t\t\t\t   Balance: {bc.formatted_balance} BTC", )
    print_rainbow(f"\t\t\t\t   Total Transactions: {bc.tx_count}", )

def show_transactions(bc: BlockChaining, limit: int = 25) -> None:

    colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA]

    print_rainbow(f"\n\t\t\t\t   Showing up to {limit} transactions:",)

    for i, tx in enumerate(bc.transactions[:limit]):
        fee_btc = tx.get('fee', 0) / 1e8
        color = random.choice(colors)  # Cycle through colors
        print_rainbow(f"\t\t\t\t   {color}] {tx['txid']} — Fee: {fee_btc:.8f} BTC{Style.RESET_ALL}")
        time.sleep(1)
