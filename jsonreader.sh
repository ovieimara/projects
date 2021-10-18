#!/usr/bin/env bash

#pip install pytest #uncomment to run pytest
#source venv/bin/activate #uncomment to run pytest

python3 main.py "data/data_2.json" "schema/schema_2.json"
python3 main.py "data/data_1.json" "schema/schema_1.json"

#uncomment to run pytest
#pytest
