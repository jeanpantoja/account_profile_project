require "AccountProfiler/Parser/Service"
require "AccountProfiler/Parser/CallDuration"

module AccountProfiler
    module Parser
        class CallService < Service
            @@CALL_REGEX = /Chamadas\s+(Locais|Longa)/i
            @@LOCAL_CALL_REGEX =/Chamadas\s+Locais/i
            @@LONG_DISTANCE_REGEX = /Chamadas\s+Longa\s+Dist/i
            @@MOBILE_CALL_REGEX = /celulares|movel/i
            @@LANDLINE_CALL_REGEX = /fixo/i

            def initialize()
                super( @@CALL_REGEX )
            end

            def is_destiny_mobile?( account_line )
                account_line.match_destiny?( @@MOBILE_CALL_REGEX ) ||
                    account_line.match_service_description?( @@MOBILE_CALL_REGEX )
            end

            def is_destiny_landline?( account_line )
                account_line.match_destiny?( @@LANDLINE_CALL_REGEX ) ||
                    account_line.match_service_description?( @@LANDLINE_CALL_REGEX )
            end

            def is_local?( account_line )
                account_line.match_service_description?( @@LOCAL_CALL_REGEX )
            end

            def is_long_distance?( account_line )
                account_line.match_service_description?( @@LONG_DISTANCE_REGEX )
            end

            def get_duration( account_line )
                return AccountProfiler::Parser::CallDuration.from_string(
                    account_line.duration()
                )
            end
        end
    end
end
