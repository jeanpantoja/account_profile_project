require_relative "CallUsageProfile"

module AccountProfiler
    module Profile
        class AccountUsageProfile
            def initialize(
                sms_usage = 0,
                internet_usage = 0,
                call_usage_profile = CallUsageProfile.new() )
                @sms_usage = sms_usage
                @internet_usage  = internet_usage
                @call_usage_profile = call_usage_profile
            end

            def sms_usage()
                @sms_usage
            end

            def internet_usage()
                @internet_usage
            end

            def call_usage_profile()
                @call_usage_profile
            end

            def sms_usage=( value )
                @sms_usage = value
            end

            def internet_usage=( value )
                @internet_usage = value
            end

            def call_usage_profile=( value )
                @call_usage_profile = value
            end

            def long_distance_mobile_call_usage=( value )
                @call_usage_profile.long_distance_mobile = value
            end

            def long_distance_landline_call_usage=( value )
                @call_usage_profile.long_distance_landline = value
            end

            def local_mobile_call_usage=( value )
                @call_usage_profile.local_mobile = value
            end

            def local_landline_call_usage=( value )
                @call_usage_profile.local_landline = value
            end

            def long_distance_mobile_call_usage()
                @call_usage_profile.long_distance_mobile
            end

            def long_distance_landline_call_usage()
                @call_usage_profile.long_distance_landline
            end

            def local_mobile_call_usage()
                @call_usage_profile.local_mobile
            end

            def local_landline_call_usage()
                @call_usage_profile.local_landline
            end

            def << ( other )
                @sms_usage += other.sms_usage
                @internet_usage += other.internet_usage
                @call_usage_profile << other.call_usage_profile
                return self
            end
        end
    end
end
