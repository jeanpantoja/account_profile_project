module AccountProfiler
    module Parser
        class Service
            def initialize( type_regex )
                @type_regex = type_regex
            end

            def service?( account_line )
                account_line.match_service_description?( @type_regex )
            end
        end
    end
end
