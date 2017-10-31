require "AccountProfiler/Profile/CallUsageProfile"

describe AccountProfiler::Profile::CallUsageProfile do
    context "When testing CallUsageProfile addition" do
        it "A call usage profile plus yourself must result in double of all values" do
            call = AccountProfiler::Profile::CallUsageProfile.new(
                1, 2, 3, 4
            )

            call_result = call + call

            expect( call_result.local_mobile ).to eq 2
            expect( call_result.local_landline ).to eq 4
            expect( call_result.long_distance_mobile ).to eq 6
            expect( call_result.long_distance_landline ).to eq 8
        end
    end
end
