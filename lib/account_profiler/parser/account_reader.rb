require "csv"
require "json"

require_relative "account_line"
require_relative "long_distance_mobile_call_service"
require_relative "long_distance_landline_call_service"
require_relative "local_mobile_call_service"
require_relative "local_landline_call_service"
require_relative "sms_service"
require_relative "internet_service"

require_relative "../profile/profiler"

module AccountProfiler
    module Parser
        class AccountReader
            @@CSV_COLUMN_SEPARATOR = ";"

            def initialize()
                @service_types = [
                    AccountProfiler::Parser::InternetService.new(),
                    AccountProfiler::Parser::SMSService.new(),
                    AccountProfiler::Parser::LocalMobileCallService.new(),
                    AccountProfiler::Parser::LocalLandlineCallService.new(),
                    AccountProfiler::Parser::LongDistanceMobileCallService.new(),
                    AccountProfiler::Parser::LongDistanceLandlineCallService.new(),
                ]
            end

            def self.build_profiler_from_csv( csv_file_path )
                reader = AccountProfiler::Parser::AccountReader.new()
                csv_lines = CSV.foreach(
                    csv_file_path, col_sep: @@CSV_COLUMN_SEPARATOR
                )

                profiler = reader.build_profiler( csv_lines )
                return profiler
            end

            def build_profiler( data_lines )
                profiler = AccountProfiler::Profile::Profiler.new()

                data_lines.each do |line_data|
                    acc_line = AccountProfiler::Parser::AccountLine.from_array( line_data )

                    @service_types.each do |service|
                        if service.service?( acc_line )
                            usage_profile = service.get_usage_profile( acc_line )
                            profiler.insert( acc_line.phone_number, usage_profile)
                            break
                        end
                    end
                end

                return profiler
            end
        end
    end
end
