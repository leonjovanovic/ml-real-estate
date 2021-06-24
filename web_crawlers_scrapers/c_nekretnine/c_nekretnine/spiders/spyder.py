import scrapy
from protego import Protego
import re

all_urls = [
    'https://www.nekretnine.rs/stambeni-objekti/kuce/lista/po-stranici/10/'
]


class Spider(scrapy.Spider):
    name = "nekretnine"
    start_urls = [
        'https://www.nekretnine.rs/stambeni-objekti/kuce/lista/po-stranici/10/'
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
            if len(response.xpath('//h3[@class="stickyBox__Location"]/text()').get().split(",")) > 1:
                oglas[5] = response.xpath('//h3[@class="stickyBox__Location"]/text()').get().split(",")[1].strip()
            # ----------------------------------------------------------------------------------------------------------
            labels = response.xpath('//div[@class="property__main-details"]//ul//li//span/span/text()').getall()
            values = response.xpath('//div[@class="property__main-details"]//ul//li//span//text()').getall()
            del (values[0])
            i = 0
            for _ in labels:
                del (values[i])
                i += 1
            i = 0
            for _ in values:
                values[i] = values[i].strip()
                i += 1
            for label, value in zip(labels, values):
                self.checkLabelValue(oglas, label[:-1], value)
            # ----------------------------------------------------------------------------------------------------------
            # Godina izgradnje
            # Broj kupatila
            labels = response.xpath('//div[@class="property__amenities"]//ul//li/text()').getall()
            values = response.xpath('//div[@class="property__amenities"]//ul//li//strong/text()').getall()
            descr = response.xpath('//div[@class="cms-content-inner"]/text()').get()
            if descr.strip() is None or descr.strip() == '':
                descr = response.xpath('//div[@class="cms-content-inner"]//p/text()').getall()
                descr = ''.join(descr)
            descr_split = descr.split(" ")
            i = 0
            while i < len(labels):
                labels[i] = re.sub(r"[\n\t\s]*", "", labels[i])
                if labels[i] == '':
                    del (labels[i])
                else:
                    i += 1
            i = 0
            for _ in values:
                values[i] = values[i].strip()
                i += 1
            for label, value in zip(labels, values):
                temp = self.checkBathroom(oglas, label[:-1], value, descr, descr_split)
                if temp != 0:
                    break
            # Lift
            for label in labels:
                if "lift" in label or "Lift" in label:
                    oglas[15] = "Da"
                    break
            for label in labels:
                if "terasa" in label or "Terasa" in label or "Lođa" in label or "lođa" in label or "Balkon" in label or "balkon" in label:
                    oglas[16] = "Da"
                    break
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
        for a in response.css('a'):
            flag = False
            if 'class' not in a.attrib:
                flag = True
            else:
                if a.attrib['class'] == "akla_a1_N7Mi3Qf" or a.attrib['class'] == "akla_a1_dNekDR2" or a.attrib['class'] == "pagination-arrow arrow-left" or a.attrib['class'] == "next-number" or a.attrib['class'] == "pagination-arrow arrow-right" or a.attrib['class'] == "d-block next-article-button m-auto" or a.attrib['class'] == "d-block placeholder-preview-box ratio-4-3" or a.attrib['class'] == "dropdown-item":
                    flag = True
            if 'href' in a.attrib and flag:
                href = a.attrib['href']
                if href[0:25] == '/stambeni-objekti/stanovi' and len(response.url.split('/')) < 12:
                    yield response.follow(href, self.parse)
        # If we want specific link
        # pagination_links = response.css('li.next a')
        # yield from response.follow_all(anchors, callback=self.parse)

    def checkLabelValue(self, oglas, label, value):
        if label == "Kvadratura":
            oglas[6] = value.split(' m')[0]
        elif label == "Površina zemljišta":
            oglas[8] = value
        elif label == "Sprat":
            oglas[9] = value
        elif label == "Uknjiženo":
            oglas[10] = value
        elif label == "Grejanje":
            oglas[11] = value
        elif label == "Sobe":
            oglas[12] = value
        elif label == "Parking":
            oglas[14] = value

    def checkBathroom(self, oglas, label, value, descr, descr_split):
        if label == "Brojkupatila":
            oglas[13] = value
            return value
        else:
            s = 0
            s += descr.count("kupatilo")
            flag_toaleti = False
            i = 0
            for word in descr_split:
                if ("kupatila" in word or "toaleti" in word) and i > 0:
                    if "toaleti" in word and self.decodeNumber(descr_split[i - 1]) > 0:
                        flag_toaleti = True
                    s += self.decodeNumber(descr_split[i - 1])
                i += 1
            if not flag_toaleti:
                s += descr.count("toalet")
            oglas[13] = s
            return s

    def decodeNumber(self, n):
        if n.isdigit():
            return int(n)
        if "dva" in n or "Dva" in n:
            return 2
        if "tri" in n or "Tri" in n:
            return 3
        if "etiri" in n or "etiri" in n:
            return 4
        if "pet" in n or "Pet" in n:
            return 5
        if "sest" in n or "Sest" in n or "šest" in n or "Šest" in n:
            return 6
        return 0
