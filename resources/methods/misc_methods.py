def quit_msg(msg=None):
    """ Print the msg (if any), then quit."""
    if msg: print(f'Quit message: {str(msg)}')
    quit()