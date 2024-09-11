import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Util.Helper import Helper

# def test_print_options(capfd):
#     options = ['Option1', 'Option2', 'Option3']
#     Helper.print_options(options)
    
#     captured = capfd.readouterr()
    
#     expected_output = '\033[92m1. Option1\033[0m\n\033[92m2. Option2\033[0m\n\033[92m3. Option3\033[0m\n'
#     print(expected_output)
#     assert captured.out == expected_output

# def test_get_valid_input_valid(monkeypatch):
#     monkeypatch.setattr('builtins.input', lambda _: '2')
#     result = Helper.get_valid_input(3)
#     assert result == 2

# def test_get_valid_input_invalid_then_valid(monkeypatch, capsys):
#     inputs = iter(['a', '2'])
#     monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    
#     result = Helper.get_valid_input(3)
#     assert result == 2

#     captured = capsys.readouterr()
#     assert '\033[91mInvalid option\033[0m' in captured.out