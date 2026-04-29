# todo CLI usage

A small CLI for managing a JSON-backed todo list (stored in `todos.json`).

## add

Add a new todo.

Usage:

```
$ todo add "buy milk"
```

Arguments:
- `text` (positional, required): the todo text.

## list

List todos.

Usage:

```
$ todo list
$ todo list --only-open
```

Flags:
- `--only-open`: hide completed todos.

## done

Mark a todo done by id.

Usage:

```
$ todo done 3
```

Arguments:
- `id` (positional int, required): id of the todo to mark done.

## remove

Remove a todo by id.

Usage:

```
$ todo remove 3
```

Arguments:
- `id` (positional int, required): id of the todo to remove.
