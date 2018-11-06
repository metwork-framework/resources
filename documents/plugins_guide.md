# Plugins guide

## General

This document is a generic one about plugins. It covers `mfserv`, `mfdata` and `mfbase` plugins.

## Commands (as corresponding metwork user)

### `plugins.list`

List installed plugins.

Note: if you have a version named `dev_link`, the plugin is installed as a symbolic link to a source directory. 
It's a kind of "development mode".

### `plugins.install`

Install a given plugin (`.plugin`) file.

### `plugins.uninstall`

Uninstall a given plugin **name** (not file). The name corresponds to the first column of `plugins.list` output.

### `plugin_env`

If you have a virtualenv in your plugin or if you want to simulate the exact environment your code will run in the context
of your plugin, you can use the `plugin_env` interactive command.

If you are developping, the best way is to go in the root directory of your plugin and use `plugin_env` without argument.

If you have a "normal" installed plugin, you can use `plugin_env {PLUGIN_NAME}`.

When you are inside a plugin environment, you will find some extra environment variables:

```
# Example with MFSERV, but it's the same idea with MFDATA or MFBASE
MFSERV_CURRENT_PLUGIN_NAME=dashboard
MFSERV_CURRENT_PLUGIN_DIR=/home/mfserv/var/plugins/dashboard
MFSERV_CURRENT_PLUGIN_LABEL=plugin_dashboard@mfserv
```

### `plugin_wrapper`

This command follows the same idea than `plugin_env` but in a non-interactive way. Use it for example for `crontabs` or if you want to execute a command in a given plugin environment without changing anything to the current shell.

```
plugin_wrapper {PLUGIN_NAME} {COMMAND} [{COMMAND_ARG1}] [{COMMAND_ARG2}] [...]
```

Note: the plugin must be installed





