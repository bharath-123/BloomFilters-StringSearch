# BloomFilters-StringSearch
Speeding up string search using bloom filters. 
I ll be writing a paper describing the algorithm used shortly.

Specs : In python3. Need multiprocessing to run the algorithms parallely.

Using this code : 
 
  
    Create_DNA_Collection(text,size,no_of_bloom_filters)
    
    This function will create bloom filter collection which will be used to 
    speed up string searching. It will create a bloom filter collection object.
    Returns nothing
   
    Parameters : 
      text - The large text file you want to search in 
      size - Size of the pattern you want to search(This algorithm is sensitive to
      size of pattern).Defaults to 60.
      no_of_bloom_filters - No of bloom filters in your collection.Defaults to 15.
  

  
  
    Search(pattern,collection,textfile)
    
    This function will search for the pattern in the textfile. Collection is the 
    path to the collection object in your system. It will return the number of 
    times the pattern occurs in the text.
    
    Parameters : 
      pattern - The pattern to search
      collection - Path of the bloom filter collection object
      textfile - The file associated with the bloom filter object.
  
  
  
Look at test.pdf to see the performance improvements.
Naive with BLF - Bloom filters used with naive string search algorithm. Done serially and parallely
Naive - Direct naive string search algorithm is used.
