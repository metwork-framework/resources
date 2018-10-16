# {{cookiecutter.repo}}

[//]: # (automatically generated from https://github.com/metwork-framework/resources/blob/master/cookiecutter/%7B%7Bcookiecutter.repo%7D%7D/README.md)

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

{{ ("cat " + "REPO_HOME"|getenv + "/.metwork-framework/README.md 2>/dev/null")|shell }}

## Contributing guide

See [CONTRIBUTING.md](CONTRIBUTING.md) file.

{% if cookiecutter.integration_level|int >= 2 %}


## Code of Conduct

See [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) file.

{% endif %}

