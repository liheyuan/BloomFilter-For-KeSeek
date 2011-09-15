#Compiler and flags
CC = g++
LD = g++
CXXFLAGS := -O3 -fPIC -I/usr/include/python2.6
LINKFLAGS := -fPIC -shared
#Objects
WRAPPER = bloomfilter_wrap.o
OBJS := $(patsubst %.cpp, %.o, $(wildcard ../*.cpp) $(WRAPPER))

#Generate binary name
SO = _bloomfilter.so

#Main target
all: $(SO)
 
$(SO): $(OBJS)
	$(LD) $(OBJS) $(LINKFLAGS) -o $(SO)
 
%.o:%.cpp
	$(CC) $(CXXFLAGS) -c -o $@ $<
 
%.o:%.cxx
	$(CC) $(CXXFLAGS) -c -o $@ $<

clean:
	rm -rf $(OBJS) $(OJBS:.o=.d) $(SO)
