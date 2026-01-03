import argparse
import os.path
import shutil
import sys


def main():
    parser = argparse.ArgumentParser(description="argparse példa")

    parser.add_argument("nev", type=str, help="add meg a neved")

    parser.add_argument(
        "-n", "--number",
        type=int,
        default=1,
        help="ismétlések száma"
    )

    parser.add_argument(
        "operation",
        type=str,
        choices=["add", "subtract", "multiply", "divide"],
        help="művelet típusa"
    )

    parser.add_argument("--source", type=str, help="forrásfájl neve")

    parser.add_argument("--destination", type=str, help="célfájl neve")

    parser.add_argument("--debug", action="store_true", help="debug mód")

    args = parser.parse_args()

    if args.debug:
        print("[DEBUG] debug mód bekapcsolva")
        print(f'[DEBUG] args: {args}')

    print(f"helló {args.nev} - választott művelet: {args.operation}")

    if args.source and args.destination:
        if not os.path.exists(args.source):
            print(f'hiba: forrásfájl nem létezik: {args.source}')
            sys.exit(1)

        try:
            shutil.copy(args.source, args.destination)
            print(f"fájl másolva: {args.source} - > {args.destination}")
        except Exception as e:
            print(f'hiba másolás közben: {e}')
            sys.exit(1)

    for _ in range(args.number):
        print(f'művelet: {args.operation}')


main()
