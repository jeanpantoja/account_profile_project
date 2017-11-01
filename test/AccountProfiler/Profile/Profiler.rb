require "AccountProfiler/Profile/AccountUsageProfile"
require "AccountProfiler/Profile/CallUsageProfile"
require "AccountProfiler/Profile/Profiler"

describe AccountProfiler::Profile::Profiler do
    context "When testing Profiler resume" do
        it "Inserting twice the same AccountUsageProfile for same user, the resume call must
            result double of inserted AccountUsageProfile" do

            profiler = AccountProfiler::Profile::Profiler.new()
            phone_number = "111-11111-1111"
            2.times do
                call = AccountProfiler::Profile::CallUsageProfile.new(
                    1, 2, 3, 4
                )

                profile =  AccountProfiler::Profile::AccountUsageProfile.new(
                    1, 2, call
                )

                profiler.insert( phone_number, profile )
            end

            resumed_profile = profiler.resume( phone_number )
            call = resumed_profile.call_usage_profile

            expect( resumed_profile.sms_usage ).to eq 2
            expect( resumed_profile.internet_usage ).to eq 4
            expect( call.local_mobile ).to eq 2
            expect( call.local_landline ).to eq 4
            expect( call.long_distance_mobile ).to eq 6
            expect( call.long_distance_landline ).to eq 8
        end

        it "Call to resume with a non existent phone_number must raise ArgumentError" do

            profiler = AccountProfiler::Profile::Profiler.new()
            phone_number = "111-11111-1111"

            expect{
                profiler.resume( phone_number )
            }.to raise_error( ArgumentError )
        end
    end
end
