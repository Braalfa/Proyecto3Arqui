TARGET  = fluidanimate
SRC     = serial.cpp 
CSRC    = $(SRC)
CXX = mipsel-linux-gnu-g++ -static

serial: $(CSRC)
	$(CXX) $(CXXFLAGS) $(CSRC) $(LDFLAGS) $(LIBS) -o $(TARGET)

cmp: cmp.cpp
	rm -rf cmp
	$(CXX) cmp.cpp -o cmp
clean:
	rm -rf $(TARGET) 
	rm -rf cmp
