# {{cookiecutter.repo}}

## Status (master branch)

{%- if cookiecutter.integration_level|int >= 1 %}
[![Drone CI](http://metwork-framework.org:8000/api/badges/metwork-framework/{{cookiecutter.repo}}/status.svg)](http://metwork-framework.org:8000/metwork-framework/{{cookiecutter.repo}})
{%- endif %}
{%- if cookiecutter.integration_level|int >= 1 %}
[![Maintenance](https://github.com/metwork-framework/resources/blob/master/badges/maintained.svg)]()
{%- endif %}
{%- if cookiecutter.integration_level|int >= 5 %}
[![License](https://github.com/metwork-framework/resources/blob/master/badges/bsd.svg)]() 
{%- endif %}
