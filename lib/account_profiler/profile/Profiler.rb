require_relative "AccountUsageProfile"

module AccountProfiler
    module Profile
        class Profiler
            def initialize()
                @usage_profile_map = {}
            end

            def insert( phone_number, account_usage_profile )
                profiles = @usage_profile_map[ phone_number ]

                if profiles == nil
                    profiles = []
                    @usage_profile_map[ phone_number ] = profiles
                end

                profiles << account_usage_profile
                @usage_profile_map[ phone_number ] = profiles
            end

            def resume( phone_number )
                profiles = @usage_profile_map[ phone_number ]

                if profiles == nil
                    raise ArgumentError,
                        "Not exist account profile for phone_number[#{phone_number}]"
                end

                resumed_profile = AccountProfiler::Profile::AccountUsageProfile.new()
                profiles.each do |profile|
                    resumed_profile << profile
                end

                return resumed_profile
            end
        end
    end
end
