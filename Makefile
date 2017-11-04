PROGRAM_NAME=account_profiler

build: clean
	gem build $(PROGRAM_NAME).gemspec

install:
	gem install $(PROGRAM_NAME)-*.gem

uninstall:
	gem uninstall $(PROGRAM_NAME)

test:
	rspec -I ./lib

clean:
	rm -fv $(PROGRAM_NAME)-*.gem
