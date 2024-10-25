def repeat_5_times(fn):
    """_summary_

    Args:
        fn (function): _description_
    """    
    def wrapper(*args,**kwargs):       
        for _ in range(5):
            fn(*args,**kwargs)
    return wrapper      


@repeat_5_times
def say(message):
    ''' print the message 
    Arguments
        message: the message to show
    '''
    print(message)
    
say('Hi')    