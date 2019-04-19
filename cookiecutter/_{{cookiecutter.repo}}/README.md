{%- if cookiecutter.integration_level|int >= 4 -%}
[![logo](https://raw.githubusercontent.com/metwork-framework/resources/master/logos/metwork-white-logo-small.png)](http://www.metwork-framework.org)
{% endif -%}
# {{cookiecutter.repo}}

[//]: # (automatically generated from https://github.com/metwork-framework/resources/blob/master/cookiecutter/_%7B%7Bcookiecutter.repo%7D%7D/README.md)

## Status (master branch)

{%- if cookiecutter.integration_level|int >= 1 %}
[![Drone CI](http://metwork-framework.org:8000/api/badges/metwork-framework/{{cookiecutter.repo}}/status.svg)](http://metwork-framework.org:8000/metwork-framework/{{cookiecutter.repo}})
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

{{ ("cat " + "REPO_HOME"|getenv + "/.metwork-framework/README.md 2>/dev/null")|shell }}

{% if cookiecutter.integration_level|int >= 5 %}
## Installation guide

See [this document](.metwork-framework/install_a_metwork_package.md).

{% if cookiecutter.repo != "mfext" and cookiecutter.repo != "mfcom" %}
## Configuration guide

See [this document](.metwork-framework/configure_a_metwork_package.md).
{% endif %}
{% endif %}

## Contributing guide

See [CONTRIBUTING.md](CONTRIBUTING.md) file.

{% if cookiecutter.integration_level|int >= 2 %}

## Code of Conduct

See [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) file.

{% endif %}
