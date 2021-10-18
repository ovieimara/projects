#!/usr/bin/env bash

pip install pytest #comment after first run
source venv/bin/activate
python3 main.py "data/data_2.json" "schema/schema_2.json"
python3 main.py "data/data_1.json" "schema/schema_1.json"

#uncomment to run pytest
#pytest
