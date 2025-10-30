from argparse import ArgumentParser

arg_parser = ArgumentParser()
arg_parser.add_argument("--name", store_true=True)
args = arg_parser.parse_args()

if args.name:
    print(f"Greetings argumented {args.name}")
else:
    name = input("Please enter a name: ")
    print(f"Greetings {name}")
