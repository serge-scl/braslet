EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L MCU_ST_STM32F4:STM32F401CCFx U1
U 1 1 610064C6
P 5775 3675
F 0 "U1" H 5775 5456 50  0000 C CNN
F 1 "STM32F401CCFx" H 5775 5365 50  0000 C CNN
F 2 "Package_CSP:ST_WLCSP-49_Die423" H 5275 2075 50  0001 R CNN
F 3 "http://www.st.com/st-web-ui/static/active/en/resource/technical/document/datasheet/DM00086815.pdf" H 5775 3675 50  0001 C CNN
	1    5775 3675
	1    0    0    -1  
$EndComp
$Comp
L Regulator_Linear:AMS1117-3.3 U2
U 1 1 61014B87
P 4175 1950
F 0 "U2" H 4175 2192 50  0000 C CNN
F 1 "AMS1117-3.3" H 4175 2101 50  0000 C CNN
F 2 "Package_TO_SOT_SMD:SOT-223-3_TabPin2" H 4175 2150 50  0001 C CNN
F 3 "http://www.advanced-monolithic.com/pdf/ds1117.pdf" H 4275 1700 50  0001 C CNN
	1    4175 1950
	1    0    0    -1  
$EndComp
$Comp
L Connector:USB_B_Micro J1
U 1 1 6101668A
P 2750 1975
F 0 "J1" H 2807 2442 50  0000 C CNN
F 1 "USB_B_Micro" H 2807 2351 50  0000 C CNN
F 2 "Connector_USB:USB_Micro-B_Wuerth_614105150721_Vertical" H 2900 1925 50  0001 C CNN
F 3 "~" H 2900 1925 50  0001 C CNN
	1    2750 1975
	1    0    0    -1  
$EndComp
$Comp
L TMAG5273Hall:tmag5273 U3
U 1 1 610194D7
P 3250 6075
F 0 "U3" H 3200 6550 50  0000 C CNN
F 1 "tmag5273" H 3200 6459 50  0000 C CNN
F 2 "Package_TO_SOT_SMD:SOT-23-6" H 3250 6075 50  0001 C CNN
F 3 "" H 3250 6075 50  0001 C CNN
	1    3250 6075
	1    0    0    -1  
$EndComp
$Comp
L Transistor_FET:BF545C Q1
U 1 1 61032CC8
P 3750 3050
F 0 "Q1" H 3940 3096 50  0000 L CNN
F 1 "BF545C" H 3940 3005 50  0000 L CNN
F 2 "Package_TO_SOT_SMD:SOT-23" H 3950 2975 50  0001 L CIN
F 3 "https://www.nxp.com/docs/en/data-sheet/BF545A_BF545B_BF545C.pdf" H 3750 3050 50  0001 L CNN
	1    3750 3050
	1    0    0    -1  
$EndComp
$Comp
L dk_LED-Indication-Discrete:LH_R974-LP-1 D1
U 1 1 6103E8C0
P 7800 3275
F 0 "D1" H 7750 3612 60  0000 C CNN
F 1 "LH_R974-LP-1" H 7750 3506 60  0000 C CNN
F 2 "LED_SMD:LED_0805_2012Metric" H 8000 3475 60  0001 L CNN
F 3 "https://dammedia.osram.info/media/resource/hires/osram-dam-2493888/LH%20R974.pdf" H 8000 3575 60  0001 L CNN
F 4 "475-1415-1-ND" H 8000 3675 60  0001 L CNN "Digi-Key_PN"
F 5 "LH R974-LP-1" H 8000 3775 60  0001 L CNN "MPN"
F 6 "Optoelectronics" H 8000 3875 60  0001 L CNN "Category"
F 7 "LED Indication - Discrete" H 8000 3975 60  0001 L CNN "Family"
F 8 "https://dammedia.osram.info/media/resource/hires/osram-dam-2493888/LH%20R974.pdf" H 8000 4075 60  0001 L CNN "DK_Datasheet_Link"
F 9 "/product-detail/en/osram-opto-semiconductors-inc/LH-R974-LP-1/475-1415-1-ND/1802604" H 8000 4175 60  0001 L CNN "DK_Detail_Page"
F 10 "LED RED DIFFUSED 0805 SMD" H 8000 4275 60  0001 L CNN "Description"
F 11 "OSRAM Opto Semiconductors Inc." H 8000 4375 60  0001 L CNN "Manufacturer"
F 12 "Active" H 8000 4475 60  0001 L CNN "Status"
	1    7800 3275
	1    0    0    -1  
$EndComp
$Comp
L dk_LED-Indication-Discrete:LG_R971-KN-1 D2
U 1 1 61040C00
P 7775 3850
F 0 "D2" H 7725 4187 60  0000 C CNN
F 1 "LG_R971-KN-1" H 7725 4081 60  0000 C CNN
F 2 "LED_SMD:LED_0805_2012Metric" H 7975 4050 60  0001 L CNN
F 3 "https://dammedia.osram.info/media/resource/hires/osram-dam-2493936/LG%20R971.pdf" H 7975 4150 60  0001 L CNN
F 4 "475-1410-1-ND" H 7975 4250 60  0001 L CNN "Digi-Key_PN"
F 5 "LG R971-KN-1" H 7975 4350 60  0001 L CNN "MPN"
F 6 "Optoelectronics" H 7975 4450 60  0001 L CNN "Category"
F 7 "LED Indication - Discrete" H 7975 4550 60  0001 L CNN "Family"
F 8 "https://dammedia.osram.info/media/resource/hires/osram-dam-2493936/LG%20R971.pdf" H 7975 4650 60  0001 L CNN "DK_Datasheet_Link"
F 9 "/product-detail/en/osram-opto-semiconductors-inc/LG-R971-KN-1/475-1410-1-ND/1802598" H 7975 4750 60  0001 L CNN "DK_Detail_Page"
F 10 "LED GREEN DIFFUSED 0805 SMD" H 7975 4850 60  0001 L CNN "Description"
F 11 "OSRAM Opto Semiconductors Inc." H 7975 4950 60  0001 L CNN "Manufacturer"
F 12 "Active" H 7975 5050 60  0001 L CNN "Status"
	1    7775 3850
	1    0    0    -1  
$EndComp
$EndSCHEMATC
