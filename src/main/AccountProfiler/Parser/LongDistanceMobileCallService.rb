require_relative "CallService"
require_relative "../Profile/AccountUsageProfile"

module AccountProfiler
    module Parser
        class LongDistanceMobileCallService < CallService
            def service?( account_line )
                super( account_line ) &&
                    is_long_distance?( account_line ) &&
                    is_destiny_mobile?( account_line )
            end

            def get_usage_profile( account_line )
                duration = get_duration( account_line )
                usage = AccountProfiler::Profile::AccountUsageProfile.new()
                usage.long_distance_mobile_call_usage = duration.minutes()
                return usage
            end
        end
    end
end
