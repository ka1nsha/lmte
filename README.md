# Let me teach English

Sürekli bilgisayar başında oturan insan olarak bana böyle oturduğum yerde kelime öğretecek veya gösterecek bir uygulamaya ihtiyaç duyuyordum.

Bu sebeple böyle bir python scripti yazma gereği duydum.

### İlgili script ne işe yarıyor ### 

Aynı dizinde bulunan  `quotes.json` dosyası içerisinden tüm json veriyi alıp len ile uzunluğunu alıyor. Daha sonrasında ise 0 ile Len boyutunda random bir sayı ile cümleyi seçip daha sonra o cümle uzunluğunda yeni bir random oluşturarak içierisinden kelime seçiyor. Daha sonra bunu translate edip database'e bunu gösterdim şeklinde kaydediyor tabi bu arada Linux sistemlerde ` Notify` çıkartmaktan da geri kalmıyor.



İlgili scripti crontab'a atarsanız size crontab da belirtilen süreler içerisinde gerekli notificationları çıkartacaktır.

Örnek crontab:

`crontab -e` 

```
0 * * * * main.py #  veya
@hourly
```

Aşağıya sadece terminal içerisinde text'i bastırdığım ( Notification'ı iptal ettiğim ) bir örneği bırakıyorum. Kelimeleri çevirmek için Google Translate kullanıyor.

[![asciicast](https://asciinema.org/a/oRY2H6RUf87aCN2xpNngFQ0iX.svg)](https://asciinema.org/a/oRY2H6RUf87aCN2xpNngFQ0iX)



Basit 1 günlük bir script, geliştirilebilir. 