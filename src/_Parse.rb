module AccountProfiler
    module Parser
        class Service

            def initialize( type_regex )
                @type_regex = type_regex
            end

            def service?( type_text )
                ( type_text =~ @type_regex ) != nil
            end
        end

        class SMSService < Service

            def initialize()
                super( /TIM\s+Torpedo/i )
            end

        end

        class InternetService < Service

            def initialize( service_type_regex )
                super( service_type_regex )
            end

        end

        class LocalMobileCallService < Service

            def initialize( service_type_regex )
                super( service_type_regex )
            end

        end

        class LocalLandarray_line_dataCallService < Service

            def initialize( service_type_regex )
                super( service_type_regex )
            end

        end

        class LongDistanceMobileCallService < Service

            def initialize( service_type_regex )
                super( service_type_regex )
            end

        end

        class LongDistanceLandarray_line_dataCallService < Service

            def initialize( service_type_regex )
                super( service_type_regex )
            end

        end

        class AccountLine

            @@PHONE_NUMBER_INDEX = 3
            @@SERVICE_TYPE_INDEX = 6
            @@DURATION_INDEX = 10
            @@DESTINY_INDEX = 13

            def initialize( phone_number,
                           service_type,
                           duration,
                           destiny )
                @phone_number = phone_number
                @service_type = service_type
                @duration = duration
                @destiny = destiny
            end

            def AccountLine.from_data( line_data )
                phone_number = line_data[ @@PHONE_NUMBER_INDEX ]
                service_type = line_data[ @@SERVICE_TYPE_INDEX ]
                duration = line_data[ @@DURATION_INDEX ]
                destiny = line_data[ @@DESTINY_INDEX ]
                AccountLine.new( phone_number, service_type, duration, destiny )
            end

            def service_type?( service )
                return service.service?( @service_type )
            end
        end
    end
end
