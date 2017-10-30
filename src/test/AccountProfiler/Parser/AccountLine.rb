require "AccountProfiler/Parser/AccountLine"

describe AccountProfiler::Parser::AccountLine do
    context "When testing account line creation" do
        it "Should math field values when created from array" do
            phone_number = "000-00000-0000"
            service_description = "service description"
            duration = "a duration"
            destiny = "a destiny"
            array = [
                "", "", "", phone_number, "",
                "", service_description, "", "", "",
                duration, "", "", destiny, "",
                "", "", "", "", "",
                "", "", "", "", ""
            ]

            account_line = AccountProfiler::Parser::AccountLine.from_array(
                array
            )

            expect( account_line.phone_number ).to eq phone_number
            expect( account_line.service_description ).to eq service_description
            expect( account_line.duration ).to eq duration
            expect( account_line.destiny ).to eq destiny
        end
    end

    context "When testing account line service description" do
        it "Should reponse true when service_description match pattern" do
            account_line = AccountProfiler::Parser::AccountLine.new(
                "000-00000-0000",
                "TIM Torpedo",
                "",
                "SC FIXO - AREA 48"
            )
            pattern = /TIM Torpedo/i
            response = account_line.match_service_description?( pattern )
            expect( response ).to eq true
        end

        it "Should reponse true when service_description match pattern" do
            account_line = AccountProfiler::Parser::AccountLine.new(
                "000-00000-0000",
                "Tim Wap Fast",
                "",
                "SC FIXO - AREA 48"
            )
            pattern = /Tim\s+\w+\s+Fast/i
            response = account_line.match_service_description?( pattern )
            expect( response ).to eq true
        end
    end
end
