from django.core.management.base import BaseCommand
from post.models import Post
import csv
from django.db import IntegrityError

class Command(BaseCommand):

    def __init__(self):
        self.cur_dict = {"taiwan" :"TWD", "côte d'ivoire": "XOF", 'afghanistan': 'AFN', 'albania': 'ALL', 'algeria': 'DZD', 'american samoa': 'USD', 'andorra': 'EUR', 'angola': 'AOA', 'anguilla': 'XCD', 'antarctica': 'XCD', 'antigua and barbuda': 'XCD', 'argentina': 'ARS', 'armenia': 'AMD', 'aruba': 'AWG', 'australia': 'AUD', 'austria': 'EUR', 'azerbaijan': 'AZN', 'bahamas': 'BSD', 'bahrain': 'BHD', 'bangladesh': 'BDT', 'barbados': 'BBD', 'belarus': 'BYR', 'belgium': 'EUR', 'belize': 'BZD', 'benin': 'XOF', 'bermuda': 'BMD', 'bhutan': 'BTN', 'bolivia': 'BOB', 'bosnia and herzegovina': 'BAM', 'botswana': 'BWP', 'bouvet island': 'NOK', 'brazil': 'BRL', 'british indian ocean territory': 'USD', 'brunei': 'BND', 'bulgaria': 'BGN', 'burkina faso': 'XOF', 'burundi': 'BIF', 'cambodia': 'KHR', 'cameroon': 'XAF', 'canada': 'CAD', 'cape verde': 'CVE', 'cayman islands': 'KYD', 'central african republic': 'XAF', 'chad': 'XAF', 'chile': 'CLP', 'china': 'CNY', 'christmas island': 'AUD', 'cocos (keeling) islands': 'AUD', 'colombia': 'COP', 'comoros': 'KMF', 'congo': 'XAF','congo (kinshasa)':'XAF', 'congo (brazzaville)': 'XAF', 'cook islands': 'NZD', 'costa rica': 'CRC', 'croatia': 'HRK', 'cuba': 'CUP', 'cyprus': 'EUR', 'czechia': 'CZK', 'czech republic': 'CZK', 'denmark': 'DKK', 'djibouti': 'DJF', 'dominica': 'XCD', 'dominican republic': 'DOP', 'east timor': 'USD', 'ecuador': 'ECS', 'egypt': 'EGP', 'el salvador': 'SVC', 'england': 'GBP', 'equatorial guinea': 'XAF', 'eritrea': 'ERN', 'estonia': 'EUR', 'ethiopia': 'ETB', 'falkland islands': 'FKP', 'faroe islands': 'DKK', 'fiji islands': 'FJD', 'finland': 'EUR', 'france': 'EUR', 'french guiana': 'EUR', 'french polynesia': 'XPF', 'french southern territories': 'EUR', 'gabon': 'XAF', 'gambia': 'GMD', 'georgia': 'GEL', 'germany': 'EUR', 'ghana': 'GHS', 'gibraltar': 'GIP', 'greece': 'EUR', 'greenland': 'DKK', 'grenada': 'XCD', 'guadeloupe': 'EUR', 'guam': 'USD', 'guatemala': 'QTQ', 'guinea': 'GNF', 'guinea-bissau': 'CFA', 'guyana': 'GYD', 'haiti': 'HTG', 'heard island and mcdonald islands': 'AUD', 'holy see (vatican city state)': 'EUR', 'honduras': 'HNL', 'hong kong': 'HKD', 'hungary': 'HUF', 'iceland': 'ISK', 'india': 'INR', 'indonesia': 'IDR', 'iran': 'IRR', 'iraq': 'IQD', 'ireland': 'EUR', 'israel': 'ILS', 'italy': 'EUR', 'ivory coast': 'XOF', 'jamaica': 'JMD', 'japan': 'JPY', 'jordan': 'JOD', 'kazakhstan': 'KZT', 'kenya': 'KES', 'kiribati': 'AUD', 'kuwait': 'KWD', 'kyrgyzstan': 'KGS', 'laos': 'LAK', 'latvia': 'LVL', 'lebanon': 'LBP', 'lesotho': 'LSL', 'liberia': 'LRD', 'libya': 'LYD', 'libyan arab jamahiriya': 'LYD', 'liechtenstein': 'CHF', 'lithuania': 'LTL', 'luxembourg': 'EUR', 'macau': 'MOP', 'north macedonia': 'MKD', 'macedonia': 'MKD', 'madagascar': 'MGF', 'malawi': 'MWK', 'malaysia': 'MYR', 'maldives': 'MVR', 'mali': 'XOF', 'malta': 'EUR', 'marshall islands': 'USD', 'martinique': 'EUR', 'mauritania': 'MRO', 'mauritius': 'MUR', 'mayotte': 'EUR', 'mexico': 'MXN', 'micronesia, federated states of': 'USD', 'moldova': 'MDL', 'monaco': 'EUR', 'mongolia': 'MNT', 'montserrat': 'XCD', 'morocco': 'MAD', 'mozambique': 'MZN', 'myanmar': 'MMR', 'namibia': 'NAD', 'nauru': 'AUD', 'nepal': 'NPR', 'netherlands': 'EUR', 'netherlands antilles': 'ANG', 'new caledonia': 'XPF', 'new zealand': 'NZD', 'nicaragua': 'NIO', 'niger': 'XOF', 'nigeria': 'NGN', 'niue': 'NZD', 'norfolk island': 'AUD', 'north korea': 'KPW', 'northern ireland': 'GBP', 'northern mariana islands': 'USD', 'norway': 'NOK', 'oman': 'OMR', 'pakistan': 'PKR', 'palau': 'USD', 'palestine': None, 'panama': 'PAB', 'papua new guinea': 'PGK', 'paraguay': 'PYG', 'peru': 'PEN', 'philippines': 'PHP', 'pitcairn islands': 'NZD', 'poland': 'PLN', 'portugal': 'EUR', 'puerto rico': 'USD', 'qatar': 'QAR', 'reunion': 'EUR', 'romania': 'RON', 'russian federation': 'RUB', 'russia': 'RUB', 'rwanda': 'RWF', 'saint helena': 'SHP', 'saint kitts and nevis': 'XCD', 'saint lucia': 'XCD', 'saint pierre and miquelon': 'EUR', 'saint vincent and the grenadines': 'XCD', 'samoa': 'WST', 'san marino': 'EUR', 'sao tome and principe': 'STD', 'saudi arabia': 'SAR', 'scotland': 'GBP', 'senegal': 'XOF', 'serbia': 'RSD', 'seychelles': 'SCR', 'sierra leone': 'SLL', 'singapore': 'SGD', 'slovakia': 'EUR', 'slovenia': 'EUR', 'solomon islands': 'SBD', 'somalia': 'SOS', 'south africa': 'ZAR', 'south georgia and the south sandwich islands': 'GBP', 'south korea': 'KRW', 'south sudan': 'SSP', 'spain': 'EUR', 'sri lanka': 'LKR', 'sudan': 'SDG', 'suriname': 'SRD', 'svalbard and jan mayen': 'NOK', 'swaziland': 'SZL', 'sweden': 'SEK', 'switzerland': 'CHF', 'syria': 'SYP', 'tajikistan': 'TJS', 'tanzania': 'TZS', 'thailand': 'THB', 'the democratic republic of congo': 'CDF', 'togo': 'XOF', 'tokelau': 'NZD', 'tonga': 'TOP', 'trinidad and tobago': 'TTD', 'tunisia': 'TND', 'turkey': 'TRY', 'turkmenistan': 'TMT', 'turks and caicos islands': 'USD', 'tuvalu': 'AUD', 'uganda': 'UGX', 'ukraine': 'UAH', 'united arab emirates': 'AED', 'united kingdom': 'GBP', 'united states': 'USD', 'united states minor outlying islands': 'USD', 'uruguay': 'UYU', 'uzbekistan': 'UZS', 'vanuatu': 'VUV', 'venezuela': 'VEF', 'vietnam': 'VND', 'virgin islands, british': 'USD', 'virgin islands, u.s.': 'USD', 'wales': 'GBP', 'wallis and futuna': 'XPF', 'western sahara': 'MAD', 'yemen': 'YER', 'zambia': 'ZMW', 'zimbabwe': 'ZWD'}
        self.continent_dict = {'macau': 'Asia', 'macedonia': 'Europe', "libya": 'Africa', "czechia": 'Europe',"taiwan" :"Asia", "côte d'ivoire": "Africa", 'russia': 'Asia, Europe', 'afghanistan': 'Asia', 'albania': 'Europe', 'algeria': 'Africa', 'american samoa': 'Oceania', 'andorra': 'Europe', 'angola': 'Africa', 'anguilla': 'North America', 'antarctica': 'Antarctica', 'antigua and barbuda': 'North America', 'argentina': 'South America', 'armenia': 'Asia', 'aruba': 'North America', 'australia': 'Oceania', 'austria': 'Europe', 'azerbaijan': 'Asia', 'bahamas': 'North America', 'bahrain': 'Asia', 'bangladesh': 'Asia', 'barbados': 'North America', 'belarus': 'Europe', 'belgium': 'Europe', 'belize': 'North America', 'benin': 'Africa', 'bermuda': 'North America', 'bhutan': 'Asia', 'bolivia': 'South America', 'bosnia and herzegovina': 'Europe', 'botswana': 'Africa', 'bouvet island': 'Antarctica', 'brazil': 'South America', 'british indian ocean territory': 'Africa', 'brunei': 'Asia', 'bulgaria': 'Europe', 'burkina faso': 'Africa', 'burundi': 'Africa', 'cambodia': 'Asia', 'cameroon': 'Africa', 'canada': 'North America', 'cape verde': 'Africa', 'cayman islands': 'North America', 'central african republic': 'Africa', 'chad': 'Africa', 'chile': 'South America', 'china': 'Asia', 'christmas island': 'Oceania', 'cocos (keeling) islands': 'Oceania', 'colombia': 'South America', 'comoros': 'Africa', 'congo': 'Africa', 'cook islands': 'Oceania', 'costa rica': 'North America', 'croatia': 'Europe', 'cuba': 'North America', 'cyprus': 'Asia', 'czech republic': 'Europe', 'denmark': 'Europe', 'djibouti': 'Africa', 'dominica': 'North America', 'dominican republic': 'North America', 'east timor': 'Asia', 'ecuador': 'South America', 'egypt': 'Africa', 'el salvador': 'North America', 'england': 'Europe', 'equatorial guinea': 'Africa', 'eritrea': 'Africa', 'estonia': 'Europe', 'ethiopia': 'Africa', 'falkland islands': 'South America', 'faroe islands': 'Europe', 'fiji islands': 'Oceania', 'finland': 'Europe', 'france': 'Europe', 'french guiana': 'South America', 'french polynesia': 'Oceania', 'french southern territories': 'Antarctica', 'gabon': 'Africa', 'gambia': 'Africa', 'georgia': 'Asia', 'germany': 'Europe', 'ghana': 'Africa', 'gibraltar': 'Europe', 'greece': 'Europe', 'greenland': 'North America', 'grenada': 'North America', 'guadeloupe': 'North America', 'guam': 'Oceania', 'guatemala': 'North America', 'guinea': 'Africa', 'guinea-bissau': 'Africa', 'guyana': 'South America', 'haiti': 'North America', 'heard island and mcdonald islands': 'Antarctica', 'holy see (vatican city state)': 'Europe', 'honduras': 'North America', 'hong kong': 'Asia', 'hungary': 'Europe', 'iceland': 'Europe', 'india': 'Asia', 'indonesia': 'Asia', 'iran': 'Asia', 'iraq': 'Asia', 'ireland': 'Europe', 'israel': 'Asia', 'italy': 'Europe', 'ivory coast': 'Africa', 'jamaica': 'North America', 'japan': 'Asia', 'jordan': 'Asia', 'kazakhstan': 'Asia', 'kenya': 'Africa', 'kiribati': 'Oceania', 'kuwait': 'Asia', 'kyrgyzstan': 'Asia', 'laos': 'Asia', 'latvia': 'Europe', 'lebanon': 'Asia', 'lesotho': 'Africa', 'liberia': 'Africa', 'libyan arab jamahiriya': 'Africa', 'liechtenstein': 'Europe', 'lithuania': 'Europe', 'luxembourg': 'Europe', 'macao': 'Asia', 'north macedonia': 'Europe', 'madagascar': 'Africa', 'malawi': 'Africa', 'malaysia': 'Asia', 'maldives': 'Asia', 'mali': 'Africa', 'malta': 'Europe', 'marshall islands': 'Oceania', 'martinique': 'North America', 'mauritania': 'Africa', 'mauritius': 'Africa', 'mayotte': 'Africa', 'mexico': 'North America', 'micronesia, federated states of': 'Oceania', 'moldova': 'Europe', 'monaco': 'Europe', 'mongolia': 'Asia', 'montenegro': 'Europe', 'montserrat': 'North America', 'morocco': 'Africa', 'mozambique': 'Africa', 'myanmar': 'Asia', 'namibia': 'Africa', 'nauru': 'Oceania', 'nepal': 'Asia', 'netherlands': 'Europe', 'netherlands antilles': 'North America', 'new caledonia': 'Oceania', 'new zealand': 'Oceania', 'nicaragua': 'North America', 'niger': 'Africa', 'nigeria': 'Africa', 'niue': 'Oceania', 'norfolk island': 'Oceania', 'north korea': 'Asia', 'northern ireland': 'Europe', 'northern mariana islands': 'Oceania', 'norway': 'Europe', 'oman': 'Asia', 'pakistan': 'Asia', 'palau': 'Oceania', 'palestine': 'Asia', 'panama': 'North America', 'papua new guinea': 'Oceania', 'paraguay': 'South America', 'peru': 'South America', 'philippines': 'Asia', 'pitcairn': 'Oceania', 'poland': 'Europe', 'portugal': 'Europe', 'puerto rico': 'North America', 'qatar': 'Asia', 'reunion': 'Africa', 'romania': 'Europe', 'russian federation': 'Europe', 'rwanda': 'Africa', 'saint helena': 'Africa', 'saint kitts and nevis': 'North America', 'saint lucia': 'North America', 'saint pierre and miquelon': 'North America', 'saint vincent and the grenadines': 'North America', 'samoa': 'Oceania', 'san marino': 'Europe', 'sao tome and principe': 'Africa', 'saudi arabia': 'Asia', 'scotland': 'Europe', 'senegal': 'Africa', 'serbia': 'Europe', 'seychelles': 'Africa', 'sierra leone': 'Africa', 'singapore': 'Asia', 'slovakia': 'Europe', 'slovenia': 'Europe', 'solomon islands': 'Oceania', 'somalia': 'Africa', 'south africa': 'Africa', 'south georgia and the south sandwich islands': 'Antarctica', 'south korea': 'Asia', 'south sudan': 'Africa', 'spain': 'Europe', 'sri lanka': 'Asia', 'sudan': 'Africa', 'suriname': 'South America', 'svalbard and jan mayen': 'Europe', 'swaziland': 'Africa', 'sweden': 'Europe', 'switzerland': 'Europe', 'syria': 'Asia', 'tajikistan': 'Asia', 'tanzania': 'Africa', 'thailand': 'Asia', 'the democratic republic of congo': 'Africa', 'togo': 'Africa', 'tokelau': 'Oceania', 'tonga': 'Oceania', 'trinidad and tobago': 'North America', 'tunisia': 'Africa', 'turkey': 'Asia', 'turkmenistan': 'Asia', 'turks and caicos islands': 'North America', 'tuvalu': 'Oceania', 'uganda': 'Africa', 'ukraine': 'Europe', 'united arab emirates': 'Asia', 'united kingdom': 'Europe', 'united states': 'North America', 'united states minor outlying islands': 'Oceania', 'uruguay': 'South America', 'uzbekistan': 'Asia', 'vanuatu': 'Oceania', 'venezuela': 'South America', 'vietnam': 'Asia', 'virgin islands, british': 'North America', 'virgin islands, u.s.': 'North America', 'wales': 'Europe', 'wallis and futuna': 'Oceania', 'western sahara': 'Africa', 'yemen': 'Asia', 'zambia': 'Africa', 'zimbabwe': 'Africa'}
        self.region_dict = {'macedonia': 'Europe', "libya": 'Africa', "czechia": 'Europe',"taiwan" :"Asia", "côte d'ivoire": "Africa", 'russia': 'Eastern Europe','afghanistan': 'Southern and Central Asia', 'albania': 'Southern Europe', 'algeria': 'Northern Africa', 'american samoa': 'Polynesia', 'andorra': 'Southern Europe', 'angola': 'Central Africa', 'anguilla': 'Caribbean', 'antarctica': 'Antarctica', 'antigua and barbuda': 'Caribbean', 'argentina': 'South America', 'armenia': 'Middle East', 'aruba': 'Caribbean', 'australia': 'Australia and New Zealand', 'austria': 'Western Europe', 'azerbaijan': 'Middle East', 'bahamas': 'Caribbean', 'bahrain': 'Middle East', 'bangladesh': 'Southern and Central Asia', 'barbados': 'Caribbean', 'belarus': 'Eastern Europe', 'belgium': 'Western Europe', 'belize': 'Central America', 'benin': 'Western Africa', 'bermuda': 'North America', 'bhutan': 'Southern and Central Asia', 'bolivia': 'South America', 'bosnia and herzegovina': 'Southern Europe', 'botswana': 'Southern Africa', 'bouvet island': 'Antarctica', 'brazil': 'South America', 'british indian ocean territory': 'Eastern Africa', 'brunei': 'Southeast Asia', 'bulgaria': 'Eastern Europe', 'burkina faso': 'Western Africa', 'burundi': 'Eastern Africa', 'cambodia': 'Southeast Asia', 'cameroon': 'Central Africa', 'canada': 'North America', 'cape verde': 'Western Africa', 'cayman islands': 'Caribbean', 'central african republic': 'Central Africa', 'chad': 'Central Africa', 'chile': 'South America', 'china': 'Eastern Asia', 'christmas island': 'Australia and New Zealand', 'cocos (keeling) islands': 'Australia and New Zealand', 'colombia': 'South America', 'comoros': 'Eastern Africa', 'congo': 'Central Africa', 'cook islands': 'Polynesia', 'costa rica': 'Central America', 'croatia': 'Southern Europe', 'cuba': 'Caribbean', 'cyprus': 'Middle East', 'czech republic': 'Eastern Europe', 'denmark': 'Nordic Countries', 'djibouti': 'Eastern Africa', 'dominica': 'Caribbean', 'dominican republic': 'Caribbean', 'east timor': 'Southeast Asia', 'ecuador': 'South America', 'egypt': 'Northern Africa', 'el salvador': 'Central America', 'england': None, 'equatorial guinea': 'Central Africa', 'eritrea': 'Eastern Africa', 'estonia': 'Baltic Countries', 'ethiopia': 'Eastern Africa', 'falkland islands': 'South America', 'faroe islands': 'Nordic Countries', 'fiji islands': 'Melanesia', 'finland': 'Nordic Countries', 'france': 'Western Europe', 'french guiana': 'South America', 'french polynesia': 'Polynesia', 'french southern territories': 'Antarctica', 'gabon': 'Central Africa', 'gambia': 'Western Africa', 'georgia': 'Middle East', 'germany': 'Western Europe', 'ghana': 'Western Africa', 'gibraltar': 'Southern Europe', 'greece': 'Southern Europe', 'greenland': 'North America', 'grenada': 'Caribbean', 'guadeloupe': 'Caribbean', 'guam': 'Micronesia', 'guatemala': 'Central America', 'guinea': 'Western Africa', 'guinea-bissau': 'Western Africa', 'guyana': 'South America', 'haiti': 'Caribbean', 'heard island and mcdonald islands': 'Antarctica', 'holy see (vatican city state)': 'Southern Europe', 'honduras': 'Central America', 'hong kong': 'Eastern Asia', 'hungary': 'Eastern Europe', 'iceland': 'Nordic Countries', 'india': 'Southern and Central Asia', 'indonesia': 'Southeast Asia', 'iran': 'Southern and Central Asia', 'iraq': 'Middle East', 'ireland': 'British Isles', 'israel': 'Middle East', 'italy': 'Southern Europe', 'ivory coast': 'Western Africa', 'jamaica': 'Caribbean', 'japan': 'Eastern Asia', 'jordan': 'Middle East', 'kazakhstan': 'Southern and Central Asia', 'kenya': 'Eastern Africa', 'kiribati': 'Micronesia', 'kuwait': 'Middle East', 'kyrgyzstan': 'Southern and Central Asia', 'laos': 'Southeast Asia', 'latvia': 'Baltic Countries', 'lebanon': 'Middle East', 'lesotho': 'Southern Africa', 'liberia': 'Western Africa', 'libyan arab jamahiriya': 'Northern Africa', 'liechtenstein': 'Western Europe', 'lithuania': 'Baltic Countries', 'luxembourg': 'Western Europe', 'macau': 'Eastern Asia', 'north macedonia': 'Southern Europe', 'madagascar': 'Eastern Africa', 'malawi': 'Eastern Africa', 'malaysia': 'Southeast Asia', 'maldives': 'Southern and Central Asia', 'mali': 'Western Africa', 'malta': 'Southern Europe', 'marshall islands': 'Micronesia', 'martinique': 'Caribbean', 'mauritania': 'Western Africa', 'mauritius': 'Eastern Africa', 'mayotte': 'Eastern Africa', 'mexico': 'Central America', 'micronesia, federated states of': 'Micronesia', 'moldova': 'Eastern Europe', 'monaco': 'Western Europe', 'mongolia': 'Eastern Asia', 'montserrat': 'Caribbean', 'morocco': 'Northern Africa', 'mozambique': 'Eastern Africa', 'myanmar': 'Southeast Asia', 'namibia': 'Southern Africa', 'nauru': 'Micronesia', 'nepal': 'Southern and Central Asia', 'netherlands': 'Western Europe', 'netherlands antilles': 'Caribbean', 'new caledonia': 'Melanesia', 'new zealand': 'Australia and New Zealand', 'nicaragua': 'Central America', 'niger': 'Western Africa', 'nigeria': 'Western Africa', 'niue': 'Polynesia', 'norfolk island': 'Australia and New Zealand', 'north korea': 'Eastern Asia', 'northern ireland': None, 'northern mariana islands': 'Micronesia', 'norway': 'Nordic Countries', 'oman': 'Middle East', 'pakistan': 'Southern and Central Asia', 'palau': 'Micronesia', 'palestine': 'Middle East', 'panama': 'Central America', 'papua new guinea': 'Melanesia', 'paraguay': 'South America', 'peru': 'South America', 'philippines': 'Southeast Asia', 'pitcairn': 'Polynesia', 'poland': 'Eastern Europe', 'portugal': 'Southern Europe', 'puerto rico': 'Caribbean', 'qatar': 'Middle East', 'reunion': 'Eastern Africa', 'romania': 'Eastern Europe', 'russian federation': 'Eastern Europe', 'rwanda': 'Eastern Africa', 'saint helena': 'Western Africa', 'saint kitts and nevis': 'Caribbean', 'saint lucia': 'Caribbean', 'saint pierre and miquelon': 'North America', 'saint vincent and the grenadines': 'Caribbean', 'samoa': 'Polynesia', 'san marino': 'Southern Europe', 'sao tome and principe': 'Central Africa', 'saudi arabia': 'Middle East', 'scotland': None, 'senegal': 'Western Africa', 'serbia': 'Central and Southeast Europe', 'seychelles': 'Eastern Africa', 'sierra leone': 'Western Africa', 'singapore': 'Southeast Asia', 'slovakia': 'Eastern Europe', 'slovenia': 'Southern Europe', 'solomon islands': 'Melanesia', 'somalia': 'Eastern Africa', 'south africa': 'Southern Africa', 'south georgia and the south sandwich islands': 'Antarctica', 'south korea': 'Eastern Asia', 'south sudan': 'Eastern Africa', 'spain': 'Southern Europe', 'sri lanka': 'Southern Asia', 'sudan': 'Northern Africa', 'suriname': 'South America', 'svalbard and jan mayen': 'Nordic Countries', 'swaziland': 'Southern Africa', 'sweden': 'Nordic Countries', 'switzerland': 'Western Europe', 'syria': 'Middle East', 'tajikistan': 'Southern and Central Asia', 'tanzania': 'Eastern Africa', 'thailand': 'Southeast Asia', 'the democratic republic of congo': None, 'togo': 'Western Africa', 'tokelau': 'Polynesia', 'tonga': 'Polynesia', 'trinidad and tobago': 'Caribbean', 'tunisia': 'Northern Africa', 'turkey': 'Middle East', 'turkmenistan': 'Southern and Central Asia', 'turks and caicos islands': 'Caribbean', 'tuvalu': 'Polynesia', 'uganda': 'Eastern Africa', 'ukraine': 'Eastern Europe', 'united arab emirates': 'Middle East', 'united kingdom': 'British Isles', 'united states': 'North America', 'united states minor outlying islands': 'Micronesia/Caribbean', 'uruguay': 'South America', 'uzbekistan': 'Southern and Central Asia', 'vanuatu': 'Melanesia', 'venezuela': 'South America', 'vietnam': 'Southeast Asia', 'virgin islands, british': None, 'virgin islands, u.s.': None, 'wales': None, 'wallis and futuna': 'Polynesia', 'western sahara': 'Northern Africa', 'yemen': 'Middle East', 'zambia': 'Eastern Africa', 'zimbabwe': 'Eastern Africa'}

    def add_arguments(self, parser):
        parser.add_argument('--min_population', nargs='?', type=int, default=500000, help='Select cities with X minimum of inhabitants | Default : 500000')
        parser.add_argument('--max_population', nargs='?', type=int, default=999999999, help='Select cities with X maximum of inhabitants')
        parser.add_argument('--keep_db', action='store_true', help="Add this if you don't want to delete() curent db before injection")

    def handle(self, **options):

        def perform():
            if not options['keep_db']:
                print(f"Deleting data ...")
                Post.objects.all().delete()
                print(f"Complete !")
            cities_injection()

        def cities_injection():
            with open('/Users/omegad/Documents/ocr/p13/digitravel/post/management/commands/worldcities.csv', 'r') as file:
                reader = csv.reader(file)
                min_population = options['min_population']
                max_population = options['max_population']
                print(f"Select cities with minimum of {min_population} inhabitants and maximum of {max_population}")
                for row in reader:
                    try:
                        if int(row[9]) >= min_population and int(row[9]) <= max_population:
                            new_post = Post.objects.get_or_create(
                                city = row[1],
                                country = row[4],
                                language = row[5],
                                population = row[9],
                                latitude = row[2],
                                longitude = row[3],
                                currency = self.cur_dict[row[4].lower()],
                                continent = self.continent_dict[row[4].lower()],
                                region = self.region_dict[row[4].lower()]
                                )
                            print(f"_ Injecting data : {new_post}         ", end='\r', flush=True)
                    except (ValueError, IntegrityError, KeyError):
                        pass
                print(" ")
                return print(f"Database ready : {len(Post.objects.all())} posts !")

        perform()