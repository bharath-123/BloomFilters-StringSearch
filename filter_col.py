'''
	The filter collection class is defined here.
	Also functions which create the bloom filter collection and initiate the string search are here
'''

from bloom import Bloom
from utilities import *
import time
from search import *
from parsers import Parser
from benchmarks import *
from stringsearchalgos import *
import os


class FilterCollection() :
    #k is the number of bloom filters and segment_size is the length of pattern
	def __init__(self,k,segment_size = 60) :

	    self.collection = []
	    self.k = k
	    self.segment_size = segment_size

	def create_collection(self,genome) :

	    section_size = int(len(genome) / (self.k))
	    for i in range(self.k):
	        section = genome[i*(section_size) : (i + 1)*(section_size)]
	        bloom = Bloom(1000000000,0.3)
	        for k in range(0,len(section) - segment_size + 1) :
	            s = section[k : k + segment_size]
	            bloom.bloom_add(s)
	        self.collection.append(bloom)
	    print("Collection created successfully")
	    self.collection = tuple(self.collection)


#create a bloom filter collection of specie(file must be in pwd) where the length of the pattern you want to search for is of size(defaults to 60)
def Create_BloomFilter_Collection(text,size = 60,no_of_bloom_filters=15) :
	'''
	Creates the bloom filter collection and stores it in a folder 'Collections' (will be created if not there)
	bloom filter collection size can be specified i.e by no_of_bloom_filters
	'''
	DNA = open(text,'r+').read()
	print("Creating Collection of " + text.split('.')[0] + "\n")
	col = FilterCollection(no_of_bloom_filters,size)
	col.create_collection(DNA)
	if 'Collections' not in os.listdir('.') :
		os.mkdir('Collections')
	print("Saving object")
	save_object(col,'./Collections/'+ text.split('.')[0] +'Collection.pkl')
	print("Saved Object")

#search for a pattern using the bloom filter collection. Input the path of the collection object. also input the textfile path
def Search(pattern,collection,textfile) :


	if 'Collections' not in os.listdir('.') :
		print("Collection is not created\n")
	else :
		col = load_object(collection)
		if col.segment_size != len(pattern) :
			print("Cannot search for this pattern ")
		else :
			text = open(textfile).read()
			print("Loaded object\nNow searching for pattern\n")
			print("The length of the text is {}.\nThe length of the pattern is {}.".format(len(text),len(pattern)))
			count = parallel_search_naive(col,pattern,text)
			print("The pattern appears {} times\n".format(count))

