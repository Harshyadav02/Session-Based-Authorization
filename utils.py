from functools  import wraps
from flask import session

#  function that will become the decorator and return the decoarter function
def requires_role(roles):
    #  function that will take the whole view function 
    def decorator(view_func):
        @wraps(view_func)
        #  this will check if the roleexixst or not in the flask session 
        def wrapped_view(*args, **kwargs):
            if session.get('role') in roles:
                return view_func(*args, **kwargs)
            else:
                return '<h1>You are not a authorized user for this page</h1>'

        return wrapped_view

    return decorator
