from app import app
from models import db, Product, Seller, Price, Feedback


with app.app_context():

    # ==========================================
    # CLEAR OLD DATA
    # ==========================================
    db.create_all()


    Feedback.query.delete()
    Price.query.delete()
    Product.query.delete()
    Seller.query.delete()

    db.session.commit()




    # ==========================================
    # CREATE PRODUCTS
    # ==========================================

    iphone = Product(
        name="iPhone 15",
        category="Smartphones",
        image="/static/images/iphone15.jpg",
        description="Apple iPhone 15 with advanced camera and powerful performance."
    )


    samsung = Product(
        name="Samsung Galaxy S24",
        category="Smartphones",
        image="/static/images/samsung.jpg",
        description="Samsung Galaxy S24 with powerful performance and premium design."
    )


    oneplus = Product(
        name="OnePlus 13",
        category="Smartphones",
        image="/static/images/oneplus.jpg",
        description="OnePlus 13 with fast performance and a premium display."
    )
    cerave = Product(
        name="CeraVe Moisturizing Cream",
        category="Skincare",
        image="/static/images/CeraVe.jpg",
        description="Moisturizing cream for dry skin with ceramides and hyaluronic acid."
    )


    cetaphil = Product(
        name="Cetaphil Gentle Skin Cleanser",
        category="Skincare",
        image="/static/images/cetaphil.jpg",
        description="Gentle facial cleanser designed for everyday cleansing."
    )


    derma_co = Product(
        name="The Derma Co 2% Salicylic Acid Face Wash",
        category="Skincare",
        image="/static/images/dermaCo.jpg",
        description="Salicylic acid face wash designed for cleansing and removing excess oil."
    )

    # ==========================================
    # LAPTOP PRODUCTS
    # ==========================================

    hp_pavilion = Product(
        name="HP Pavilion 15",
        category="Laptops",
        image="/static/images/hp_pavilion.jpg",
        description="HP Pavilion 15 laptop with reliable performance for study, work and everyday use."
    )


    macbook_air = Product(
        name="Apple MacBook Air M3",
        category="Laptops",
        image="/static/images/macbook_air.jpg",
        description="Apple MacBook Air with M3 chip, lightweight design and powerful everyday performance."
    )


    asus_vivobook = Product(
        name="ASUS Vivobook 15",
        category="Laptops",
        image="/static/images/asus_vivobook.jpg",
        description="ASUS Vivobook 15 with a large display and smooth performance for work and study."
    )

# ==========================================
# AUDIO PRODUCTS
# ==========================================

    sony_ch720n = Product(
        name="Sony WH-CH720N",
        category="Audio",
        image="/static/images/sony_ch720n.jpg",
        description="Wireless noise cancelling headphones with comfortable design and long battery life."
    )


    jbl_tune_770nc = Product(
        name="JBL Tune 770NC",
        category="Audio",
        image="/static/images/jbl_tune_770nc.jpg",
        description="Wireless over-ear headphones with adaptive noise cancellation and powerful JBL sound."
    )


    boat_rockerz_450 = Product(
        name="boAt Rockerz 450",
        category="Audio",
        image="/static/images/boat_rockerz_450.jpg",
        description="Wireless on-ear headphones with deep bass, 40mm drivers and long playback."
    )

# ==========================================
# CAMERA PRODUCTS
# ==========================================

    canon_r50 = Product(
        name="Canon EOS R50",
        category="Cameras",
        image="/static/images/canon_r50.jpg",
        description="Compact mirrorless camera with high-quality photos, 4K video and fast autofocus."
    )


    sony_zv_e10 = Product(
        name="Sony ZV-E10",
        category="Cameras",
        image="/static/images/sony_zv_e10.jpg",
        description="Mirrorless vlogging camera with interchangeable lenses and excellent video features."
    )


    nikon_z50ii = Product(
        name="Nikon Z50 II",
        category="Cameras",
        image="/static/images/nikon_z50ii.jpg",
        description="Advanced mirrorless camera with powerful autofocus and excellent image quality."
    )


    db.session.add(iphone)
    db.session.add(samsung)
    db.session.add(oneplus)

    db.session.add(cerave)
    db.session.add(cetaphil)
    db.session.add(derma_co)

    db.session.add(hp_pavilion)
    db.session.add(macbook_air)
    db.session.add(asus_vivobook)
    
    db.session.add(sony_ch720n)
    db.session.add(jbl_tune_770nc)
    db.session.add(boat_rockerz_450)


    db.session.add(canon_r50)
    db.session.add( sony_zv_e10)
    db.session.add( nikon_z50ii)


    db.session.commit()


    # ==========================================
    # CREATE SELLERS
    # ==========================================

    amazon = Seller(
        name="Amazon",
        website="https://www.amazon.in"
    )


    flipkart = Seller(
        name="Flipkart",
        website="https://www.flipkart.com"
    )


    croma = Seller(
        name="Croma",
        website="https://www.croma.com"
    )


    nykaa = Seller(
        name="Nykaa",
        website="https://www.nykaa.com"
    )


    db.session.add(amazon)
    db.session.add(flipkart)
    db.session.add(croma)
    db.session.add(nykaa)

    db.session.commit()


    # ==========================================
    # IPHONE 15 PRICES
    # ==========================================

    iphone_price_1 = Price(
        product_id=iphone.id,
        seller_id=amazon.id,
        price=55999,
        availability="In Stock",
        url="https://amzn.in/d/0corf6O9"
    )


    iphone_price_2 = Price(
        product_id=iphone.id,
        seller_id=flipkart.id,
        price=52999,
        availability="In Stock",
        url="https://dl.flipkart.com/s/XYAygrNNNN"
    )


    iphone_price_3 = Price(
        product_id=iphone.id,
        seller_id=croma.id,
        price=54499,
        availability="In Stock",
        url="https://www.croma.com/apple-iphone-15-128gb-pink-/p/300679"
    )


    # ==========================================
    # SAMSUNG S24 PRICES
    # ==========================================

    samsung_price_1 = Price(
        product_id=samsung.id,
        seller_id=amazon.id,
        price=69999,
        availability="In Stock",
        url="https://amzn.in/d/0iMWeMRz"
    )


    samsung_price_2 = Price(
        product_id=samsung.id,
        seller_id=flipkart.id,
        price=67999,
        availability="In Stock",
         url="https://dl.flipkart.com/s/XYTjHONNNN"
    )


    samsung_price_3 = Price(
        product_id=samsung.id,
        seller_id=croma.id,
        price=68999,
        availability="In Stock",
        url="https://www.croma.com/samsung-galaxy-s24-5g-8gb-ram-256gb-onyx-black-/p/303849"
    )


    # ==========================================
    # ONEPLUS 13 PRICES
    # ==========================================

    oneplus_price_1 = Price(
        product_id=oneplus.id,
        seller_id=amazon.id,
        price=64999,
        availability="In Stock",
        url="https://amzn.in/d/06SBlOxg"
    )


    oneplus_price_2 = Price(
        product_id=oneplus.id,
        seller_id=flipkart.id,
        price=62999,
        availability="In Stock",
       url="https://dl.flipkart.com/s/FZjDytuuuN"
    )


    oneplus_price_3 = Price(
        product_id=oneplus.id,
        seller_id=croma.id,
        price=63999,
        availability="In Stock",
        url="https://www.croma.com/oneplus-13-5g-12gb-ram-256gb-midnight-ocean-/p/312532"
    )

    # ==========================================
    # CERAVE MOISTURIZING CREAM PRICES
    # ==========================================

    cerave_price_1 = Price(
        product_id=cerave.id,
        seller_id=amazon.id,
        price=421,
        availability="In Stock",
        url="https://amzn.in/d/0h1V5XrQ"
    )


    cerave_price_2 = Price(
        product_id=cerave.id,
        seller_id=flipkart.id,
        price=422,
        availability="In Stock",
        url="https://dl.flipkart.com/s/XQL4qrNNNN"
    )


    cerave_price_3 = Price(
        product_id=cerave.id,
        seller_id=nykaa.id,
        price=422,
        availability="In Stock",
        url="https://www.nykaa.com/cerave-moisturizing-cream-for-dry-to-very-dry-skin-with-ceramides-hyaluronic-acid/p/13169472?skuId=13169457&se=0"
    )

# ==========================================
# CETAPHIL GENTLE SKIN CLEANSER PRICES
# ==========================================

    cetaphil_price_1 = Price(
        product_id=cetaphil.id,
        seller_id=amazon.id,
        price=937,
        availability="In Stock",
        url="https://amzn.in/d/0idEjsTm"
    )


    cetaphil_price_2 = Price(
        product_id=cetaphil.id,
        seller_id=flipkart.id,
        price=418,
        availability="In Stock",
        url="https://dl.flipkart.com/s/XQlUbxNNNN"
    )


    cetaphil_price_3 = Price(
        product_id=cetaphil.id,
        seller_id=nykaa.id,
        price=418,
        availability="In Stock",
        url="https://www.nykaa.com/cetaphil-cleansing-lotion/p/22032?skuId=22031&se=0"
    )

    # ==========================================
    # THE DERMA CO 2% SALICYLIC ACID FACE WASH PRICES
    # ==========================================

    derma_co_price_1 = Price(
        product_id=derma_co.id,
        seller_id=amazon.id,
        price=239,
        availability="In Stock",
        url="https://amzn.in/d/0acrhzyT"
    )


    derma_co_price_2 = Price(
        product_id=derma_co.id,
        seller_id=flipkart.id,
        price=243,
        availability="In Stock",
        url="https://dl.flipkart.com/s/XQf9EpNNNN"
    )


    derma_co_price_3 = Price(
        product_id=derma_co.id,
        seller_id=nykaa.id,
        price=296,
        availability="In Stock",
        url="https://www.nykaa.com/the-derma-co-2percent-salicylic-acid-gel-face-wash-with-salicylic-acid-witch-hazel/p/17371002?se=0"
    )

    # ==========================================
    # HP PAVILION 15 PRICES
    # ==========================================

    hp_pavilion_price_1 = Price(
        product_id=hp_pavilion.id,
        seller_id=amazon.id,
        price=77700,
        availability="In Stock",
        url="https://amzn.in/d/0dawZZkP"
    )

    hp_pavilion_price_2 = Price(
        product_id=hp_pavilion.id,
        seller_id=flipkart.id,
        price=77507,
        availability="In Stock",
        url="https://dl.flipkart.com/s/xAlPWqNNNN"
    )

    hp_pavilion_price_3 = Price(
        product_id=hp_pavilion.id,
        seller_id=croma.id,
        price=77800,
        availability="In Stock",
        url="https://www.croma.com/hp-pavilion-15-eg3017tu-intel-core-i5-13th-gen-15-6-inch-16gb-1tb-windows-11-home-ms-office-2021-intel-iris-xe-full-hd-ips-display-fog-blue-8u5g0pa-/p/275678?srsltid=AfmBOorUP2p4tj2YRY4r9tRlYxs2ME3SriiTk8GaW-AM8j5pxj9Wv9vL"
    )


    # ==========================================
    # APPLE MACBOOK AIR M3 PRICES
    # ==========================================

    macbook_air_price_1 = Price(
        product_id=macbook_air.id,
        seller_id=amazon.id,
        price=104990,
        availability="In Stock",
        url="https://amzn.in/d/0f1qo5Rn"
    )

    macbook_air_price_2 = Price(
        product_id=macbook_air.id,
        seller_id=flipkart.id,
        price=102999,
        availability="In Stock",
        url="https://www.flipkart.com/apple-macbook-air-m3-8-gb-256-gb-ssd-macos-sonoma-mrym3hn-a/p/itmcbda9ca4a4775"
    )

    macbook_air_price_3 = Price(
        product_id=macbook_air.id,
        seller_id=croma.id,
        price=103490,
        availability="In Stock",
        url="https://www.croma.com/apple-macbook-air-2024-13-6-inch-m3-8gb-256gb-macos-sequoia-space-grey-/p/305375"
    )


    # ==========================================
    # ASUS VIVOBOOK 15 PRICES
    # ==========================================

    asus_vivobook_price_1 = Price(
        product_id=asus_vivobook.id,
        seller_id=amazon.id,
        price=52999,
        availability="In Stock",
        url="https://www.amazon.in/ASUS-Vivobook-i5-1335U-15-6-inch-X1504VA-NJ540WS/dp/B0D4TGZG1H"
    )

    asus_vivobook_price_2 = Price(
        product_id=asus_vivobook.id,
        seller_id=flipkart.id,
        price=51499,
        availability="In Stock",
        url="https://www.flipkart.com/asus-vivobook-15-intel-core-i5-13th-gen-1334u-8-gb-512-gb-ssd-windows-11-home-x1504va-nj1765ws-thin-light-laptop/p/itme9833882f198b"
    )

    asus_vivobook_price_3 = Price(
        product_id=asus_vivobook.id,
        seller_id=croma.id,
        price=51999,
        availability="In Stock",
        url="https://www.croma.com/asus-vivobook-15-x1504va-nj1765ws-intel-core-i5-13th-gen-laptop-8gb-512gb-ssd-windows-11-home-15-6-inch-full-hd-display-ms-office-2024-cool-silver-1-7-kg-/p/315069"
    )

# ==========================================
# SONY WH-CH720N PRICES
# ==========================================

    sony_ch720n_price_1 = Price(
        product_id=sony_ch720n.id,
        seller_id=amazon.id,
        price=8490,
        availability="In Stock",
        url="https://amzn.in/d/0bEBCUnZ"
    )


    sony_ch720n_price_2 = Price(
        product_id=sony_ch720n.id,
        seller_id=flipkart.id,
        price=7989,
        availability="In Stock",
        url="https://www.flipkart.com/sony-wh-ch720n-wireless-over-ear-active-noise-cancellation-headphones-mic-bluetooth/p/itm45d94d7470182?utm_source=chatgpt.com"
    )


    sony_ch720n_price_3 = Price(
        product_id=sony_ch720n.id,
        seller_id=croma.id,
        price=8299,
        availability="In Stock",
        url="https://www.croma.com/sony-wh-ch720n-bluetooth-headphone-with-mic-dual-noise-sensor-technology-over-ear-black-/p/270320?srsltid=AfmBOooF0o4hyFnvKQrBroTJNyRciLgUdkKiCm4cIifppxYZSYeBfIBG"
    )

# ==========================================
# JBL TUNE 770NC PRICES
# ==========================================

    jbl_tune_770nc_price_1 = Price(
        product_id=jbl_tune_770nc.id,
        seller_id=amazon.id,
        price=5799,
        availability="In Stock",
        url="https://amzn.in/d/03UH8yBa"
    )


    jbl_tune_770nc_price_2 = Price(
        product_id=jbl_tune_770nc.id,
        seller_id=flipkart.id,
        price=5999,
        availability="In Stock",
        url="https://dl.flipkart.com/dl/jbl-tune-770nc-active-noise-cancelling-70hr-playtime-fast-pair-multi-connect-bluetooth-gaming/p/itmdf5c83684df50?pid=ACCGQZVZWZFFPGYE&marketplace=FLIPKART&lid=LSTACCGQZVZWZFFPGYEZQYCGO&_refId=&_appId=CL"
    )


    jbl_tune_770nc_price_3 = Price(
        product_id=jbl_tune_770nc.id,
        seller_id=croma.id,
        price=6199,
        availability="In Stock",
        url="https://www.croma.com/jbl-tune-770nc-bluetooth-headphone-with-adaptive-noise-cancellation-pure-bass-sound-over-ear-black-/p/273406?srsltid=AfmBOoqf8oSV631eiUOXE0nFYXgDLil0UH77VBRqoNQjHbSonuLKNDoI"
    )

# ==========================================
# BOAT ROCKERZ 450 PRICES
# ==========================================

    boat_rockerz_450_price_1 = Price(
        product_id=boat_rockerz_450.id,
        seller_id=amazon.id,
        price=1899,
        availability="In Stock",
        url="https://www.amazon.in/Rockerz-450-Wireless-Bluetooth-Headphone/dp/B07PR1CL3S?utm_source=chatgpt.com"
    )


    boat_rockerz_450_price_2 = Price(
        product_id=boat_rockerz_450.id,
        seller_id=flipkart.id,
        price=1899,
        availability="In Stock",
        url="https://www.flipkart.com/boat-bluetooth-headset/p/itmb3a87c939ee82?utm_source=chatgpt.com"
    )


    boat_rockerz_450_price_3 = Price(
        product_id=boat_rockerz_450.id,
        seller_id=croma.id,
        price=1999,
        availability="In Stock",
        url="https://www.croma.com/boat-rockerz-450-bluetooth-headphone-with-mic-dual-connectivity-on-ear-luscious-black-/p/273418?srsltid=AfmBOorRyw3id0wZqK58GKM6-OSP_57fI4A6dz1oDipyPk1ZpS919OJC"
    )

# ==========================================
# CANON EOS R50 PRICES
# ==========================================

    canon_r50_price_1 = Price(
        product_id=canon_r50.id,
        seller_id=amazon.id,
        price=59990,
        availability="In Stock",
        url="https://www.amazon.in/Canon-Digital-Camera-RF-S18-45mm-Black/dp/B0BYZHDRN6"
    )

    canon_r50_price_2 = Price(
        product_id=canon_r50.id,
        seller_id=flipkart.id,
        price=65990,
        availability="In Stock",
        url="https://www.flipkart.com/canon-eos-r50-mirrorless-camera-body-rf-s-18-45-mm-f-4-5-6-3-stm/p/itm3bc65ea11d81b"
    )

    canon_r50_price_3 = Price(
        product_id=canon_r50.id,
        seller_id=croma.id,
        price=67990,
        availability="In Stock",
        url="https://www.croma.com/canon-eos-r50-24-2mp-mirrorless-camera-18-45-mm-lens-5-axis-electronic-image-stabilization/p/270723"
    )

# ==========================================
# SONY ZV-E10 PRICES
# ==========================================

    sony_zv_e10_price_1 = Price(
        product_id=sony_zv_e10.id,
        seller_id=amazon.id,
        price=64990,
        availability="In Stock",
        url="https://amzn.in/d/0g8trZS0"
    )

    sony_zv_e10_price_2 = Price(
        product_id=sony_zv_e10.id,
        seller_id=flipkart.id,
        price=63990,
        availability="In Stock",
        url="https://dl.flipkart.com/s/9ugsSAuuuN"
    )

    sony_zv_e10_price_3 = Price(
        product_id=sony_zv_e10.id,
        seller_id=croma.id,
        price=65990,
        availability="In Stock",
        url="https://www.croma.com/sony-alpha-zv-e10l-24-2mp-mirrorless-camera-16-50-mm-lens-23-5-x-15-6-mm-sensor-vari-angle-touch-screen-lcd-/p/244230"
    )
# ==========================================
# NIKON Z50 II PRICES
# ==========================================

    nikon_z50ii_price_1 = Price(
        product_id=nikon_z50ii.id,
        seller_id=amazon.id,
        price=91990,
        availability="In Stock",
        url="https://amzn.in/d/00pFdnvJ"
    )

    nikon_z50ii_price_2 = Price(
        product_id=nikon_z50ii.id,
        seller_id=flipkart.id,
        price=86999,
        availability="In Stock",
        url="https://www.flipkart.com/nikon-na-z-50-mirrorless-camera-body-16-50mm-lens/p/itmdc64017735260"
    )

    nikon_z50ii_price_3 = Price(
        product_id=nikon_z50ii.id,
        seller_id=croma.id,
        price=89990,
        availability="In Stock",
        url="https://www.croma.com/nikon-z-50ii-20-9mp-mirrorless-camera-16-50-mm-lens-23-5-x-15-7-mm-sensor-tft-touch-sensitive-lcd-/p/312191"
    )


    # ==========================================
    # SAVE PRICES
    # ==========================================

    db.session.add_all([
        iphone_price_1,
        iphone_price_2,
        iphone_price_3,

        samsung_price_1,
        samsung_price_2,
        samsung_price_3,

        oneplus_price_1,
        oneplus_price_2,
        oneplus_price_3,

        cerave_price_1,
        cerave_price_2,
        cerave_price_3,

        cetaphil_price_1,
        cetaphil_price_2,
        cetaphil_price_3,

        derma_co_price_1,
        derma_co_price_2,
        derma_co_price_3,

        hp_pavilion_price_1,
        hp_pavilion_price_2,
        hp_pavilion_price_3,

        macbook_air_price_1,
        macbook_air_price_2,
        macbook_air_price_3,

        asus_vivobook_price_1,
        asus_vivobook_price_2,
        asus_vivobook_price_3,

        sony_ch720n_price_1,  
        sony_ch720n_price_2,  
        sony_ch720n_price_3,

        jbl_tune_770nc_price_1,  
        jbl_tune_770nc_price_2,  
        jbl_tune_770nc_price_3, 

        boat_rockerz_450_price_1,  
        boat_rockerz_450_price_2,  
        boat_rockerz_450_price_3,

        canon_r50_price_1,
        canon_r50_price_2,
        canon_r50_price_3,

        sony_zv_e10_price_1,
        sony_zv_e10_price_2,
        sony_zv_e10_price_3,

        nikon_z50ii_price_1,
        nikon_z50ii_price_2,
        nikon_z50ii_price_3,   


    ])

    # ==========================================
    # CREATE FEEDBACK
    # ==========================================

    feedback_1 = Feedback(
        product_id=iphone.id,
        name="Rahul",
        rating=5,
        comment="Amazing phone. The camera quality and performance are excellent."
    )

    feedback_2 = Feedback(
        product_id=iphone.id,
        name="Priya",
        rating=4,
        comment="Very good phone with a beautiful display. Battery life could be better."
    )

    feedback_3 = Feedback(
        product_id=iphone.id,
        name="Arjun",
        rating=5,
        comment="Premium design and smooth performance. Really happy with my purchase."
    )

    feedback_4 = Feedback(
        product_id=iphone.id,
        name="Sneha",
        rating=4,
        comment="Great camera and fast performance. Overall, a very good smartphone."
    )

    # ==========================================
    # SAMSUNG S24 FEEDBACK
    # ==========================================

    samsung_feedback_1 = Feedback(
        product_id=samsung.id,
        name="Amit",
        rating=5,
        comment="Excellent display and camera quality. The phone feels very premium."
    )

    samsung_feedback_2 = Feedback(
        product_id=samsung.id,
        name="Neha",
        rating=4,
        comment="Very good performance and battery life. Overall a great smartphone."
    )

    samsung_feedback_3 = Feedback(
        product_id=samsung.id,
        name="Rohan",
        rating=5,
        comment="Fast, smooth and the camera is amazing. Totally worth it."
    )

    # ==========================================
    # ONEPLUS 13 FEEDBACK
    # ==========================================

    oneplus_feedback_1 = Feedback(
        product_id=oneplus.id,
        name="Karan",
        rating=5,
        comment="Super fast performance and a beautiful display. Really impressed."
    )

    oneplus_feedback_2 = Feedback(
        product_id=oneplus.id,
        name="Ananya",
        rating=4,
        comment="Great phone with excellent battery life and smooth performance."
    )

    oneplus_feedback_3 = Feedback(
        product_id=oneplus.id,
        name="Vikram",
        rating=5,
        comment="One of the best Android phones I have used. Very fast and premium."
    )

    # ==========================================
    # CERAVE FEEDBACK
    # ==========================================

    cerave_feedback_1 = Feedback(
        product_id=cerave.id,
        name="Meera",
        rating=5,
        comment="Very moisturizing and gentle on my dry skin. It feels great."
    )

    cerave_feedback_2 = Feedback(
        product_id=cerave.id,
        name="Pooja",
        rating=4,
        comment="A good moisturizer for daily use. My skin feels soft and hydrated."
    )

    cerave_feedback_3 = Feedback(
        product_id=cerave.id,
        name="Riya",
        rating=5,
        comment="Excellent cream for dry skin. I would definitely buy it again."
    )

    # ==========================================
    # CETAPHIL FEEDBACK
    # ==========================================

    cetaphil_feedback_1 = Feedback(
        product_id=cetaphil.id,
        name="Anjali",
        rating=5,
        comment="Very gentle on the skin and perfect for everyday cleansing."
    )

    cetaphil_feedback_2 = Feedback(
        product_id=cetaphil.id,
        name="Siddharth",
        rating=4,
        comment="A good cleanser that does not make my skin feel dry."
    )

    cetaphil_feedback_3 = Feedback(
        product_id=cetaphil.id,
        name="Kavya",
        rating=5,
        comment="Simple, gentle and effective. Great for sensitive skin."
    ) 

    # ==========================================
    # THE DERMA CO FEEDBACK
    # ==========================================

    derma_co_feedback_1 = Feedback(
        product_id=derma_co.id,
        name="Ishaan",
        rating=5,
        comment="Works very well for oily skin and leaves my face feeling fresh."
    )

    derma_co_feedback_2 = Feedback(
        product_id=derma_co.id,
        name="Nisha",
        rating=4,
        comment="Good face wash for daily use. It helps control excess oil."
    )

    derma_co_feedback_3 = Feedback(
        product_id=derma_co.id,
        name="Aditya",
        rating=5,
        comment="I like the texture and cleansing effect. A very good product."
    )

    # ==========================================
    # HP PAVILION 15 FEEDBACK
    # ==========================================

    hp_feedback_1 = Feedback(
        product_id=hp_pavilion.id,
        name="Rahul",
        rating=5,
        comment="Good performance for daily work and college use."
    )

    hp_feedback_2 = Feedback(
        product_id=hp_pavilion.id,
        name="Priya",
        rating=4,
        comment="The display and overall performance are very good."
    )

    hp_feedback_3 = Feedback(
        product_id=hp_pavilion.id,
        name="Arjun",
        rating=5,
        comment="A reliable laptop for study, work and everyday tasks."
    )


    # ==========================================
    # MACBOOK AIR M3 FEEDBACK
    # ==========================================

    macbook_feedback_1 = Feedback(
        product_id=macbook_air.id,
        name="Neha",
        rating=5,
        comment="Very lightweight, fast and easy to carry everywhere."
    )

    macbook_feedback_2 = Feedback(
        product_id=macbook_air.id,
        name="Rohan",
        rating=5,
        comment="Excellent battery life and very smooth performance."
    )

    macbook_feedback_3 = Feedback(
        product_id=macbook_air.id,
        name="Sneha",
        rating=4,
        comment="Premium build quality and a great display for daily use."
    )


    # ==========================================
    # ASUS VIVOBOOK 15 FEEDBACK
    # ==========================================

    asus_feedback_1 = Feedback(
        product_id=asus_vivobook.id,
        name="Karan",
        rating=4,
        comment="Good value for money and suitable for everyday work."
    )

    asus_feedback_2 = Feedback(
        product_id=asus_vivobook.id,
        name="Meera",
        rating=5,
        comment="Smooth performance and a nice display for study and work."
    )

    asus_feedback_3 = Feedback(
        product_id=asus_vivobook.id,
        name="Vikram",
        rating=4,
        comment="A good laptop with reliable performance for the price."
    )

# ==========================================
# SONY WH-CH720N REVIEWS
# ==========================================

    sony_review_1 = Feedback(
        product_id=sony_ch720n.id,
        name="Rahul",
        rating=5,
        comment="Very comfortable headphones with excellent noise cancellation. Battery life is also impressive."
    )

    sony_review_2 = Feedback(
        product_id=sony_ch720n.id,
        name="Aman",
        rating=4,
        comment="Sound quality is very good and the headphones are lightweight. Great for daily use."
    )

    sony_review_3 = Feedback(
        product_id=sony_ch720n.id,
        name="Priya",
        rating=5,
        comment="The noise cancellation works really well during travel. I am happy with the purchase."
    )

    sony_review_4 = Feedback(
       product_id=sony_ch720n.id,
       name="Neha",
       rating=4,
       comment="Good bass, clear sound and very comfortable for long listening sessions."
    )

# ==========================================
# JBL TUNE 770NC REVIEWS
# ==========================================

    jbl_review_1 = Feedback(
        product_id=jbl_tune_770nc.id,
        name="Arjun",
        rating=5,
        comment="Excellent sound quality with powerful bass. The noise cancellation is very useful."
    )

    jbl_review_2 = Feedback(
        product_id=jbl_tune_770nc.id,
        name="Karan",
        rating=4,
        comment="Good headphones for music and movies. Battery backup is also very good."
    )

    jbl_review_3 = Feedback(
        product_id=jbl_tune_770nc.id,
        name="Sneha",
        rating=5,
        comment="Comfortable fit and clear audio quality. The wireless connection is stable."
    )

    jbl_review_4 = Feedback(
        product_id=jbl_tune_770nc.id,
        name="Rohan",
        rating=4,
        comment="Nice design and balanced sound. Worth considering for the price."
    )

# ==========================================
# BOAT ROCKERZ 450 REVIEWS
# ==========================================

    boat_review_1 = Feedback(
        product_id=boat_rockerz_450.id,
        name="Vikram",
        rating=4,
        comment="Good value for money with strong bass and comfortable ear cushions."
    )

    boat_review_2 = Feedback(
        product_id=boat_rockerz_450.id,
        name="Anjali",
        rating=5,
        comment="Amazing battery life for the price. Sound quality is good for daily listening."
    )

    boat_review_3 = Feedback(
        product_id=boat_rockerz_450.id,
        name="Siddharth",
        rating=4,
        comment="The headphones are comfortable and the Bluetooth connection works smoothly."
    )

    boat_review_4 = Feedback(
        product_id=boat_rockerz_450.id,
        name="Pooja",
        rating=4,
        comment="Good bass and stylish design. Overall a very good budget wireless headphone."
    )

# ==========================================
# CANON EOS R50 REVIEWS
# ==========================================

    canon_review_1 = Feedback(
        product_id=canon_r50.id,
        name="Aditya",
        rating=5,
        comment="Excellent camera for beginners. The autofocus is fast and photos come out very sharp."
    )

    canon_review_2 = Feedback(
        product_id=canon_r50.id,
        name="Riya",
        rating=5,
        comment="Very lightweight and easy to use. The 4K video quality is also impressive."
    )

    canon_review_3 = Feedback(
        product_id=canon_r50.id,
        name="Manish",
        rating=4,
        comment="Good image quality and colours. A great choice for photography and travel."
    )

    canon_review_4 = Feedback(
        product_id=canon_r50.id,
        name="Kavya",
        rating=5,
        comment="Compact camera with excellent autofocus. I am very happy with its overall performance."
    )

# ==========================================
# SONY ZV-E10 REVIEWS
# ==========================================

    zve10_review_1 = Feedback(
        product_id=sony_zv_e10.id,
        name="Rohit",
        rating=5,
        comment="Perfect camera for vlogging. The video quality and autofocus are excellent."
    )

    zve10_review_2 = Feedback(
        product_id=sony_zv_e10.id,
        name="Ishita",
        rating=5,
        comment="Very good for creating videos. The flip screen is extremely useful for self recording."
    )

    zve10_review_3 = Feedback(
        product_id=sony_zv_e10.id,
        name="Nikhil",
        rating=4,
        comment="Great image quality and easy controls. Battery life could be slightly better."
    )

    zve10_review_4 = Feedback(
        product_id=sony_zv_e10.id,
        name="Simran",
        rating=5,
        comment="Lightweight and powerful camera. The autofocus tracks subjects very smoothly."
    )

# ==========================================
# NIKON Z50 II REVIEWS
# ==========================================

    nikon_review_1 = Feedback(
        product_id=nikon_z50ii.id,
        name="Akash",
        rating=5,
        comment="Excellent build quality and very fast autofocus. Photos are detailed and sharp."
    )

    nikon_review_2 = Feedback(
        product_id=nikon_z50ii.id,
        name="Meera",
        rating=4,
        comment="A very capable mirrorless camera with great colours and easy handling."
    )

    nikon_review_3 = Feedback(
        product_id=nikon_z50ii.id,
        name="Sahil",
        rating=5,
        comment="Great camera for both photography and video. The performance is impressive."
    )

    nikon_review_4 = Feedback(
        product_id=nikon_z50ii.id,
        name="Tanvi",
        rating=5,
        comment="Very good autofocus and image quality. Definitely worth it for serious photography."
    )

    
    # ==========================================
    # SAVE FEEDBACK
    # ==========================================

    db.session.add_all([
        # iPhone reviews
        feedback_1,
        feedback_2,
        feedback_3,
        feedback_4,

        # Samsung reviews
        samsung_feedback_1,
        samsung_feedback_2,
        samsung_feedback_3,

        # OnePlus reviews
        oneplus_feedback_1,
        oneplus_feedback_2,
        oneplus_feedback_3,

        # CeraVe reviews
        cerave_feedback_1,
        cerave_feedback_2,
        cerave_feedback_3,

        # Cetaphil reviews
        cetaphil_feedback_1,
        cetaphil_feedback_2,
        cetaphil_feedback_3,

        # The Derma Co reviews
        derma_co_feedback_1,
        derma_co_feedback_2,
        derma_co_feedback_3,
        
        # The hp reviews
        hp_feedback_1,
        hp_feedback_2,
        hp_feedback_3,
        
        # The macbook reviews
        macbook_feedback_1,
        macbook_feedback_2,
        macbook_feedback_3,
        
        # The asus reviews
        asus_feedback_1,
        asus_feedback_2,
        asus_feedback_3,
        
        # The sony reviews
        sony_review_1, 
        sony_review_2, 
        sony_review_3, 
        sony_review_4, 

        #The jbl reviews
        jbl_review_1, 
        jbl_review_2, 
        jbl_review_3, 
        jbl_review_4, 
        
        #The boat reviews
        boat_review_1, 
        boat_review_2, 
        boat_review_3, 
        boat_review_4,
        
        #The canon reviews 
        canon_review_1,
        canon_review_2,
        canon_review_3,
        canon_review_4,
        
        #The zve10 reviews
        zve10_review_1,
        zve10_review_2,
        zve10_review_3,
        zve10_review_4,
        
        #The nikon review
        nikon_review_1,
        nikon_review_2,
        nikon_review_3,
        nikon_review_4
    ])

    db.session.commit()

    
    print("===================================")
    print("Database seeded successfully!")
    print("Products added: 6")
    print("Sellers added: 4")
    print("Price records added: 18")
    print("===================================")