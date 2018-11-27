#!/bin/bash
# automatically generated from https://github.com/metwork-framework/resources/blob/master/cookiecutter/_%7B%7Bcookiecutter.repo%7D%7D/mfxxx_drone.yml template

{% if cookiecutter.repo|fnmatch('mf*-integration-tests-runner') %}
    {% set LIST = cookiecutter.repo.split("-") %}
    {% set MODULE = LIST[0] %}
{% else %}
    {% set MODULE = "" %}
{% endif %}

cd {{MODULE}}/integration_tests

if test $? != 0; then
    echo "Directory integration_tests is missing"
    exit 0
fi

list_rep=`ls`
if test -z "$list_rep"; then
    echo "There are no integration tests"
    exit 0
fi

ret=0
for rep in $list_rep; do
    if [ -d $rep ]; then
        cd $rep
{% if MODULE == "mfext" %}
        LAYERS_TO_LOAD=`cat .layerapi2_dependencies |xargs |sed 's/ /,/g'`
{% endif %}
        for test in test*.sh; do
            echo "Test" $test "in" $rep
{% if MODULE == "mfext" %}
            layer_wrapper --layers=$LAYERS_TO_LOAD -- ./$test
{% else %}
            ./$test
{% endif %}
            if test $? == 0; then
                echo "Test $test OK"
            else
                echo "Test $test KO"
                ret=1
            fi
        done
        cd ..
    fi
done

exit $ret
