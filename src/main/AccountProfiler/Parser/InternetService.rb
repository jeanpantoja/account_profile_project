require "AccountProfiler/Parser/Service"

module AccountProfiler
    module Parser
        class InternetService < Service
            def initialize()
                super(
                    /(TIM\s+\w+\s+Fast)|(BlackBerry\s+Professional\s+-\s+MB)/i
                )
            end
        end
    end
end
