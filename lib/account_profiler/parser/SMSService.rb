require_relative "Service"
require_relative "../profile/AccountUsageProfile"

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
                return usage
            end
        end
    end
end
