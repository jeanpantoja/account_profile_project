require "AccountProfiler/Parser/CallService"

module AccountProfiler
    module Parser
        class LongDistanceMobileCallService < CallService
            def service?( account_line )
                super( account_line ) &&
                    is_long_distance?( account_line ) &&
                    is_destiny_mobile?( account_line )
            end
        end
    end
end
