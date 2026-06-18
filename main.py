import os, argparse

from commands.init import *
from commands.list_snap import *
from commands.save_snap import *
from commands.restore_snap import *

parser = argparse.ArgumentParser(prog="snap", description="Project snapshot manager")

subparsers = parser.add_subparsers(dest="command")

subparsers.add_parser("init")
subparsers.add_parser("list")

save_parser = subparsers.add_parser("save")
save_parser.add_argument("message")

restore_parser = subparsers.add_parser("restore")
restore_parser.add_argument("snap_id", type=int)

args = parser.parse_args()

if args.command == "init":
    init()

elif args.command == "save":
    snapshot(args.message)

elif args.command == "restore":
    restore(args.snap_id)

elif args.command == "list":
    list_snap()

else:
    parser.print_help()