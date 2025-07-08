from bloxplorer import bitcoin_explorer as explorer
from bloxplorer.exceptions import BlockstreamApiError
from typing import Optional
from config import DEFAULT_ADDRESS
from rainbow import print_rainbow
import os

class BlockChaining:
    def __init__(self, btcaddy: str = DEFAULT_ADDRESS):
        self.btcaddy: str =  btcaddy
        self.formatted_balance: Optional[str] = None
        self.tx_count: Optional[int] = None
        self.transactions: list[dict] = []

    def fetch_info(self) -> bool:
        os.system('cls')
        print_rainbow(f'\t\t\t\t\t   fetching info for {self.btcaddy} \n                    $ - - - - - - - - - - - - - - - THE API ONLY PRINTS UP TO 25 TRANSACTIONS AT A TIME - - - - - - - - - - - - - - - $')

        try:
            result = explorer.addr.get(self.btcaddy)
            tx_hist = explorer.addr.get_tx_history(self.btcaddy)

            total_received = result.data['chain_stats']['funded_txo_sum'] / 1e8
            total_sent = result.data['chain_stats']['spent_txo_sum'] / 1e8
            balance = total_received - total_sent

            self.formatted_balance = f"{balance:,.8f}"
            self.tx_count = result.data['chain_stats']['tx_count']
            self.transactions = tx_hist.data
            return True
        except BlockstreamApiError as api_err:
            print_rainbow(f" API error: {api_err}")
            return False
        except KeyboardInterrupt as e:
            print_rainbow(f'u exited out : {e}')