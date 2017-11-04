require "account_profiler/parser/digital_data_size"

describe AccountProfiler::Parser::DigitalDataSize do
    context "When creating DigitalDataSize" do
        it "Should reponse in bytes must be 2 when value is '2 B'" do
            digital_data = AccountProfiler::Parser::DigitalDataSize.from_string( "2 B" )
            response = digital_data.length_in_bytes()
            expect( response ).to eq 2
        end

        it "Should reponse in bytes must be 2.5 when value is '2,5 B'" do
            digital_data = AccountProfiler::Parser::DigitalDataSize.from_string( "2,5 B" )
            response = digital_data.length_in_bytes()
            expect( response ).to eq 2.5
        end

        it "Should reponse in bytes must be 2048 when value is '2 KB'" do
            digital_data = AccountProfiler::Parser::DigitalDataSize.from_string( "2 KB" )
            response = digital_data.length_in_bytes()
            expect( response ).to eq 2048
        end

        it "Should reponse in bytes must be 2560 when value is '2,5 KB'" do
            digital_data = AccountProfiler::Parser::DigitalDataSize.from_string( "2,50 KB" )
            response = digital_data.length_in_bytes()
            expect( response ).to eq 2560
        end

        it "Should reponse in bytes must be 2508.8 when value is '2,45 KB'" do
            digital_data = AccountProfiler::Parser::DigitalDataSize.from_string( "2,45 KB" )
            response = digital_data.length_in_bytes()
            expect( response ).to eq 2508.8
        end

        it "Should reponse in bytes must be 2097152 when value is '2 MB'" do
            digital_data = AccountProfiler::Parser::DigitalDataSize.from_string( "2 MB" )
            response = digital_data.length_in_bytes()
            expect( response ).to eq 2097152
        end

        it "Should reponse in bytes must be 2621440 when value is '2,5 MB'" do
            digital_data = AccountProfiler::Parser::DigitalDataSize.from_string( "2,5 MB" )
            response = digital_data.length_in_bytes()
            expect( response ).to eq 2621440
        end

        it "Should raise ArgumentError if is in invalid format'" do
            expect{
                AccountProfiler::Parser::DigitalDataSize.from_string( "2.5 BB" )
            }.to raise_error( ArgumentError )
        end
    end
end
