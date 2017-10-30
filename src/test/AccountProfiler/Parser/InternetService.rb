require "AccountProfiler/Parser/InternetService"

describe AccountProfiler::Parser::InternetService do
    context "When detecting internet service using service description" do
        it "Should reponse true when service_description is" do
            service = AccountProfiler::Parser::InternetService.new()
            service_description = "TIM Connect Fast"
            response = service.service?( service_description )
            expect( response ).to eq true
        end

        it "Should reponse true when service_description is" do
            service = AccountProfiler::Parser::InternetService.new()
            service_description = "TIM Wap Fast"
            response = service.service?( service_description )
            expect( response ).to eq true
        end

        it "Should reponse true when service_description is" do
            service = AccountProfiler::Parser::InternetService.new()
            service_description = "BlackBerry Professional - MB"
            response = service.service?( service_description )
            expect( response ).to eq true
        end
    end
end
