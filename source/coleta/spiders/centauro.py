import scrapy

class CentauroSpider(scrapy.Spider):
    name = "centauro"
    allowed_domains = ["centauro.com.br"]
    start_urls = ["https://www.centauro.com.br/nav/produto/tenis/esportes/academiafitness"]
    pagina_atual = 1
    max_page = 10

    def parse(self, response):
        # Extrair informações dos produtos
        products = response.css('a.ProductCard-styled__Card-sc-bbe8eefb-0.kOXydP')
        for product in products:
            yield {
                'name': product.css('p.Typographystyled__Paragraph-sc-bdxvrr-1.knvuZc.ProductCard-styled__Title-sc-bbe8eefb-3.fnPvPK::text').get().split("-")[0],
                'brand': product.css('p.Typographystyled__Paragraph-sc-bdxvrr-1.knvuZc.ProductCard-styled__Title-sc-bbe8eefb-3.fnPvPK::text').get().split(" ")[1],
                'last_price': product.css('del.Typographystyled__Offer-sc-bdxvrr-4.cAyLkZ.Price-styled__OldPriceOffer-sc-f65c9c0d-2.hLWMiV::text').get(),
                'current_price': product.css('p.Typographystyled__Paragraph-sc-bdxvrr-1.eFDcLB.Price-styled__CurrentPrice-sc-f65c9c0d-4.jNAhVm::text').get()
            }
        
        # Incrementar o número da página e gerar a URL da próxima página
        if self.pagina_atual < self.max_page:
            self.pagina_atual += 1
            next_page = f"https://www.centauro.com.br/nav/produto/tenis/esportes/academiafitness?page={self.pagina_atual}"
            yield scrapy.Request(next_page, callback=self.parse)
