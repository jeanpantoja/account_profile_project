require_relative "service"
require_relative "digital_data_size"

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
        usage
      end
    end
  end
end

