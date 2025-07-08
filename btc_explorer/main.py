import argparse
from explorer import BlockChaining
from display import show_summary, show_transactions

def main():
    parser = argparse.ArgumentParser(description="btc addy lookup")
    parser.add_argument(
        "-t", "--target",
        help="use -t <bitcoin_address>",
        required=False
    )
    args = parser.parse_args()

    # Pass address if provided, otherwise use default from config
    b = BlockChaining(btcaddy=args.target) if args.target else BlockChaining()

    if b.fetch_info():
        show_summary(b)
        show_transactions(b, limit=25)

if __name__ == "__main__":
    main()
