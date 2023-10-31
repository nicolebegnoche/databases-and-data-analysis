from resources.methods.misc_methods import *


class TestReturnTrue:
    """  return_true() returns True to demonstrate the link works. """
    def test_import_check(self):
        assert return_true()


if __name__ == '__main__':
    try:
        if return_true(): print('Success.')
        else: raise Exception('Neither success nor error')
    except Exception as error:
        print(f'Failure.\nReason: {error}')