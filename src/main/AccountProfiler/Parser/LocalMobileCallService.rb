require "AccountProfiler/Parser/CallService"
require "AccountProfiler/Profile/AccountUsageProfile"

module AccountProfiler
    module Parser
        class LocalMobileCallService < CallService
            def service?( account_line )
                super( account_line ) &&
                    is_local?( account_line ) &&
                    is_destiny_mobile?( account_line )
            end

            def get_usage_profile( account_line )
                duration = get_duration( account_line )
                usage = AccountProfiler::Profile::AccountUsageProfile.new()
                usage.local_mobile_call_usage = duration.minutes()
                return usage
            end
        end
    end
end
