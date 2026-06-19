import argparse

from snapshot.commands.init import init
from snapshot.commands.list_snap import list_snap
from snapshot.commands.save_snap import snapshot
from snapshot.commands.restore_snap import restore
from snapshot.commands.restore_latest import restore_latest
from snapshot.commands.info_snap import show_info
from snapshot.commands.delete_snap import delete
from snapshot.commands.stats_snap import stats

from snapshot.utils.console import print_help


def main():
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

    restore_latest_parser = subparsers.add_parser("restorelatest")
    restore_latest_parser.add_argument("--clean", action="store_true")

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

    elif args.command == "restorelatest":
        restore_latest(is_clean=args.clean)

    elif args.command == "del":
        delete(args.snap_id)

    elif args.command == "info":
        show_info(args.snap_id)

    elif args.command == "stats":
        stats()

    elif args.command == "list":
        list_snap()

    else:
        print_help()


if __name__ == "__main__":
    main()
