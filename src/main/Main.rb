$LOAD_PATH << '.'

require "AccountProfiler/Cli"

program = AccountProfiler::Cli::Program.new()
program.run()
