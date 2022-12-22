from django.core.management.base import BaseCommand
from post.models import Post
import json, csv
from django.db import IntegrityError
import os
import numpy as np

class Command(BaseCommand):
    def handle(self, *args, **options):
        """
        f = json.load(open('post/management/commands/city_list.json', 'r'))
        for item in f:
            print(item)
            print(item['city'])
            print(item['country'])
        """
        Post.objects.all().delete()

        def cities_injection():
            with open('/Users/omegad/Documents/ocr/p13/digitravel/post/management/commands/worldcities.csv', 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    try:
                        if int(row[9]) >= 500000:
                            new_post = Post.objects.create(
                                city = row[1],
                                country = row[4],
                                language = row[6],
                                population = row[10],
                                latitude = row[2],
                                longitude = row[3],
                                )
                            print(new_post)
                    except (ValueError, IntegrityError) as e:
                        print(e)
        

        #cities_injection()

        cur_dict = {'afghanistan': 'AFN', 'albania': 'ALL', 'algeria': 'DZD', 'american samoa': 'USD', 'andorra': 'EUR', 'angola': 'AOA', 'anguilla': 'XCD', 'antarctica': 'XCD', 'antigua and barbuda': 'XCD', 'argentina': 'ARS', 'armenia': 'AMD', 'aruba': 'AWG', 'australia': 'AUD', 'austria': 'EUR', 'azerbaijan': 'AZN', 'bahamas': 'BSD', 'bahrain': 'BHD', 'bangladesh': 'BDT', 'barbados': 'BBD', 'belarus': 'BYR', 'belgium': 'EUR', 'belize': 'BZD', 'benin': 'XOF', 'bermuda': 'BMD', 'bhutan': 'BTN', 'bolivia': 'BOB', 'bosnia and herzegovina': 'BAM', 'botswana': 'BWP', 'bouvet island': 'NOK', 'brazil': 'BRL', 'british indian ocean territory': 'USD', 'brunei': 'BND', 'bulgaria': 'BGN', 'burkina faso': 'XOF', 'burundi': 'BIF', 'cambodia': 'KHR', 'cameroon': 'XAF', 'canada': 'CAD', 'cape verde': 'CVE', 'cayman islands': 'KYD', 'central african republic': 'XAF', 'chad': 'XAF', 'chile': 'CLP', 'china': 'CNY', 'christmas island': 'AUD', 'cocos (keeling) islands': 'AUD', 'colombia': 'COP', 'comoros': 'KMF', 'congo': 'XAF', 'cook islands': 'NZD', 'costa rica': 'CRC', 'croatia': 'HRK', 'cuba': 'CUP', 'cyprus': 'EUR', 'czech republic': 'CZK', 'denmark': 'DKK', 'djibouti': 'DJF', 'dominica': 'XCD', 'dominican republic': 'DOP', 'east timor': 'USD', 'ecuador': 'ECS', 'egypt': 'EGP', 'el salvador': 'SVC', 'england': 'GBP', 'equatorial guinea': 'XAF', 'eritrea': 'ERN', 'estonia': 'EUR', 'ethiopia': 'ETB', 'falkland islands': 'FKP', 'faroe islands': 'DKK', 'fiji islands': 'FJD', 'finland': 'EUR', 'france': 'EUR', 'french guiana': 'EUR', 'french polynesia': 'XPF', 'french southern territories': 'EUR', 'gabon': 'XAF', 'gambia': 'GMD', 'georgia': 'GEL', 'germany': 'EUR', 'ghana': 'GHS', 'gibraltar': 'GIP', 'greece': 'EUR', 'greenland': 'DKK', 'grenada': 'XCD', 'guadeloupe': 'EUR', 'guam': 'USD', 'guatemala': 'QTQ', 'guinea': 'GNF', 'guinea-bissau': 'CFA', 'guyana': 'GYD', 'haiti': 'HTG', 'heard island and mcdonald islands': 'AUD', 'holy see (vatican city state)': 'EUR', 'honduras': 'HNL', 'hong kong': 'HKD', 'hungary': 'HUF', 'iceland': 'ISK', 'india': 'INR', 'indonesia': 'IDR', 'iran': 'IRR', 'iraq': 'IQD', 'ireland': 'EUR', 'israel': 'ILS', 'italy': 'EUR', 'ivory coast': 'XOF', 'jamaica': 'JMD', 'japan': 'JPY', 'jordan': 'JOD', 'kazakhstan': 'KZT', 'kenya': 'KES', 'kiribati': 'AUD', 'kuwait': 'KWD', 'kyrgyzstan': 'KGS', 'laos': 'LAK', 'latvia': 'LVL', 'lebanon': 'LBP', 'lesotho': 'LSL', 'liberia': 'LRD', 'libyan arab jamahiriya': 'LYD', 'liechtenstein': 'CHF', 'lithuania': 'LTL', 'luxembourg': 'EUR', 'macau': 'MOP', 'north macedonia': 'MKD', 'madagascar': 'MGF', 'malawi': 'MWK', 'malaysia': 'MYR', 'maldives': 'MVR', 'mali': 'XOF', 'malta': 'EUR', 'marshall islands': 'USD', 'martinique': 'EUR', 'mauritania': 'MRO', 'mauritius': 'MUR', 'mayotte': 'EUR', 'mexico': 'MXN', 'micronesia, federated states of': 'USD', 'moldova': 'MDL', 'monaco': 'EUR', 'mongolia': 'MNT', 'montserrat': 'XCD', 'morocco': 'MAD', 'mozambique': 'MZN', 'myanmar': 'MMR', 'namibia': 'NAD', 'nauru': 'AUD', 'nepal': 'NPR', 'netherlands': 'EUR', 'netherlands antilles': 'ANG', 'new caledonia': 'XPF', 'new zealand': 'NZD', 'nicaragua': 'NIO', 'niger': 'XOF', 'nigeria': 'NGN', 'niue': 'NZD', 'norfolk island': 'AUD', 'north korea': 'KPW', 'northern ireland': 'GBP', 'northern mariana islands': 'USD', 'norway': 'NOK', 'oman': 'OMR', 'pakistan': 'PKR', 'palau': 'USD', 'palestine': None, 'panama': 'PAB', 'papua new guinea': 'PGK', 'paraguay': 'PYG', 'peru': 'PEN', 'philippines': 'PHP', 'pitcairn islands': 'NZD', 'poland': 'PLN', 'portugal': 'EUR', 'puerto rico': 'USD', 'qatar': 'QAR', 'reunion': 'EUR', 'romania': 'RON', 'russian federation': 'RUB', 'rwanda': 'RWF', 'saint helena': 'SHP', 'saint kitts and nevis': 'XCD', 'saint lucia': 'XCD', 'saint pierre and miquelon': 'EUR', 'saint vincent and the grenadines': 'XCD', 'samoa': 'WST', 'san marino': 'EUR', 'sao tome and principe': 'STD', 'saudi arabia': 'SAR', 'scotland': 'GBP', 'senegal': 'XOF', 'serbia': 'RSD', 'seychelles': 'SCR', 'sierra leone': 'SLL', 'singapore': 'SGD', 'slovakia': 'EUR', 'slovenia': 'EUR', 'solomon islands': 'SBD', 'somalia': 'SOS', 'south africa': 'ZAR', 'south georgia and the south sandwich islands': 'GBP', 'south korea': 'KRW', 'south sudan': 'SSP', 'spain': 'EUR', 'sri lanka': 'LKR', 'sudan': 'SDG', 'suriname': 'SRD', 'svalbard and jan mayen': 'NOK', 'swaziland': 'SZL', 'sweden': 'SEK', 'switzerland': 'CHF', 'syria': 'SYP', 'tajikistan': 'TJS', 'tanzania': 'TZS', 'thailand': 'THB', 'the democratic republic of congo': 'CDF', 'togo': 'XOF', 'tokelau': 'NZD', 'tonga': 'TOP', 'trinidad and tobago': 'TTD', 'tunisia': 'TND', 'turkey': 'TRY', 'turkmenistan': 'TMT', 'turks and caicos islands': 'USD', 'tuvalu': 'AUD', 'uganda': 'UGX', 'ukraine': 'UAH', 'united arab emirates': 'AED', 'united kingdom': 'GBP', 'united states': 'USD', 'united states minor outlying islands': 'USD', 'uruguay': 'UYU', 'uzbekistan': 'UZS', 'vanuatu': 'VUV', 'venezuela': 'VEF', 'vietnam': 'VND', 'virgin islands, british': 'USD', 'virgin islands, u.s.': 'USD', 'wales': 'GBP', 'wallis and futuna': 'XPF', 'western sahara': 'MAD', 'yemen': 'YER', 'zambia': 'ZMW', 'zimbabwe': 'ZWD'}
        print(cur_dict['france'])