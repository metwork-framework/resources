# Plugin guide

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

The best way is 
