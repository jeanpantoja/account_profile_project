# -*- coding: utf-8 -*-

import account_profile.parser as parser

BILL_LINES_OF_LONG_DISTANCE_CALL = [
    parser.BillLine(
        "111-1111-1111",
        "Chamadas Longa Distância: Telefônica",
        "SP AREA 14",
        "01m06s"
    ),
    parser.BillLine(
        "111-1111-1111",
        "Chamadas Longa Distância: Brasil Telecom",
        "SC FIXO - AREA 48",
        "01m06s"
    ),
    parser.BillLine(
        "111-1111-1111",
        "Chamadas Longa Distância: Embratel",
        "RJ FIXO - AREA 21",
        "01m06s"
    ),
    parser.BillLine(
        "111-1111-1111",
        "Chamadas Longa Distância: TIM LD 41",
        "SC FIXO - AREA 48",
        "01m06s"
    ),
    parser.BillLine(
        "111-1111-1111",
        "Chamadas Longa Distância: Telemar",
        "SP FIXO - AREA 15",
        "01m06s"
    )
]

BILL_LINES_OF_LOCAL_CALL = [
    parser.BillLine(
        "111-1111-1111",
        "Chamadas Locais para Outros Telefones Fixos",
        "SC FIXO - AREA 48",
        "01m06s"
    ),
    parser.BillLine(
        "111-1111-1111",
        "Chamadas Locais para Outros Celulares",
        "SP MOVEL - AREA 11",
        "01m06s"
    ),
    parser.BillLine(
        "111-1111-1111",
        "Chamadas Locais para Celulares TIM",
        "SC MOVEL TIM - AREA 48",
        "01m06s"
    ),
    parser.BillLine(
        "111-1111-1111",
        "Chamadas Locais para Telefones Fixos",
        "SC FIXO - AREA 48",
        "01m06s"
    )
]


BILL_LINES_OF_CALL_TO_MOBILE_PHONE = [
    parser.BillLine(
        "111-1111-1111",
        "Chamadas Locais para Celulares TIM",
        "SC MOVEL TIM - AREA 48",
        "01m06s"
    ),
    parser.BillLine(
        "111-1111-1111",
        "Chamadas Locais para Outros Celulares",
        "SC MOVEL - AREA 48",
        "01m06s"
    ),
    parser.BillLine(
        "111-1111-1111",
        "Chamadas Longa Distância: TIM LD 41",
        "SC MOVEL TIM - AREA 48",
        "01m06s"
    ),
    parser.BillLine(
        "111-1111-1111",
        "Chamadas Locais para Celulares TIM",
        "SC TIM AREA 48",
        "01m06s"
    )
]

BILL_LINES_OF_CALL_TO_LANDLINE_PHONE = [
    parser.BillLine(
        "111-1111-1111",
        "Chamadas Longa Distância: Embratel",
        "RJ FIXO - AREA 21",
        "01m06s"
    ),
    parser.BillLine(
        "111-1111-1111",
        "Chamadas Locais para Outros Telefones Fixos",
        "SC FIXO - AREA 48",
        "01m06s"
    ),
    parser.BillLine(
        "111-1111-1111",
        "Chamadas Locais para Telefones Fixos",
        "HORA CERTA",
        "01m06s"
    ),
    parser.BillLine(
        "111-1111-1111",
        "Chamadas Longa Distância: Telemar",
        "RS FIXO - AREA 51",
        "01m06s"
    ),
    parser.BillLine(
        "111-1111-1111",
        "Chamadas Longa Distância: TIM LD 41",
        "SP FIXO - AREA 11",
        "01m06s"
    ),
    parser.BillLine(
        "111-1111-1111",
        "Chamadas Longa Distância: Brasil Telecom",
        "SC FIXO - AREA 48",
        "01m06s"
    )
]

BILL_LINES_01 = [
    #local mobile calls( 2.20 min)
    parser.BillLine(
        "111-1111-1111",
        "Chamadas Locais para Celulares TIM",
        "SC TIM AREA 48",
        "01m06s"
    ),
    parser.BillLine(
        "111-1111-1111",
        "Chamadas Locais para Outros Celulares",
        "SC MOVEL - AREA 48",
        "01m06s"
    ),
    #local landline calls( 1.10 min )
    parser.BillLine(
        "111-1111-1111",
        "Chamadas Locais para Outros Telefones Fixos",
        "SC FIXO - AREA 48",
        "01m06s"
    ),
    #long distance mobile calls( 2.9166666666666665 min )
    parser.BillLine(
        "111-1111-1111",
        "Chamadas Longa Distância: TIM LD 41",
        "SC MOVEL TIM - AREA 48",
        "01m30s"
    ),
    parser.BillLine(
        "111-1111-1111",
        "Chamadas Longa Distância: Brasil Telecom",
        "SC MOVEL - AREA 48",
        "01m25s"
    ),
    #long distance landline calls( 1.8333333333333333 min )
    parser.BillLine(
        "111-1111-1111",
        "Chamadas Longa Distância: Telemar",
        "SP FIXO - AREA 15",
        "01m05s"
    ),
    parser.BillLine(
        "111-1111-1111",
        "Chamadas Longa Distância: Brasil Telecom",
        "SP FIXO - AREA 15",
        "00m45s"
    ),
    #sms( 2 und )
    parser.BillLine(
        "111-1111-1111",
        "TIM Torpedo",
        "SC FIXO - AREA 48",
        ""
    ),
    parser.BillLine(
        "111-1111-1111",
        "TIM Torpedo",
        "SC FIXO - AREA 48",
        ""
    ),
    #internet( 2073640.47712 B)
    parser.BillLine(
        "111-1111-1111",
        "TIM Wap Fast",
        "-",
        "18,67969 KB"
    ),
    parser.BillLine(
        "111-1111-1111",
        "TIM Connect Fast",
        "-",
        "1,95332 MB"
    ),
    parser.BillLine(
        "111-1111-1111",
        "BlackBerry Professional - MB",
        "-",
        "5,64551 KB"
    ),
    parser.BillLine(
        "111-1111-1111",
        "BlackBerry Professional - MB",
        "-",
        "527 B"
    )
]
