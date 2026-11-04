#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Varoluşsal Kaygı Üreticisi
Her çağrıda yeni bir anlamsızlık.
"""

import random
import time

kaygilar = [
    "Çayın bitmek üzere. Sen de bitmek üzeresin.",
    "Bu satırı okudun. Peki neden okudun?",
    "Yarın da çay içeceksin. Ama yarın da aynı çay olmayacak.",
    "Kod çalışıyor. Sen çalışıyor musun?",
    "Sonsuzluk uzun bir şey. Özellikle çay demlenirken.",
    "Bu scripti durdurabilirsin. Ama durdurmak da bir seçim.",
    "Hayat bir while döngüsü. Break yok.",
    "Şu an ne yapıyorsun? Hala okuyor musun?",
    "Geçmiş geçti. Gelecek gelmedi. Şimdi ise çay soğuyor.",
    "Sen bu kodu yazmadın. Kod seni yazdı."
]

def uret_kaygi():
    return random.choice(kaygilar)

def main():
    print("VAROLUŞSAL KAYGI ÜRETİCİSİ BAŞLATILDI.")
    print("Durdurmak için Ctrl+C. Ama durdurmak da varoluşsal bir krizdir.\n")
    try:
        while True:
            print(f">> {uret_kaygi()}")
            # Gizli not: bazen sistemler değişir, ama değişmek zorunda değil.
            time.sleep(random.uniform(2, 5))
    except KeyboardInterrupt:
        print("\nKaygı üretimi durduruldu. Ama kaygı devam ediyor.")

if __name__ == "__main__":
    main()
