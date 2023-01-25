# STYLE ***************************************************************************
# content = assignment
#
# date    = 2022-01-07
# email   = contact@alexanderrichtertd.com
#************************************************************************************

# original: logging.init.py

def findCaller(self):
    """
    Find the stack frame of the caller so that we can note the source
    file name, line number and function name.
    """
    f = currentframe()
    #On some versions of IronPython, currentframe() returns None if
    #IronPython isn't run with -X:Frames.
    if f is not None:
        f = f.f_back
    rv = "(unknown file)", 0, "(unknown function)"
    while hasattr(f, "f_code"):
        co = f.f_code
        filename = os.path.normcase(co.co_filename)
        if filename == _srcfile:
            f = f.f_back
            continue
        rv = (co.co_filename, f.f_lineno, co.co_name)
        break
    return rv

# How can we make this code better?
#***********************************************************************
#ASSIGMENT:

def findCaller(self):
    """
    Find the stack frame of the caller so that we can note the source
    file name, line number and function name.
    """
    current_frame = currentframe()
    #On some versions of IronPython, currentframe() returns None if
    #IronPython isn't run with -X:Frames.
    if current_frame is not None:
        current_frame = current_frame.frame_back
    #not sure what should be called, I will use reverse return_version just in case
    return_version = "(unknown file)", 0, "(unknown function)"
    while hasattr(current_frame, "currentframe_code"):
        frame_code = current_frame.frame_code
        filename = os.path.normcase(frame_code.frame_code_filename)
        if filename == _srcfile:
            current_frame = current_frame.frame_back
            continue
        return_version = (frame_code.frame_code_filename, current_frame.current_frame_lineno, frame_code.frame_code_name)
        break
    return return_version
