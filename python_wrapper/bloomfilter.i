/* bloomfilter.i */
%module bloomfilter
%{
/* Reference included */
#include "../MurmurHash3.h"
#include "../BloomFilter.h"
%}

/* Suppourt STL */
%include stl.i

/* Wrapper and generate code */
%include "../MurmurHash3.h"
%include "../BloomFilter.h"
