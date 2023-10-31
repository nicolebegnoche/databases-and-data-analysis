import resources.methods.misc_methods as misc


def call_misc():
    """ Check for response from misc_methods. """
    return True if misc.return_true() else False


if __name__ == '__main__':
    print(f'Checking link to "{misc.__name__}"...  ', end='')
    
    try:
        if call_misc(): print('Success.')
        else: raise Exception('Neither success nor error.')
    except Exception as error:
        print(f'Failure.\nReason: {error}')