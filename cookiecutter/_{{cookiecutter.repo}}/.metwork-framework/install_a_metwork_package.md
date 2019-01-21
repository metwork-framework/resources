# How to install/upgrade/remove {{cookiecutter.repo}} metwork package (with internet access)

[//]: # (automatically generated from https://github.com/metwork-framework/resources/blob/master/cookiecutter/_%7B%7Bcookiecutter.repo%7D%7D/.metwork-framework/install_a_metwork_package.md)

## Prerequisites

You must:

- have configured the metwork yum repository. Please see [the corresponding document](configure_metwork_repo.md) document to do that.
- have an internet access on this computer

## Install {{cookiecutter.repo}} metwork package

You just have to execute the following command (as `root` user):

```
yum install metwork-{{cookiecutter.repo}}
```

Of course, you can install several metwork packages on the same linux box.

{% if cookiecutter.repo != "mfcom" and cookiecutter.repo != "mfext" %}
You can start corresponding services with the root command:

```
service metwork start
```

Or you can also reboot your computer (because metwork services are started automatically on boot).
{% endif %}


## Uninstall {{cookiecutter.repo}} metwork package

{% if cookiecutter.repo != "mfcom" and cookiecutter.repo != "mfext" %}
To uninstall {{cookiecutter.repo}} metwork package, please stop corresponding metwork services with the `root` command:

```
# note: this is not necessary with mfext or mfcom
# because there is no corresponding services
service metwork stop {{cookiecutter.repo}}
```

Then, use the following command (still as `root` user):
{% else %}
To uninstall {{cookiecutter.repo}} metwork package, use the following command (still as `root` user):

{% endif %}

```
yum remove "metwork-{{cookiecutter.repo}}*"
```

## Uninstall all metwork packages

To uninstall all metwork packages, use following root commands:

```
# We stop metwork services
service metwork stop

# we remove metwork packages
yum remove "metwork-*"
```

## Upgrade all metwork packages

The same idea applies to upgrade.

For example, to upgrade all metwork packages on a computer, use following root commands:

```
# We stop metwork services
service metwork stop

# We upgrade metwork packages
yum upgrade "metwork-*"

# We start metwork services
service metwork start
```
