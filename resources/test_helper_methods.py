import pytest
from helper_methods import *

class TestQuitMsg:
    msgs = ['Message A', '0']
    symbols = ['`~!@#$%^&*\\|()-_=+[]{};:\'",<.>/?']
    numbers = ['0123', 4567, 8+9, 0o123]
    false_msgs = ['', 0, False, None]

    # messages that should print
    @pytest.mark.parametrize('msg', (msgs + symbols + numbers))
    def test_prints_message(self, capsys, msg):
        with pytest.raises(SystemExit):
            quit_msg(msg)
        assert str(msg) in capsys.readouterr().out

    # messages that should not print
    @pytest.mark.parametrize('msg', false_msgs)
    def test_prints_message(self, capsys, msg):
        with pytest.raises(SystemExit):
            quit_msg(msg)
        assert not capsys.readouterr().out