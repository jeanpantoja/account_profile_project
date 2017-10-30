module AccountProfiler
    module Parser
        class Service
            def initialize( type_regex )
                @type_regex = type_regex
            end

            def service?( type_text )
                ( type_text =~ @type_regex ) != nil
            end
        end
    end
end
