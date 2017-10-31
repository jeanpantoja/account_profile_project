require "AccountProfiler/Profile/Call"

describe AccountProfiler::Profile::Call do
    context "When testing Call addition" do
        it "A call with all usage set as 1  plus yourself must result
            in a call profile with all usage equals 2" do
            call = AccountProfiler::Profile::Call.new()

            call.local_mobile = 1
            call.local_landline = 1
            call.long_distance_mobile = 1
            call.long_distance_landline = 1

            call_result = call + call

            expect( call_result.local_mobile ).to eq 2
            expect( call_result.local_landline ).to eq 2
            expect( call_result.long_distance_mobile ).to eq 2
            expect( call_result.long_distance_landline ).to eq 2
        end
    end
end
