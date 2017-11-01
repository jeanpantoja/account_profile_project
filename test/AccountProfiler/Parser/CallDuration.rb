require "AccountProfiler/Parser/CallDuration"

describe AccountProfiler::Parser::CallDuration do
    context "When creating CallDuration" do
        it "Should reponse in minutes be 2  when duration is 02ms00" do
            duration = AccountProfiler::Parser::CallDuration.from_string( "02m00s" )
            response = duration.minutes()
            expect( response ).to eq 2
        end

        it "Should reponse in minutes be 2.5  when duration is 02ms30" do
            duration = AccountProfiler::Parser::CallDuration.from_string( "02m30s" )
            response = duration.minutes()
            expect( response ).to eq 2.5
        end

        it "Should raise ArgumentError when duration is in wrong format" do
            expect {
                AccountProfiler::Parser::CallDuration.from_string( "02:30" )
            }.to raise_error( ArgumentError )
        end
    end
end
