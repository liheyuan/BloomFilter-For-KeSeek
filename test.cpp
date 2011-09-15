#include "BloomFilter.h"
#include "MurmurHash3.h"
#include <iostream>
#include <fstream>
#include <sstream>
#include <bitset>
#include <stdlib.h>

using std::cout;
using std::endl;
using std::bitset;
using std::ifstream;
using std::ofstream;
using std::stringstream;
using std::string;
using std::ostringstream;



void test_init_dump()
{
	//Init 1
	/*
	BloomFilter bf;
	sleep(10);
	*/
	//Dump
	BloomFilter bf;
	bf.Dump("out.txt");
	sleep(10);
	//Init 2
}

void test_mmh3()
{
	string str = "liheyuan";
	uint32_t out;
	MurmurHash3_x86_32(str.c_str(),str.length(),0,&out);
	cout<<out<<endl;
}

void test_bloom_filter()
{
	string str = "Just an test";
	BloomFilter bf;
	cout<<bf.Test(str)<<endl;
	bf.Add(str);
	cout<<bf.Test(str)<<endl;
}

#define TEST_LEN1 10000000
#define TEST_LEN2 20000000

void test_bloom_filter_100w()
{
	ostringstream oss;
	//add 100w
	BloomFilter bf;
	for(size_t i=0; i<TEST_LEN1; i++)
	{
		oss.str("");
		oss << i;		
		bf.Add(oss.str());
	}

	//test false negitive
	size_t cnt = 0;
	for(size_t i=0; i<TEST_LEN1; i++)
	{
		oss.str("");
		oss << i;
		if(!bf.Test(oss.str()))
		{
			cnt++;
		}
	}
	cout<<"False Negitive "<<cnt<<" ."<<endl;

	//test false positive
	cnt = 0;
	for(size_t i=TEST_LEN1; i<TEST_LEN2; i++)
	{
		oss.str("");
		oss << i;
		if(bf.Test(oss.str()))
		{
			cnt++;
		}
	}
	cout<<"False Positive "<<cnt<<" ."<<endl;
}

void test_bloom_filter_dump_read()
{
	for(int i=0;i<5;i++){
	ostringstream oss;
	//add 100w
	BloomFilter* pbf = new BloomFilter();
	for(size_t i=0; i<100000; i++)
	{
		oss.str("");
		oss << i;		
		pbf->Add(oss.str());
	}
	pbf->Dump("out.txt");
	delete pbf;
	pbf = NULL;
	cout<<"Saved"<<endl;
	sleep(5);

	//test false negitive
	pbf = new BloomFilter("out.txt");
	size_t cnt = 0;
	for(size_t i=0; i<100000; i++)
	{
		oss.str("");
		oss << i;
		if(!pbf->Test(oss.str()))
		{
			cnt++;
		}
	}
	cout<<"False Negitive "<<cnt<<" ."<<endl;

	//test false positive
	cnt = 0;
	for(size_t i=100000; i<200000; i++)
	{
		oss.str("");
		oss << i;
		if(pbf->Test(oss.str()))
		{
			cnt++;
		}
	}
	cout<<"False Positive "<<cnt<<" ."<<endl;
	delete pbf;
	pbf = NULL;
	cout<<"Tested"<<endl;
	}
	sleep(20);
}

int main()
{
	cout<<"Test Start."<<endl;

	//test_init_dump();
	
	//test_mmh3();

	//test_bloom_filter();

	//test_bloom_filter_100w();

	test_bloom_filter_dump_read();

	cout<<"Test End."<<endl;
	return 0;
}
