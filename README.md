# Snapshot

Snapshot is a lightweight code snapshotting tool that allows you to save and restore your entire project at any point in time.

Think of it as a simpler alternative to Git when you just want quick save points without branches, commits, remotes, or repositories.

## Features

* Save snapshots of your entire project
* Restore previous snapshots at any time
* Ignore files and directories using `.snapignore`
* View snapshot history
* View detailed snapshot information
* Clean restore mode for exact project restoration
* Rich terminal interface

## Installation

```bash
pip install -r requirements.txt
```

## Usage

Initialize Snapshot in your project root:

```bash
snap init
```

Create a snapshot:

```bash
snap save "before authentication rewrite"
```

List all snapshots:

```bash
snap list
```

View information about a snapshot:

```bash
snap info 3
```

Restore a snapshot:

```bash
snap restore 3
```

Perform a clean restore (removes existing project files before restoring):

```bash
snap restore 3 --clean
```

## .snapignore

Use a `.snapignore` file in your project root to exclude files and directories from snapshots.

Example:

```text
.env
venv
__pycache__
node_modules
```

## Roadmap

* [ ] Delete snapshots (`snap delete <id>`)
* [ ] Compare snapshots (`snap diff <id1> <id2>`)
* [ ] Snapshot tags
* [ ] Snapshot search
* [ ] Snapshot export/import

```
```
