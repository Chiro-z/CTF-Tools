# Şifreli hex verisi
hex_data = "3222180926570b391c222312213322125e36193527042741370a262c1a03141e2c422314121a002b"

# Hex'i byte dizisine çevir
cipher_bytes = bytes.fromhex(hex_data)

# Anahtarın bildiğimiz kısmı (THM{ ile bulduğumuz kısım)
known_key = "fjUr"

print("Olası sonuçlar taranıyor...\n")

# Anahtarın 5. karakterini bulmak için yazdırılabilir tüm karakterleri deniyoruz
import string
for char in string.printable:
    # 5 karakterlik tam anahtar denemesi
    key_guess = known_key + char
    
    decrypted_text = ""
    # Tüm şifreli metni bu anahtarla çözmeyi dene
    for i in range(len(cipher_bytes)):
        # XOR işlemi: ŞifreliByte XOR AnahtarKarakteri
        decrypted_char = cipher_bytes[i] ^ ord(key_guess[i % 5])
        decrypted_text += chr(decrypted_char)
    
    # Eğer sonuç mantıklı görünüyorsa ekrana bas
    if "THM{" in decrypted_text:
        print(f"[+] ANAHTAR BULUNDU: {key_guess}")
        print(f"[+] BAYRAK: {decrypted_text}")
        print("-" * 30)
