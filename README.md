1. Execute the jsonreader.sh file on the command line to run and test the functionality. Edit command as required.
    $ ./jsonreader.sh

2. You can edit the jsonreader.sh command line arguments with any input data file and output file of your choice.

3. The first argument must be the input data file, while the second argument is the outfile path.

4. You can also execute main.py directly by invoking the command below, and passing the input and output files respectively as arguments e.g:
   $ python3 main.py "data/data_1.json" "schema/schema_1.json"

5. You can execute test with the pytest command:
    $ pytest

6. You can also uncomment "pytest" in "jsonreader.sh" to execute pytest.

7. You can pass any key into the 'test_list' array in the "test_jsonFileReader.py" file to verify it's existence in the schema file.

Good luck.