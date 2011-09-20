
#ifndef BLOOM_FILTER_H
#define BLOOM_FILTER_H

#include <bitset>
#include <string>
//Define of BitVector and M
#define LEN 1<<26
#define M 5
typedef ::std::bitset<LEN> BV;

class BloomFilter
{
public:

	BloomFilter();

	BloomFilter(const char* in_path);

	~BloomFilter();
	
	//Seralize bitset to file
	void Dump(const char* out_path);
	
	//Add to Bloom Filter and set M bit to True
	void Add(const ::std::string key);
	
	//if all of the M bit was set to True -> return True;if any of the M bit was set to False -> Return False
	bool Test(const ::std::string key);

	//Test first, add it if not in and return false, else return false
	bool TestAndAdd(const ::std::string key);
private:
	BV* pbv;
};

#endif
