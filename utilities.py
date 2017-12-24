'''
    Benchmarks to measure the algorithms Performance are here.
'''

import dill # module to store and retrive python objects

def save_object(obj, filename):
    '''
    Here we open a file(.pkl file)(it gets created if it does not exist) and
    we store our python object in binary format
    '''
    with open(filename, 'wb') as output:
        dill.dump(obj, output)

def load_object(filename) :
    '''
    Here we retrive the python object from a .pkl file
    '''
    with open(filename,'rb') as input :
        obj = dill.load(input)
    return obj

def load_file(filename) :
    '''
    Normal file loading
    '''
    return open(filename,'r').read()
