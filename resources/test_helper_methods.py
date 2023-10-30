import pytest
import string
import re
import itertools

from resources.helper_methods import *

reserved_chars =  r'<>:"\|?*'

# @pytest.mark.skip(reason='testing_other_functions')
# class TestQuitMsg:
#     # header    quit_msg(msg=None)
#     # behavior  prints the message (if there is one), then quits
#     # return    none

#     msgs = ["My message", string.printable, string.punctuation]
#     system = [BaseException, Exception, SystemError, SyntaxError, SystemExit]
#     numbers = ['0123', 4567, 8+9, 0o123]
#     false_msgs = ['', 0, False, None]

#     # messages that should print
#     @pytest.mark.parametrize('msg', (msgs + numbers + system))
#     def test_print_message(self, capsys, msg):
#         with pytest.raises(SystemExit):
#             quit_msg(msg)
#         assert str(msg) in capsys.readouterr().out

#     # messages that should not print
#     @pytest.mark.parametrize('msg', false_msgs)
#     def test_skip_message(self, capsys, msg):
#         with pytest.raises(SystemExit):
#             quit_msg(msg)
#         assert not capsys.readouterr().out 


# @pytest.mark.skip(reason="in progress")
# TODO: implement pytest temporary directory fixtures
class TestCreatePath:
    # header:   def create_path(path)
    # behavior: create a file or folder according to user input
    # return:   True if path is created (pathor already existed); False

    tree = '___test/A/B/'     # keep trailing / for regex match
    setup_filenames = ['file.txt']  # needs to be in a list for itertools


    # valid_chars = ''.join((a for a in string.printable if a not in TestCreatePath.reserved_characters))
    # valid_chars = ''.join([a for a in string.printable if a not in TestCreatePath.reserved_characters])

    # @pytest.fixture
    # def test_tmp_dir(self):
    #     tree = __class__().tree
    #     filenames = __class__().filenames

    #     # remove top level folder if it exists
    #     if os.path.exists(folder := tree.split('/')[0]): shutil.rmtree(folder)

    #     # generate list of files
    #     delimiter_indices = (x.span()[0] for x in re.finditer('/', tree))
    #     folders = [tree[0:i+1] for i in delimiter_indices]
    #     files = [os.path.join(x,y) for (x,y) in itertools.product(folders, filenames)]

    #     # create folders and files
    #     os.makedirs(tree)
    #     for file in files:
    #         if not os.path.exists(file): open(file, 'w')

    #     # confirm creation
    #     assert os.path.exists(tree)
    #     for file in files: assert os.path.exists(file)

    @pytest.mark.parametrize('path', reserved_chars)
    def test_improper_path_name(self, path):
        with pytest.raises(SystemExit):
            create_path(f"a{path}b")

    @pytest.mark.parametrize('path', ['', ' ', '  '])
    def test_empty_path_name(self, path):
        with pytest.raises(SystemExit):
            create_path(path)       

    bad_paths = [
        '..',
        'a/b/../../..'
    ]

#     def test_path_goes_above_root_directory(path):
#         # quit with message if path attempts to go above the root directory
#         assert False

#     def test_path_already_exists(path):
#         # return True if the file or folder already exists
#         assert False
 
#     def test_path_doesnt_exist(path):
#        # create the new file or folder and return True
#         assert False

#     def test_some_folders_exist(path):
#         # create the missing folders (and file, if appropriate)
#         assert False



    # def test_rm_dir(self):
    #     top_folder = __class__().tree.split('/')[0]
    #     shutil.rmtree(top_folder)