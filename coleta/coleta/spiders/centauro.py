import scrapy


class CentauroSpider(scrapy.Spider):
    name = "centauro"
    allowed_domains = ["www.centauro.com.br"]
    start_urls = ["https://www.centauro.com.br/nav/produto/tenis/esportes/academiafitness"]

    def parse(self, response):
        products = response.css('a.ProductCard-styled__Card-sc-bbe8eefb-0.kOXydP')
        for product in products:
            yield {
                'name': product.css('p.Typographystyled__Paragraph-sc-bdxvrr-1.knvuZc.ProductCard-styled__Title-sc-bbe8eefb-3.fnPvPK::text').get().split("-")[0],
                'current_price': product.css('p.Typographystyled__Paragraph-sc-bdxvrr-1.eFDcLB.Price-styled__CurrentPrice-sc-f65c9c0d-4.jNAhVm::text').get()
                
                }
        pass
