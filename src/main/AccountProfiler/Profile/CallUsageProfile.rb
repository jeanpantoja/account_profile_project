module AccountProfiler
    module Profile
        class CallUsageProfile
            def initialize()
                @long_distance_mobile = 0
                @long_distance_landline = 0
                @local_mobile = 0
                @local_landline = 0
            end

            def long_distance_mobile()
                @long_distance_mobile
            end

            def long_distance_landline()
                @long_distance_landline
            end

            def local_mobile()
                @local_mobile
            end

            def local_landline()
                @local_landline
            end

            def long_distance_mobile=( value )
                @long_distance_mobile = value
            end

            def long_distance_landline=( value )
                @long_distance_landline = value
            end

            def local_mobile=( value )
                @local_mobile = value
            end

            def local_landline=( value )
                @local_landline = value
            end

            def + ( other )
                call = CallUsageProfile.new()
                call << other
                call << self
                return call
            end

            def << ( other )
                @local_mobile += other.local_mobile
                @local_landline += other.local_landline
                @long_distance_mobile += other.long_distance_mobile
                @long_distance_landline += other.long_distance_landline
                return self
            end
        end
    end
end
