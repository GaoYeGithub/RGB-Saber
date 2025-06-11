# RGB Saber

## Description

Collapsible 3D printed light-saber made using strip of neopixels and a custom PCB in the bottom hilt to control power and motion effects. Made with translucent filament, and electronics.

## Motivation

I built this project to beacuse it combines my interests in 3D printing, electronics, and programming. I wanted a fun toy that invovles cadding, custom PCB, microcontroller, all while being cool.

---

## Gallery

### Full 3D Model
![Model](https://hc-cdn.hel1.your-objectstorage.com/s/v3/1d36873c29ba3a11aa21cd488ee18cd1a008545b_image.png)

### Assembly
![Assembly](https://hc-cdn.hel1.your-objectstorage.com/s/v3/33c3c40f43e308743065bab0ddf5dd657cb26b87_image.png)

### Schematic
![Schematic](https://hc-cdn.hel1.your-objectstorage.com/s/v3/510a52b7503bd1756012874e082a3a52cb886434_image.png)

### PCB Layout
![PCB](https://hc-cdn.hel1.your-objectstorage.com/s/v3/de6bb687d293a6ab25cb9b345f19867af3f4dfba_image.png)

---

## Bill of Materials

| Component                    | Quantity | Price(C$)    | Price    |
|------------------------------|:--------:|:--------:|:--------:|
| PLA or PETG Filament         |     1    | 17.20    | https://www.aliexpress.com/item/1005008799080678.html?spm=a2g0o.productlist.main.7.569155c4LpDaiD&algo_pvid=0cdf618c-4ac8-48f3-b76c-637597b9bf32&algo_exp_id=0cdf618c-4ac8-48f3-b76c-637597b9bf32-6&pdp_ext_f=%7B%22order%22%3A%2220%22%2C%22eval%22%3A%221%22%7D&pdp_npi=4%40dis%21CAD%2117.90%2117.20%21%21%2112.76%2112.26%21%402103241117496011728381886e0cfc%2112000046709698104%21sea%21CA%210%21ABX&curPageLogUid=TTxfIs3iXczu&utparam-url=scene%3Asearch%7Cquery_from%3A      |
| Custom PCB                   |     1    | 3.5      |       |
| Adafruit PowerBoost 500C     |     1    | 26       |       |
| MPU-6050                     |     1    | 2.16     | https://www.aliexpress.com/item/1005005682188615.html?spm=a2g0o.productlist.main.1.4e535c1dwuSMoC&algo_pvid=f0dd6247-6be6-4e40-af29-3791f561f5f8&algo_exp_id=f0dd6247-6be6-4e40-af29-3791f561f5f8-0&pdp_ext_f=%7B%22order%22%3A%22116%22%2C%22eval%22%3A%221%22%7D&pdp_npi=4%40dis%21CAD%212.86%212.16%21%21%2114.63%2111.05%21%402103247417496010492627169e4559%2112000033996007871%21sea%21CA%210%21ABX&curPageLogUid=RwTCb5QPqLdb&utparam-url=scene%3Asearch%7Cquery_from%3A      |
| Xiao Seeed RP2040            |     1    | 7.27     | https://www.aliexpress.com/item/1005008417542061.html?spm=a2g0o.productlist.main.1.481e7008rivjqS&algo_pvid=11cc1144-b9ab-43a2-9c0c-267de2563945&algo_exp_id=11cc1144-b9ab-43a2-9c0c-267de2563945-0&pdp_ext_f=%7B%22order%22%3A%22492%22%2C%22eval%22%3A%221%22%2C%22orig_sl_item_id%22%3A%221005008417542061%22%2C%22orig_item_id%22%3A%221005004459618789%22%7D&pdp_npi=4%40dis%21CAD%2115.94%217.27%21%21%2111.36%215.18%21%40210318e817496012303111303e073d%2112000044970570433%21sea%21CA%210%21ABX&curPageLogUid=BhqjZfFO2lA9&utparam-url=scene%3Asearch%7Cquery_from%3A      |
| Male Header Pins             |     3    | 2.68      | https://www.aliexpress.com/item/4000873858801.html?spm=a2g0o.productlist.main.1.17653d7caZEbCX&algo_pvid=7e6c9525-c84d-4b88-aefa-1952674cd5f5&algo_exp_id=7e6c9525-c84d-4b88-aefa-1952674cd5f5-0&pdp_ext_f=%7B%22order%22%3A%223658%22%2C%22eval%22%3A%221%22%7D&pdp_npi=4%40dis%21CAD%213.38%212.68%21%21%212.41%211.91%21%402103201917496012834233808e26f4%2110000010058190554%21sea%21CA%210%21ABX&curPageLogUid=K9WqpqLKTFdv&utparam-url=scene%3Asearch%7Cquery_from%3A      |
| 10 kΩ Resistor               |     2.47    |          | https://www.aliexpress.com/item/1005005670101072.html?spm=a2g0o.productlist.main.1.18ae7373QzZA2B&algo_pvid=66fd1724-733f-4ce0-8ba8-34b341e39640&algo_exp_id=66fd1724-733f-4ce0-8ba8-34b341e39640-0&pdp_ext_f=%7B%22order%22%3A%222247%22%2C%22eval%22%3A%221%22%7D&pdp_npi=4%40dis%21CAD%214.87%212.47%21%21%2124.95%2112.69%21%402103146f17496015463302370ed9d1%2112000033959066986%21sea%21CA%210%21ABX&curPageLogUid=KcMaed1KghFK&utparam-url=scene%3Asearch%7Cquery_from%3A      |
| 0.1 µF Decoupling Capacitor  |     2.43    |          | https://www.aliexpress.com/item/32973259342.html?spm=a2g0o.productlist.main.2.745060c6mVOSL3&algo_pvid=0f00e17f-19ee-4d8d-9fb7-312d358b29b6&algo_exp_id=0f00e17f-19ee-4d8d-9fb7-312d358b29b6-1&pdp_ext_f=%7B%22order%22%3A%222123%22%2C%22eval%22%3A%221%22%7D&pdp_npi=4%40dis%21CAD%213.13%212.43%21%21%2116.01%2112.43%21%402101c72a17496015899788222eda07%2166651074293%21sea%21CA%210%21ABX&curPageLogUid=grwcmkgx2m7M&utparam-url=scene%3Asearch%7Cquery_from%3A      |
| LiPo Battery                 |     1    | 8.03    | https://www.aliexpress.com/item/1005007252723935.html?spm=a2g0o.productlist.main.31.39d23b2cyRTTV5&algo_pvid=7b6f0939-255b-4789-9e2d-1e0eb49a3b33&algo_exp_id=7b6f0939-255b-4789-9e2d-1e0eb49a3b33-30&pdp_ext_f=%7B%22order%22%3A%22417%22%2C%22eval%22%3A%221%22%7D&pdp_npi=4%40dis%21CAD%2115.06%218.03%21%21%2177.11%2141.14%21%402103277f17496013600106529efb7d%2112000039955346439%21sea%21CA%210%21ABX&curPageLogUid=LuUbCz3WH4yr&utparam-url=scene%3Asearch%7Cquery_from%3A      |
| 20x1 neopixel strip	         |     1    | 11.34         |  https://www.aliexpress.com/item/1005004289391906.html?spm=a2g0o.prohttps://www.aliexpress.com/item/1005004289391906.html?spm=a2g0o.productlist.main.22.47514d9box6iEa&utparam-url=scene%3Asearch%7Cquery_from%3Apc_back_same_best&algo_pvid=3988296f-0dd2-4bec-8b73-8f63d1d35268&algo_exp_id=3988296f-0dd2-4bec-8b73-8f63d1d35268&pdp_ext_f=%7B%22order%22%3A%227482%22%7D&pdp_npi=4%40dis%21CAD%2125.62%2111.34%21%21%21131.20%2158.08%21%40210318e817496014993624942e0747%2112000038338767442%21sea%21CA%210%21ABXductlist.main.22.47514d9box6iEa&utparam-url=scene%3Asearch%7Cquery_from%3Apc_back_same_best&algo_pvid=3988296f-0dd2-4bec-8b73-8f63d1d35268&algo_exp_id=3988296f-0dd2-4bec-8b73-8f63d1d35268&pdp_ext_f=%7B%22order%22%3A%227482%22%7D&pdp_npi=4%40dis%21CAD%2125.62%2111.34%21%21%21131.20%2158.08%21%40210318e817496014993624942e0747%2112000038338767442%21sea%21CA%210%21ABX     |
| 3 volt panel mount buttons   |     1    | 9.58     | https://www.aliexpress.com/item/32811291365.html?spm=a2g0o.productlist.main.1.6fe94879HZS8la&algo_pvid=d12cfa4a-bb13-466b-ba3c-29940c8b7132&algo_exp_id=d12cfa4a-bb13-466b-ba3c-29940c8b7132-0&pdp_ext_f=%7B%22order%22%3A%222%22%2C%22eval%22%3A%221%22%7D&pdp_npi=4%40dis%21CAD%219.98%219.58%21%21%217.11%216.83%21%402101eac917496014501275389e242c%2112000032369815459%21sea%21CA%210%21ABX&curPageLogUid=aaAEn5JpLPBH&utparam-url=scene%3Asearch%7Cquery_from%3A      |
