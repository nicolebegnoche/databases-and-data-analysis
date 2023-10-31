import os

# files cannot be written above this directory 
root_folder = os.getcwd()
reserved_chars = reserved_chars =  r'<>:"\|?*'

abs_ = lambda x: os.path.abspath(x)
join_ = lambda *x: os.path.join(*x)
exists_ = lambda x: os.path.exists(x)

class TestValidPathName:
    # valid_path_name(path)
    """ Return True if:
          - path is not empty, 
          - path does not use reserved characters, and
          - path is a subdirectory of the root folder.

        dependencies: none
    """



class TestCreatePath:
    # create_path(path)
    """Create a file or folder from user input"""
    # dependencies

class TestPathExists:
    # path_exists(path, doesnt_exist=None, msg=None)
    """" """



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