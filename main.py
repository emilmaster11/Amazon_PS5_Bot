from bot import AmazonBot


if __name__ == "__main__":
    ps5 = AmazonBot("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36")
    

    ps5.go_to_product(r"https://www.amazon.de/ECHTPower-Controller-Ladestation-Schnelllade-Playstation/dp/B08PCMKR2C/?_encoding=UTF8&pd_rd_w=20NbL&content-id=amzn1.sym.19b3c00c-468f-440c-b90d-756778c282ea&pf_rd_p=19b3c00c-468f-440c-b90d-756778c282ea&pf_rd_r=HSWNHR6Q78DTABHR2FK7&pd_rd_wg=bM3Q5&pd_rd_r=f437264f-8e62-4852-a720-751639a9b72d&ref_=pd_gw_ci_mcx_mi")
    ps5.put_to_shopping_card()
    
    #ps5.buy_now()
