import pytest
import subprocess
import shlex
import os, fnmatch

import analex

test_cases = [("", "-k"), ("teste.c", "-k"), ("notexists.cm", "-k")]

for file in fnmatch.filter(os.listdir('tests'), '*.cm'):
    test_cases.append((file, "-k"))

@pytest.mark.parametrize("input_file, args", test_cases)
def test_execute(input_file, args):
    if input_file != '':
        path_file = 'tests/' + input_file
    else:
        path_file = ""

    cmd = "python analex.py {0} {1}".format(args, path_file)
    process = subprocess.Popen(shlex.split(cmd), stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    stdout, stderr = process.communicate()

    path_file = 'tests/' + input_file
    with open(path_file + ".lex.out", "r") as output_file:
        expected_output = output_file.read()

    # Debug
    print("Generated output (raw):")
    print(repr(stdout.decode("utf-8")))
    print("Expected output (raw):")
    print(repr(expected_output))

    generated_output = stdout.decode("utf-8").replace('\r\n', '\n').strip()
    expected_output = expected_output.replace('\r\n', '\n').strip()

    assert generated_output == expected_output, f"Generated: {repr(generated_output)}\nExpected: {repr(expected_output)}"