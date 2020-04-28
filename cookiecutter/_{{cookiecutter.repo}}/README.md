{%- if cookiecutter.integration_level|int >= 4 -%}
[![logo](https://raw.githubusercontent.com/metwork-framework/resources/master/logos/metwork-white-logo-small.png)](http://www.metwork-framework.org)
{% endif -%}
# {{cookiecutter.repo}}

[//]: # (automatically generated from https://github.com/metwork-framework/resources/blob/master/cookiecutter/_%7B%7Bcookiecutter.repo%7D%7D/README.md)

**Status (master branch)**

{% set drone_managed = ("cat " + "REPO_HOME"|getenv + "/.drone.yml 2>/dev/null")|shell %}

{% if cookiecutter.integration_level|int >= 1 %}
{% if drone_managed != "" %}[![Drone CI](http://metwork-framework.org:8000/api/badges/metwork-framework/{{cookiecutter.repo}}/status.svg)](http://metwork-framework.org:8000/metwork-framework/{{cookiecutter.repo}}){% else %}[![GitHub CI](https://github.com/metwork-framework/{{cookiecutter.repo}}/workflows/CI/badge.svg?branch=master)](https://github.com/metwork-framework/{{cookiecutter.repo}}/actions?query=workflow%3ACI&branch=master){% endif %}
{%- endif %}
{%- if "docker-image" in "REPO_TOPICS"|getenv|from_json %}
[![DockerHub](https://github.com/metwork-framework/resources/blob/master/badges/dockerhub_link.svg)](https://hub.docker.com/r/metwork/{{cookiecutter.repo}}/)
{%- endif %}
{%- if cookiecutter.integration_level|int >= 1 %}
[![Maintenance](https://github.com/metwork-framework/resources/blob/master/badges/maintained.svg)]()
{%- endif %}
{%- if cookiecutter.integration_level|int >= 5 %}
[![License](https://github.com/metwork-framework/resources/blob/master/badges/bsd.svg)]()
{%- endif %}
{%- if cookiecutter.integration_level|int >= 4 %}
[![Gitter](https://github.com/metwork-framework/resources/blob/master/badges/community-en.svg)](https://gitter.im/metwork-framework/community-en?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge)
[![Gitter](https://github.com/metwork-framework/resources/blob/master/badges/community-fr.svg)](https://gitter.im/metwork-framework/community-fr?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge)
{%- endif %}
{{ ("cat " + "REPO_HOME"|getenv + "/.metwork-framework/EXTRA_BADGES.md 2>/dev/null")|shell }}

[//]: # (TABLE_OF_CONTENTS_PLACEHOLDER)

{{ ("cat " + "REPO_HOME"|getenv + "/.metwork-framework/README.md 2>/dev/null")|shell }}

{% if cookiecutter.repo not in ['mfext', 'mfsysmon', 'mfadmin'] and "mfextaddon" not in cookiecutter.repo %}
{% set components=("cat " + "REPO_HOME"|getenv + "/.metwork-framework/components.md 2>/dev/null")|shell %}

{% if components != "" %}
{% if "(0 component)" not in components %}

## Full list of components

{{ components }}

{% endif %}
{% endif %}

{% if cookiecutter.integration_level|int >= 5  or "mfextaddon_" in cookiecutter.repo %}
{% if cookiecutter.repo != "mfextaddon_template" %}

{% if "mfextaddon_" not in cookiecutter.repo %}

## Cheatsheet

A cheatsheet for this module is available [here](.metwork-framework/cheatsheet.md)

{% endif %}

## Reference documentation

- (for **master (development)** version), see [this dedicated site](http://metwork-framework.org/pub/metwork/continuous_integration/docs/master/{{cookiecutter.repo}}/) for reference documentation.
- (for **latest released stable** version), see [this dedicated site](http://metwork-framework.org/pub/metwork/releases/docs/stable/{{cookiecutter.repo}}/) for reference documentation.

For very specific use cases, you might be interested in
[reference documentation for integration branch](http://metwork-framework.org/pub/metwork/continuous_integration/docs/integration/{{cookiecutter.repo}}/).

And if you are looking for an old released version, you can search [here](http://metwork-framework.org/pub/metwork/releases/docs/).

{% endif %}

## Installation guide

See [this document](.metwork-framework/install_a_metwork_package.md).

{% if cookiecutter.repo != "mfext" %}
## Configuration guide

See [this document](.metwork-framework/configure_a_metwork_package.md).
{% endif %}
{% endif %}

{% else %}

## Quickstart, installation guide...

Please consult the [reference documentation](http://metwork-framework.org/pub/metwork/continuous_integration/docs/master/{{cookiecutter.repo}}/).

For very specific use cases, you might be interested in
[reference documentation for integration branch](http://metwork-framework.org/pub/metwork/continuous_integration/docs/integration/{{cookiecutter.repo}}/).

And if you are looking for an old released version, you can search [here](http://metwork-framework.org/pub/metwork/releases/docs/).
{% endif %}

## Contributing guide

See [CONTRIBUTING.md](CONTRIBUTING.md) file.

{% if cookiecutter.integration_level|int >= 2 %}

## Code of Conduct

See [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) file.

{% endif %}

## Sponsors

*(If you are officially paid to work on MetWork Framework, please contact us to add your company logo here!)*

[![logo](https://raw.githubusercontent.com/metwork-framework/resources/master/sponsors/meteofrance-small.jpeg)](http://www.meteofrance.com)
