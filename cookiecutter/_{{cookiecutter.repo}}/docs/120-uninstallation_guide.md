# Uninstallation guide

## How to uninstall {{cookiecutter.repo}} module

To uninstall {{cookiecutter.repo}} metwork module, use the following command (as `root` user):

```console tab="CentOS/Fedora"
{% if cookiecutter.repo != "mfext" %}
service metwork stop {{cookiecutter.repo}}
{% endif %}
yum remove "metwork-{{cookiecutter.repo}}*"
```

```console tab="Mageia"
{% if cookiecutter.repo != "mfext" %}
service metwork stop {{cookiecutter.repo}}
{% endif %}
urpme "metwork-{{cookiecutter.repo}}*"
```

```console tab="SUSE"
{% if cookiecutter.repo != "mfext" %}
service metwork stop {{cookiecutter.repo}}
{% endif %}
zypper remove "metwork-{{cookiecutter.repo}}*"
```

## How to uninstall all metwork modules

To uninstall all metwork modules, use following `root` commands:

```console tab="CentOS/Fedora"
# for CentOS or Fedora (see previous note for other distributions)
# We stop metwork services (see note below)
service metwork stop

# we remove metwork modules
yum remove "metwork-*"
```

```console tab="Mageia"
# for CentOS or Fedora (see previous note for other distributions)
# We stop metwork services (see note below)
service metwork stop

# we remove metwork modules
urpme "metwork-*"
```

```console tab="SUSE"
# for CentOS or Fedora (see previous note for other distributions)
# We stop metwork services (see note below)
service metwork stop

# we remove metwork modules
zypper remove "metwork-*"
```

!!! note
    If your distribution does not provide `service` command, you can use
    `systemctl stop metwork.service` instead or `/etc/rc.d/init.d/metwork stop`
    (if you don't have a `systemd` enabled machine or container).

!!! warning
    When you remove a module, the corresponding home directory will be deleted.
    For example, if you remove mfbase module, the `/home/mfbase` directory
    will be dropped. To avoid losing some work, the removal process will make a
    backup directoy in `/home/mfbase.rpmsave{date}` (without the content of
    `log` and `tmp` subdir). If you really want to clean all metwork stuff on
    this machine, you can also drop these backup directories. Same idea for
    `/etc/metwork.config.d/{module}`.
