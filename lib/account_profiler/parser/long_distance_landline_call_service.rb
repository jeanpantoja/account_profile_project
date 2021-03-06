require_relative "call_service"
require_relative "../profile/account_usage_profile"

module AccountProfiler
  module Parser
    class LongDistanceLandlineCallService  < CallService
      def service?( account_line )
        super( account_line ) &&
          is_long_distance?( account_line ) &&
          is_destiny_landline?( account_line )
      end

      def get_usage_profile( account_line )
        duration = get_duration( account_line )
        usage = AccountProfiler::Profile::AccountUsageProfile.new()
        usage.long_distance_landline_call_usage = duration.minutes()
        usage
      end
    end
  end
end

