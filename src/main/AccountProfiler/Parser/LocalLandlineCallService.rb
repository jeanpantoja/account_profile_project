require "AccountProfiler/Parser/CallService"

module AccountProfiler
    module Parser
        class LocalLandlineCallService < CallService
            def service?( account_line )
                super( account_line ) &&
                    is_local?( account_line ) &&
                    is_destiny_landline?( account_line )
            end
        end
    end
end
