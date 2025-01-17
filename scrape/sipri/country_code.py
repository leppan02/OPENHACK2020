def get_country(country_code): 
    mp = {
        "AFG": "Afghanistan",
        "AU": "African Union**",
        "ALB": "Albania",
        "ALG": "Algeria",
        "XLA": "Amal (Lebanon)*",
        "XSA": "ANC (South Africa)*",
        "ANG": "Angola",
        "XCC": "Anti-Castro rebels (Cuba)*",
        "ARG": "Argentina",
        "XGC": "Armas (Guatemala)*",
        "ARM": "Armenia",
        "ARU": "Aruba",
        "AUS": "Australia",
        "AST": "Austria",
        "AZB": "Azerbaijan",
        "BAS": "Bahamas",
        "BAH": "Bahrain",
        "BAN": "Bangladesh",
        "BAR": "Barbados",
        "BLR": "Belarus",
        "BEL": "Belgium",
        "BLZ": "Belize",
        "BEN": "Benin",
        "BHU": "Bhutan",
        "BIA": "Biafra",
        "BOL": "Bolivia",
        "BOS": "Bosnia-Herzegovina",
        "BOT": "Botswana",
        "BRA": "Brazil",
        "BRU": "Brunei",
        "BUL": "Bulgaria",
        "BF": "Burkina Faso",
        "BDI": "Burundi",
        "CAP": "Cabo Verde",
        "CMB": "Cambodia",
        "CAM": "Cameroon",
        "CAN": "Canada",
        "CAR": "Central African Republic",
        "CHA": "Chad",
        "CHE": "Chile",
        "CHI": "China",
        "COL": "Colombia",
        "COM": "Comoros",
        "CON": "Congo",
        "XNC": "Contras (Nicaragua)*",
        "COS": "Costa Rica",
        "IVO": "Cote d'Ivoire",
        "CRO": "Croatia",
        "CUB": "Cuba",
        "CYP": "Cyprus",
        "CZR": "Czechia",
        "CZE": "Czechoslovakia",
        "XSD": "Darfur rebels (Sudan)*",
        "DEN": "Denmark",
        "DJI": "Djibouti",
        "DOM": "Dominican Republic",
        "DRC": "DR Congo",
        "GDR": "East Germany (GDR)",
        "ECU": "Ecuador",
        "EGY": "Egypt",
        "XEE": "ELF (Ethiopia)*",
        "SAL": "El Salvador",
        "XEP": "EPLF (Ethiopia)*",
        "EQU": "Equatorial Guinea",
        "ERI": "Eritrea",
        "EST": "Estonia",
        "SWA": "Eswatini",
        "ETH": "Ethiopia",
        "EU": "European Union**",
        "EUR": "Europe multi-state",
        "XCF": "FAN (Chad)*",
        "FJI": "Fiji",
        "FIN": "Finland",
        "XSF": "FMLN (El Salvador)*",
        "XAF": "FNLA (Angola)*",
        "FRA": "France",
        "XPR": "FRELIMO (Portugal)*",
        "GAB": "Gabon",
        "GAM": "Gambia",
        "GEO": "Georgia",
        "FRG": "Germany",
        "GHA": "Ghana",
        "GRE": "Greece",
        "GND": "Grenada",
        "GUA": "Guatemala",
        "GUI": "Guinea",
        "GBI": "Guinea-Bissau",
        "XCG": "GUNT (Chad)*",
        "GUY": "Guyana",
        "HAI": "Haiti",
        "XHB": "Haiti rebels*",
        "XPA": "Hamas (Palestine)*",
        "XLH": "Hezbollah (Lebanon)*",
        "HON": "Honduras",
        "XYH": "Houthi rebels (Yemen)*",
        "HUN": "Hungary",
        "ICE": "Iceland",
        "IND": "India",
        "INS": "Indonesia",
        "XIR": "Indonesia rebels*",
        "IRA": "Iran",
        "IRQ": "Iraq",
        "IRE": "Ireland",
        "ISR": "Israel",
        "ITA": "Italy",
        "JAM": "Jamaica",
        "JAP": "Japan",
        "JOR": "Jordan",
        "KAT": "Katanga",
        "KAZ": "Kazakhstan",
        "KEN": "Kenya",
        "XCR": "Khmer Rouge (Cambodia)*",
        "KIR": "Kiribati",
        "KSV": "Kosovo",
        "KUW": "Kuwait",
        "KYR": "Kyrgyzstan",
        "LAO": "Laos",
        "LAT": "Latvia",
        "LEB": "Lebanon",
        "XLP": "Lebanon Palestinian rebels*",
        "LES": "Lesotho",
        "XLL": "LF (Lebanon)*",
        "LIB": "Liberia",
        "LYA": "Libya",
        "LYW": "Libya GNC",
        "LYE": "Libya HoR",
        "LIT": "Lithuania",
        "XUL": "LRA (Uganda)*",
        "XSL": "LTTE (Sri Lanka)*",
        "LUX": "Luxembourg",
        "MAC": "Macedonia",
        "MAD": "Madagascar",
        "MWI": "Malawi",
        "MAL": "Malaysia",
        "MLV": "Maldives",
        "MLI": "Mali",
        "MTA": "Malta",
        "MAR": "Marshall Islands",
        "MRA": "Mauritania",
        "MAU": "Mauritius",
        "MEX": "Mexico",
        "MIC": "Micronesia",
        "XPQ": "MNLF (Philippines)*",
        "MOL": "Moldova",
        "MON": "Mongolia",
        "MTG": "Montenegro",
        "MOR": "Morocco",
        "MOZ": "Mozambique",
        "XPM": "MPLA (Portugal)*",
        "XMX": "MTA (Myanmar)*",
        "XAM": "Mujahedin (Afghanistan)*",
        "MUL": "(multiple sellers)",
        "MYA": "Myanmar",
        "NAM": "Namibia",
        "NAT": "NATO**",
        "NEP": "Nepal",
        "NET": "Netherlands",
        "NZ": "New Zealand",
        "NIC": "Nicaragua",
        "NIR": "Niger",
        "NIG": "Nigeria",
        "XMN": "NLA (Macedonia)*",
        "XAN": "Northern Alliance (Afghanistan)*",
        "NCY": "Northern Cyprus",
        "KON": "North Korea",
        "YEN": "North Yemen",
        "NOR": "Norway",
        "XLB": "NTC (Libya)*",
        "OMA": "Oman",
        "OSC": "OSCE**",
        "XPP": "PAIGC (Portugal)*",
        "PAK": "Pakistan",
        "PAL": "Palau",
        "PA": "Palestine",
        "PAN": "Panama",
        "PAP": "Papua New Guinea",
        "PAR": "Paraguay",
        "XLO": "Pathet Lao (Laos)*",
        "PER": "Peru",
        "PHI": "Philippines",
        "XID": "PIJ (Israel/Palestine)*",
        "XTP": "PKK (Turkey)*",
        "XIP": "PLO (Israel)*",
        "POL": "Poland",
        "POR": "Portugal",
        "XPC": "PRC (Israel/Palestine)*",
        "XUI": "Provisional IRA (UK)*",
        "QAT": "Qatar",
        "RSS": "Regional Security System**",
        "ROM": "Romania",
        "XRR": "RPF (Rwanda)*",
        "XSR": "RUF (Sierra Leone)*",
        "RUS": "Russia",
        "RWA": "Rwanda",
        "SKN": "Saint Kitts and Nevis",
        "SVG": "Saint Vincent",
        "SAM": "Samoa",
        "SAU": "Saudi Arabia",
        "SEN": "Senegal",
        "SER": "Serbia",
        "SEY": "Seychelles",
        "SIE": "Sierra Leone",
        "SIN": "Singapore",
        "XLS": "SLA (Lebanon)*",
        "SLK": "Slovakia",
        "SLO": "Slovenia",
        "XSY": "SNA (Somalia)*",
        "SOL": "Solomon Islands",
        "SOM": "Somalia",
        "SA": "South Africa",
        "XYS": "Southern rebels (Yemen)*",
        "KOS": "South Korea",
        "SSD": "South Sudan",
        "VNS": "South Vietnam",
        "YES": "South Yemen",
        "USR": "Soviet Union",
        "SPA": "Spain",
        "XSP": "SPLA (Sudan)*",
        "SRI": "Sri Lanka",
        "SUD": "Sudan",
        "SUR": "Suriname",
        "SWE": "Sweden",
        "SWI": "Switzerland",
        "SYR": "Syria",
        "XSX": "Syria rebels*",
        "TAI": "Taiwan",
        "TAJ": "Tajikistan",
        "TAN": "Tanzania",
        "THA": "Thailand",
        "ET": "Timor-Leste",
        "TOG": "Togo",
        "TON": "Tonga",
        "TRI": "Trinidad and Tobago",
        "TUN": "Tunisia",
        "TUR": "Turkey",
        "TRK": "Turkmenistan",
        "TUV": "Tuvalu",
        "UAE": "UAE",
        "UGA": "Uganda",
        "XSI": "UIC (Somalia)*",
        "UKR": "Ukraine",
        "XUR": "Ukraine Rebels*",
        "XAU": "UNITA (Angola)*",
        "UK": "United Kingdom",
        "UNO": "United Nations**",
        "USA": "United States",
        "XMU": "United Wa State (Myanmar)*",
        "XXX": "Unknown country",
        "XXU": "Unknown rebel group*",
        "XXR": "Unknown recipient(s)",
        "XXS": "Unknown supplier(s)",
        "URU": "Uruguay",
        "UZB": "Uzbekistan",
        "VAN": "Vanuatu",
        "VEN": "Venezuela",
        "XVC": "Viet Cong (South Vietnam)*",
        "XFV": "Viet Minh (France)*",
        "VN": "Viet Nam",
        "SAH": "Western Sahara",
        "YEM": "Yemen",
        "YAR": "Yemen Arab Republic",
        "YUG": "Yugoslavia",
        "ZAM": "Zambia",
        "XZZ": "ZAPU (Zimbabwe)*",
    }
    return mp[country_code]