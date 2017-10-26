PROGRAM_NAME=profiler

all: make_package

make_package:
	rm -f ./$(PROGRAM_NAME)
	cd src && zip -r /tmp/profiler_tmp.zip *
	mv /tmp/profiler_tmp.zip ./$(PROGRAM_NAME)

test:
	cd src && python3 test.py

