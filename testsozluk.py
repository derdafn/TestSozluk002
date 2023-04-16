meme_sozlugu = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "SHEESH": "onaylamamak",
            "LOW HP": "DÜŞÜK CAN",
            "FLASH": "IŞIK"
            }
kelime = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")
if kelime in meme_sozlugu.keys():
    print("Kelime Bulundu")
else:
    print("Eksik veya Hatalı Kelime Girdiniz")
