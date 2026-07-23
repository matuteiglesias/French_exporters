def chunk(s):
    '''
    The function applied to the
    individual partition (map)
    '''    
    return s.apply(lambda x: list(set(x)))


def agg(s):
    '''
    The function whic will aggrgate 
    the result from all the partitions(reduce)
    '''
    s = s._selected_obj    
    return s.groupby(level=list(range(s.index.nlevels))).sum()


def finalize(s):
    '''
    The optional functional that will be 
    applied to the result of the agg_tu functions
    '''
    return s.apply(lambda x: len(set(x)))
