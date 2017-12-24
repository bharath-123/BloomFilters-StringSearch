'''
    String searching algorithms integrated with bloom filter collections. The speed ups are here folks!!
'''


from filter_col import *
from stringsearchalgos import *
import multiprocessing as mp


def multiprocess_naive(processes,pattern,text,section_size,selection_list) :
    '''
        Parallelizing the searching
    '''
    pool = mp.Pool(processes = processes)
    results = [pool.apply_async(FAsearch,args = (pattern,text[i*(section_size) : (i + 1)*section_size])) for i in selection_list]
    results = [p.get() for p in results]
    return sum(results)

def parallel_search_naive(col,pattern,genome) :
    '''
        Parallelizing the bloom filter searching
    '''
    occurences = []
    selection_list = []#will have the sections to look at
    section_size = int(len(genome) / (col.k))
    for i in range(col.k) :
        if col.collection[i].bloom_check(pattern) :
            occurences.append(1)
        else :
            occurences.append(0)
    for j in range(len(occurences)) :
        if occurences[j] == 1 :
            selection_list.append(j)
    return multiprocess_naive(3,pattern,genome,section_size,selection_list)

def serial_search_naive(col,pattern,genome) :
    '''
        String search using bloom filters but is done serially i.e all bloom filters are checked one by one
    '''
	occurences = []
	count = 0
	section_size = int(len(genome) / (col.k))
	for i in range(col.k) :
		if col.collection[i].bloom_check(pattern) :
			count += FAsearch(pattern,genome[i*section_size : (i + 1)*section_size])
			occurences.append(1)
		else :
			occurences.append(0)
	return count,occurences
