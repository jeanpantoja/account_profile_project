require_relative "service"
require_relative "../profile/account_usage_profile"

module AccountProfiler
  module Parser
    class SMSService < Service
      @@USAGE_BY_SMS = 1

      def initialize()
        super( /TIM\s+Torpedo/i )
      end

      def get_usage_profile( account_line )
        usage = AccountProfiler::Profile::AccountUsageProfile.new()
        usage.sms_usage = @@USAGE_BY_SMS
        usage
      end
    end
  end
end

