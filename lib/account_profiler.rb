require_relative "account_profiler/parser/AccountReader"

module AccountProfiler
    def AccountProfiler.create_profiler( csv_file_path )
        return AccountProfiler::Parser::AccountReader.build_profiler_from_csv(
            csv_file_path
        )
    end
end
