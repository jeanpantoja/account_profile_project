require_relative "CallService"
require_relative "../profile/AccountUsageProfile"

module AccountProfiler
    module Parser
        class LocalLandlineCallService < CallService
            def service?( account_line )
                super( account_line ) &&
                    is_local?( account_line ) &&
                    is_destiny_landline?( account_line )
            end

            def get_usage_profile( account_line )
                duration = get_duration( account_line )
                usage = AccountProfiler::Profile::AccountUsageProfile.new()
                usage.local_landline_call_usage = duration.minutes()
                return usage
            end
        end
    end
end
