require "AccountProfiler/Parser/Service"
require "AccountProfiler/Parser/DigitalDataSize"

module AccountProfiler
    module Parser
        class InternetService < Service
            def initialize()
                super(
                    /(TIM\s+\w+\s+Fast)|(BlackBerry\s+Professional\s+-\s+MB)/i
                )
            end

            def get_usage_profile( account_line )
                digital_data = AccountProfiler::Parser::DigitalDataSize.from_string(
                    account_line.duration()
                )

                usage = AccountProfiler::Profile::AccountUsageProfile.new()
                usage.internet_usage = digital_data.length_in_bytes()
                return usage
            end
        end
    end
end
