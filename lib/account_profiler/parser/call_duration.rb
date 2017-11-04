module AccountProfiler
    module Parser
        class CallDuration
            @@DURATION_REGEX = /(\d+)m(\d+)s/

            def initialize( minutes, seconds )
                @minutes = minutes
                @seconds = seconds
            end

            def self.from_string( duration_text )
                matched = @@DURATION_REGEX.match( duration_text )

                if matched == nil
                    raise ArgumentError,
                        "The duration is not in the correct format[ '%dm%ds' ]"
                end

                minutes = matched[ 1 ].to_i()
                seconds = matched[ 2 ].to_i()

                CallDuration.new( minutes, seconds )
            end

            def minutes()
                ( @minutes + ( @seconds / 60.0 ) )
            end
        end
    end
end
