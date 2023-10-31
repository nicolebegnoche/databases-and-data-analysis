import importlib
app = importlib.import_module('intro-to-data-mining.main')

class TestCallMisc:
    """ call_misc()  checks for a response from misc_methods.
    
    Sig:    call_misc() -> boolean
    Returns True if function receives a response from misc.import_check
    """
    def test_call_misc(self):
        assert app.call_misc()


if __name__ == '__main__':
    print(f'Checking link to "{app.__name__}"...  ', end='')
    try:
        if app.call_misc(): print('Success.')
        else: raise Exception('Neither success nor error.')
    except Exception as error:
        print(f'Failure.\nReason: {error}')