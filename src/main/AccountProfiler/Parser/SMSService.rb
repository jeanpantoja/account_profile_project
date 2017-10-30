require "AccountProfiler/Parser/Service"

module AccountProfiler
    module Parser
        class SMSService < Service
            def initialize()
                super( /TIM\s+Torpedo/i )
            end
        end
    end
end
