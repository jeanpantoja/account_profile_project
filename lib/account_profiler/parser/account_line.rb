module AccountProfiler
  module Parser
    class AccountLine
      @@PHONE_NUMBER_INDEX = 3
      @@SERVICE_DESCRIPTION_INDEX = 6
      @@DESTINY_INDEX = 10
      @@DURATION_INDEX = 13

      def initialize(
        phone_number,
        service_description,
        duration,
        destiny
      )
        @phone_number = phone_number
        @service_description = service_description
        @duration = duration
        @destiny = destiny
      end

      def self.from_array( line_data )
        phone_number = line_data[ @@PHONE_NUMBER_INDEX ]
        service_description = line_data[ @@SERVICE_DESCRIPTION_INDEX ]
        duration = line_data[ @@DURATION_INDEX ]
        destiny = line_data[ @@DESTINY_INDEX ]
        AccountLine.new( phone_number, service_description, duration, destiny )
      end

      def phone_number()
        @phone_number
      end

      def service_description()
        @service_description
      end

      def duration()
        @duration
      end

      def destiny()
        @destiny
      end

      def match_service_description?( regex )
        return ( regex =~ @service_description ) != nil
      end

      def match_destiny?( regex )
        return ( regex =~ @destiny ) != nil
      end
    end
  end
end

