CC=gcc
CFLAGS=-Wall -pedantic -std=gnu99
LDFLAGS=-std=gnu99
EXECUTABLE=hellorpm

all: $(EXECUTABLE)

$(EXECUTABLE): hellorpm.o
	$(CC) -o $(EXECUTABLE) hellorpm.c $(LDFLAGS)

clean:
	rm *.o $(EXECUTABLE)

install:
	mkdir -p $(DESTDIR)
	install -m 0644 $(EXECUTABLE) $(DESTDIR)
