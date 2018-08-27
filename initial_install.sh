#! /usr/bin/env bash
if [[ ! "${BASH_SOURCE[0]}" != "${0}" ]]; then
    echo "Script must be sourced!"
    exit 1
fi

python3 -m venv venv/
source venv/bin/activate

# Must be done in this order
pip install -e pkg2
pip install -e pkg1
pip install -e pkg3
