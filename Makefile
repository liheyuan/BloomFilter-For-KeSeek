#Compiler and flags
CC = g++
LD = g++
CXXFLAGS := -O3 
LINKFLAGS :=  
#Objects
OBJS := $(patsubst %.cpp, %.o, $(wildcard *.cpp))

#Generate binary name
PROG = TestBloomFilter

#Main target
all: $(PROG)
 
$(PROG): $(OBJS)
	$(LD) $(OBJS) $(LINKFLAGS) -o $(PROG)
 
%.o:%.cpp
	$(CC) $(CXXFLAGS) -c -o $@ $<
 
clean:
	rm -rf $(OBJS) $(OJBS:.o=.d) $(PROG)
