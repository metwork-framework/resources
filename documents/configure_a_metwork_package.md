# How to configure a metwork package ?

## General

There are several ways to configure a metwork package (or a plugin).

It mainly depends:

- if you want to configure a metwork module (mfserv, mfbase, mfdata...) or a custom plugin
- if you are still developing
- if you are deploying in production

All these ways are not incompatible but in what follows, you will find our recommendations for each use case.

Please read everything from the beginning to be sure to really understand the configuration process.

### How to configure a metwork package (mfserv, mfbase, mfdata...) during development process ?

#### Find the module configuration file `config.ini`

You will find the module configuration file in `${MODULE_RUNTIME_HOME}/config/config.ini` path.

If you are developing with a standard metwork installation using a standard metwork user like `mfserv`, `mfdata`..., `${MODULE_RUNTIME_HOME}`
is the home directory of the current user. So, if you are developing with `mfserv` user, you will find the module configuration file
in `~/config/config.ini`.

Please make sure that your configuration file is not a symbolic link. In that particular case, you are in "production mode" 
(refer to the corresponding section).

#### Understand the inheritance process

The beginning of the file is something like that:

```
# THIS FILE OVERRIDES /opt/metwork-mfserv-master/config/config.ini CONFIGURATION FILE
# DON'T CHANGE ANYTHING IN /opt/metwork-mfserv-master/config/config.ini FILE
# DON'T REMOVE THE INCLUDE_config.ini LINE BELLOW
# => YOU CAN JUST SET THE KEY YOU WANT TO OVERRIDE BY REMOVING COMMENT
#    BEFORE THE KEY NAME AND BY CHANGING ITS VALUE HERE
[INCLUDE_config.ini]

[...]
```

So this file overrides `${MODULE_HOME}/config/config.ini` (`${MODULE_HOME}` is in `/opt` in a standard metwork installation).

**never change anything in `${MODULE_HOME}/config/config.ini`**
*(because this file is silently overriden after each metwork upgrade)*

So, you have to do your modifications in `${MODULE_RUNTIME_HOME}/config/config.ini` file (probably hosted in `/home`).

Note that, by default, all keys are commented. In that case, default values are read in `${MODULE_HOME}/config/config.ini`.

#### Override a key

To override a configuration option, select the corresponding key, uncomment it and change its value.

For example, to override the listening port of nginx daemon for `mfserv` module:

- edit `${MODULE_RUNTIME_HOME}/config/config.ini` as the user you use to run `mfserv` module
- find `[nginx]` section
- uncomment `port=...` key below
- change the value (for example `8080`)

#### Understand the link between "configuration file" and "environment variables"

The value in the configuration file is read only by a custom profile script that will transform into an environment variable.

Only this environment variable will be used by the rest of the module.

To resume the previous example, the key `port` in `[nginx]` section of the `mfserv` configuration file is put into 
`MFSERV_NGINX_PORT` environment variable.

In a more general way, every configuration option of module is stored in an environment variable: `{MODULE}_{SECTION}_{KEY}`.

And this environment variable is set **only during profile loading**. 

**VERY IMPORTANT : when you change the configuration file, it does not change existing environment variable so it does not change
daemons behaviour**

**To get the new value, you have to close/reopen your terminal to force a new profile loading**

**To change daemons and services behaviour (like `nginx` listening port in your example), you have to restart services from a 
newly restarted terminal or from a `root` user through `service metwork restart` command.**

To get current environment variables values for the current module, you can use for example:

```bash
env |grep "^${MODULE}_"
```

#### Understand what is overriden during module upgrades

During a metwork module upgrade :

- the default values file `${MODULE_HOME}/config/config.ini` (most of the time in `opt`) is silently overriden
- the custom values file `${MODULE_RUNTIME_HOME}/config/config.ini` (most of the time in `home`) is overriden by a new default one **only if there is no change in it**

So, if you changed some keys in `${MODULE_RUNTIME_HOME}/config/config.ini`, your change will never be overriden by a metwork upgrade.

But the upgrade add a new configuration option, the new configuration option will be (of course) visible in `${MODULE_HOME}/config/config.ini` but not in your `${MODULE_RUNTIME_HOME}/config/config.ini` (because we prefer to keep your changes). It's not a problem in itself but you can miss some configuration options. 

So, when you do some metwork ugprades on a customized system, you should sometimes do a kind of diff/merge between `${MODULE_RUNTIME_HOME}/config/config.ini` and `${MODULE_HOME}/config/config.ini`.

But again: if you don't do this, it won't break anything. But you can just miss some new configuration features.

### How to configure plugins during development process ?

FIXME

### How to configure a metwork package (mfserv, mfbase, mfdata...) during production deployment process ?

Of course, you can use the same way described above but we recommand another way for production deployment.

FIXME: /etc/metwork.config.d/mfserv/






