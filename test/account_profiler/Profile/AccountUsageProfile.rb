require "account_profiler/Profile/AccountUsageProfile"
require "account_profiler/Profile/CallUsageProfile"

describe AccountProfiler::Profile::AccountUsageProfile do
    context "When testing AccountUsageProfile addition" do
        it "An account profile add to yourself must result in double
            of all values" do

            call = AccountProfiler::Profile::CallUsageProfile.new(
                1, 2, 3, 4
            )

            account_profile = AccountProfiler::Profile::AccountUsageProfile.new(
                1, 2, call
            )

            other = AccountProfiler::Profile::AccountUsageProfile.new()

            other << account_profile;
            other << account_profile;

            call = other.call_usage_profile

            expect( other.sms_usage ).to eq 2
            expect( other.internet_usage ).to eq 4
            expect( call.local_mobile ).to eq 2
            expect( call.local_landline ).to eq 4
            expect( call.long_distance_mobile ).to eq 6
            expect( call.long_distance_landline ).to eq 8
        end
    end
end
