# Snapshot

Snapshot is a code snapshotting tool, which lets you create snapshots of your whole codebase and then restore it whenever you wanna, essentially works like git but simpler.

## Basic Commands

- snap init - initializes your project (only needs to be run once in the project root)
- snap save <message> - saves the snapshot of your project
- snap list - lists all the saves
- snap restore <snap ID> - lets you restore your project to a certain save. Snap ID can be found in ``snap list``
- snap info <snap ID> - shows the info of a certain save. Snap ID can be found in ``snap list``

## Snap Ignore

- Lets you ignore certain files being included in the save. (as of now you cannot add /<dirname>, just mention the directory name.)

For example:
```
.env
__pycache__
venv

```

## Future Additions
- snap delete <id> - Lets you delete a certain save.
- snap diff <id1> <id2> - Lets you see the difference between two saves.