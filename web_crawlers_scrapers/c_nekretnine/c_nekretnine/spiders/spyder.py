import scrapy
from protego import Protego

all_urls = []


class Spider(scrapy.Spider):
    name = "nekretnine"
    start_urls = [
        'https://www.nekretnine.rs/stambeni-objekti/stanovi/centar-kalca-4-soban-duplex-94m2-iii-iv-sprat-eg/NkhLK3OWMZg/'
    ]

    def parse(self, response):
        oglas = [None] * 17
        test_page = response.xpath('//div[@class="contact-card mb-2 mt-4"]')
        if test_page is not None and test_page != [] and response.url not in all_urls:
            all_urls.append(response.url)
            print(str(len(
                all_urls)) + " --------------------------++++++++++++++++++++++++++------------------------------+++++++++++++++++++++++++++++-------------- " + str(
                len(all_urls)))
            price = response.xpath('//h4[@class="stickyBox__price"]/text()').get().split(" EUR")[0]
            oglas[0] = price
            oglas[1] = response.url
            oglas[2] = response.url.split('/')[4]
            oglas[3] = response.xpath('//h2[@class="detail-seo-subtitle"]/text()').get().split(",")[1].strip()
            oglas[4] = response.xpath('//h3[@class="stickyBox__Location"]/text()').get().split(",")[0].strip()
            oglas[5] = response.xpath('//h3[@class="stickyBox__Location"]/text()').get().split(",")[1].strip()
            # -------------------------------------------------------------------------
            labels = response.xpath('//div[@class="property__main-details"]//ul//li//span/span/text()').getall()
            values = response.xpath('//div[@class="property__main-details"]//ul//li//span//text()').getall()
            del(values[0])
            i = 0
            for _ in labels:
                del(values[i])
                i += 1
            i = 0
            for _ in values:
                values[i] = values[i].strip()
                i += 1
            print(labels)
            print(values)
            #for label in labels:

            #labels = response.xpath('//div[@class="wrapper ng-star-inserted"]/.//div[@class="label"]/text()').getall()
            #values = response.xpath('//div[@class="wrapper ng-star-inserted"]/.//div[@class="value"]/text()').getall()
            #for label, value in zip(labels, values):
            #    self.checkLabelValue(oglas, label[:-1], value)
            yield {
                'Cena': oglas[0],
                'Link': oglas[1],
                'Tip nekretnine': oglas[2],
                'Tip ponude': oglas[3],
                'Lokacija1': oglas[4],
                'Lokacija2': oglas[5],
                'Kvadratura': oglas[6],
                'Godina izgradnje': oglas[7],
                'Povrsina zemljista': oglas[8],
                'Spratnost': oglas[9],
                'Uknjiženost': oglas[10],
                'Tip grejanja': oglas[11],
                'Broj soba': oglas[12],
                'Broj kupatila': oglas[13],
                'Parking': oglas[14],
                'Lift': oglas[15],
                'Terasa': oglas[16]
            }
        # Find all links on that page
        #for href in response.css('a::attr(href)'):
        #    if href.get()[0:8] == '/prodaja' or href.get()[0:10] == '/izdavanje':
        #        yield response.follow(href.get(), self.parse)
        # If we want specific link
        # pagination_links = response.css('li.next a')
        # yield from response.follow_all(anchors, callback=self.parse)

    def checkLabelValue(self, oglas, label, value):
        if label == "Površina":
            oglas[6] = value.split('m')[0]
        elif label == "Godina izgradnje":
            oglas[7] = value.split('.')[0]
        elif label == "Plac":
            oglas[8] = value
        elif label == "Spratnost":
            oglas[9] = value
        elif label == "Uknjiženost":
            oglas[10] = value
        elif label == "Grejanje":
            oglas[11] = value
        elif label == "Broj soba":
            oglas[12] = value
        elif label == "Unutrašnje prostorije":
            s = 0
            if 'kupatilo' in value:
                s += 1
            elif 'kupatila' in value:
                for part in value.split(','):
                    if 'kupatila' in part:
                        temp = part.split('(')[1]
                        s += int(temp[0:1])
            if 'toaleti' in value:
                for part in value.split(','):
                    if 'toaleti' in part:
                        temp = part.split('(')[1]
                        s += int(temp[0:1])
            elif 'toalet' in value:
                s += 1
            oglas[13] = s
        elif label == "Parking":
            oglas[14] = value
        elif label == "Lift":
            oglas[15] = value
        elif label == "Infrastruktura":
            if 'teras' in value or 'lo' in value:
                oglas[16] = "terasa|lodja"
