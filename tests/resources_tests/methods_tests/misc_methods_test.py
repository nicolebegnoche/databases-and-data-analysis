import string
import pytest
from resources.methods.misc_methods import *


class TestQuitMsg:
    # quit_msg(msg=None)
    """Prints the message (if there is one), then quits"""

    msgs = ['My message', string.printable, string.punctuation]
    system = [BaseException, Exception, SystemError, SyntaxError, SystemExit]
    numbers = ['0123', 4567, 8+9, 0o123]
    false_msgs = ['', 0, False, None]
    
    # messages that should print
    @pytest.mark.parametrize('msg', (msgs + numbers + system))
    def test_print_message(self, capsys, msg):
        with pytest.raises(SystemExit):
            quit_msg(msg)
        assert str(msg) in capsys.readouterr().out

    # messages that should not print
    @pytest.mark.parametrize('msg', false_msgs)
    def test_skip_message(self, capsys, msg):
        with pytest.raises(SystemExit):
            quit_msg(msg)
        assert not capsys.readouterr().out 