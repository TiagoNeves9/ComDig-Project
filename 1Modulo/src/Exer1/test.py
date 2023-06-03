import io
import os
import unittest
from contextlib import redirect_stdout
from math import isclose
from unittest.mock import patch

from Exer1.exerc5A import prog
from Exer1.exerc5B import mdc
from Exer1.exerc5D import hist_maker


# def test_GeometricProgression(N, u, r, expected_output):
#     with io.StringIO() as buf, redirect_stdout(buf):
#         prog(N, u, r)
#         actual_output = buf.getvalue().strip()
#         for i, term in enumerate(actual_output.split('\n')):
#             expected_term = expected_output[i]
#             assert isclose(float(term.split(':')[1]), expected_term, rel_tol=1e-9)
#
#
# class TestGeometricProgression(unittest.TestCase):
#     def test_output(self):
#         expected_output = [3.0, 6.0, 12.0, 24.0, 48.0]
#         test_input = (5, 3, 2)
#         test_GeometricProgression(*test_input, expected_output)


def test_mcd():
    assert mdc(10, 25) == 5
    assert mdc(16, 64) == 16
    assert mdc(14, 21) == 7
    assert mdc(36, 48) == 12


def test_histMaker():
    with open('test_file.txt', 'w') as f:
        f.write('aaaabbbcc\n')
    with patch('sys.stdout', new=io.StringIO()) as fakeOutput:
        hist_maker('test_file.txt')
        output = fakeOutput.getvalue()
        assert 'Informação Própria: 1.3219280948873622 para simbolo a' in output
        assert 'Informação Própria: 1.736965594166206 para simbolo b' in output
        assert 'Informação Própria: 2.321928094887362 para simbolo c' in output
        assert 'Informação Própria: 3.321928094887362 para simbolo ' in output
        assert 'Entropia: 1.8464393446710154' in output
    os.remove('test_file.txt')
    print("\nAll tests passed!\n")


print(test_mcd())
print(test_histMaker())
