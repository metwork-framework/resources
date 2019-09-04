#!/bin/bash

# find external dependencies (system) with a dynamic link with metwork libs

export PATH=${PATH}:${PWD}/..
RET=0

{% if "mfext-addon" not in "REPO_TOPICS"|getenv|from_json %}
cd "${MODULE_HOME}" || exit 1
external_dependencies.sh >deps
for F in $(cat deps); do
    N=$(ldd "${F}" 2>/dev/null |grep -c metwork)
    if test "$N" -gt 0; then
        echo "***** $F *****"
        echo "=== ldd |grep metwork ==="
        ldd "${F}" |grep metwork
        echo
        echo "=== revert ldd ==="
        revert_ldd.sh "${F}"
        echo
        echo
        RET=1
    fi
done
{% else %}
cd "${MFEXT_HOME}" || exit 1
cd opt
for layer in `ls`; do
    cd "${layer}"
    if test -f .mfextaddon; then
        addon="mfextaddon_"`cat .mfextaddon`
        if test "{{cookiecutter.repo}}" = "${addon}"; then
            echo
            echo "=== Suspicious dependencies layer ${layer} ==="
            echo
            external_dependencies.sh >deps
            for F in $(cat deps); do
                N=$(ldd "${F}" 2>/dev/null |grep -c metwork)
                if test "$N" -gt 0; then
                    echo "***** $F *****"
                    echo "=== ldd |grep metwork ==="
                    ldd "${F}" |grep metwork
                    echo
                    echo "=== revert ldd layer ${layer} ==="
                    revert_ldd.sh "${F}"
                    echo
                    echo
                    RET=1
                fi
            done
        fi
    fi
    cd ..
done


{% endif %}

rm -f deps
if test "${RET}" = "1"; then
    echo "suspicious dependencies found"
    #exit 1
fi
