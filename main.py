import argparse

from commands.init import *
from commands.list_snap import *
from commands.save_snap import *
from commands.restore_snap import *
from commands.info_snap import *
from commands.delete_snap import *
from commands.stats_snap import *

from utils.console import print_help

parser = argparse.ArgumentParser(
    prog="snap",
    description="Project snapshot manager",
    add_help=False,
)

subparsers = parser.add_subparsers(dest="command")

subparsers.add_parser("init")
subparsers.add_parser("list")
subparsers.add_parser("stats")

save_parser = subparsers.add_parser("save")
save_parser.add_argument("message")

restore_parser = subparsers.add_parser("restore")
restore_parser.add_argument("snap_id", type=int)
restore_parser.add_argument("--clean", action="store_true")

info_parser = subparsers.add_parser("info")
info_parser.add_argument("snap_id", type=int)

del_parser = subparsers.add_parser("del")
del_parser.add_argument("snap_id", type=int)

args = parser.parse_args()

if args.command == "init":
    init()

elif args.command == "save":
    snapshot(args.message)

elif args.command == "restore":
    restore(args.snap_id, clean=args.clean)

elif args.command == "del" or "delete":
    delete(args.snap_id)

elif args.command == "info":
    show_info(args.snap_id)

elif args.command == "stats":
    stats()

elif args.command == "list":
    list_snap()

else:
    print_help()