require "AccountProfiler/Parser/SMSService"

describe AccountProfiler::Parser::SMSService do
    context "When detecting SMS service using service description" do
        it "Should reponse true when service_description is" do
            service = AccountProfiler::Parser::SMSService.new()
            service_description = "TIM torpedo"
            response = service.service?( service_description )
            expect( response ).to eq true
        end

        it "Should reponse true when service_description is" do
            service = AccountProfiler::Parser::SMSService.new()
            service_description = "  TIM    torpedo  "
            response = service.service?( service_description )
            expect( response ).to eq true
        end

        it "Should reponse true when service_description is" do
            service = AccountProfiler::Parser::SMSService.new()
            service_description = "tim torpedo"
            response = service.service?( service_description )
            expect( response ).to eq true
        end
    end
end
