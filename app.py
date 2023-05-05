
import logging

from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from keyboard import btn, btn2
from keyboard import btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10

token = '6233181361:AAH233QSPkO9Bpi_YQgyYH-Jv5SK4bBp8jw'


logging.basicConfig(level=logging.INFO)

bot = Bot(token=token)
dp = Dispatcher(bot=bot)


@dp.message_handler(commands='start',)
async def Start(message:types.Message):
    await message.answer(f'Hurmatli fuqaro o\'zingizni qiziqtirgan savolni tanlash orqali unga qonuniy javob olishingiz mumkin. Savollaringizga javob olish uchun boshlash tugmasini bosing', reply_markup=btn10)
@dp.callback_query_handler(text='boshlash')
async def call(call:types.CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer(f'Quyida eng ko`p beriladigan savollarga javoblar keltirilgan 👇 Yo\'nalishlardan birini tanlash orqali savollarga javoblarni olishingiz mumkin! Agar sizning savolingizga javob topilmasa savol yozib qoldirish bo\'limida  o\'z murojaatingizni qoldirish orqali, qisqa vaqt ichida savolingizga javob olishingiz mumkin bo\'ladi.', reply_markup=btn)

# Texnik ko`rik start


@dp.callback_query_handler(text='texkorik')
async def call(call:types.CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer(f'Savollar bilan tanishib chiqing. O\'zingizni qiziqtirgan savol raqamini tanlash orqali unga javob olishingiz mumkin.')
    await call.message.answer(f'Transport vositalarin texnik ko\'rikdan o\'tkazish.\n'
                              f'1. Savol: Jismoniy shaxslarga qarashli bo\'lgan transport vositalarining texnik ko\'rigi qaysi davriylikda o\'tkaziladi? \n'
                              f'2. Savol: Jismoniy shaxslarga tegishli yengil avtomobil necha yilda texnik ko\'rikdan o\'tadi? \n'
                              f'3. Savol: Meni avtomobilimga o\'rnatilgan metan gaz baloni necha yilda sinovdan o\'tkazishim kerak? \n',  reply_markup=btn2)
@dp.callback_query_handler(text='1')
async def call(call:types.CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer(f'1-savolga javob: Vazirlar Mahkamasining 2021 yil 9 martdagi 125-son qarori bilan tasdiqlangan Transport vositalarini majburiy texnik ko\'rikdan o\'tkazish tartibi to\'g\'risida nizomning 6-bandiga asosan Jismoniy va yuridik shaxslarga tegishli boshqa transport vositalarining texnik ko\'rigi 1 yanvar — 31 dekabrda o\'tkaziladi.\n\n'
                              f'Quyida eng ko`p beriladigan savollarga javoblar keltirilgan 👇 Yo\'nalishlardan birini tanlash orqali savollarga javoblarni olishingiz mumkin! Agar sizning savolingizga javob topilmasa savol yozib qoldirish bo\'limida  o\'z murojaatingizni qoldirish orqali, qisqa vaqt ichida savolingizga javob olishingiz mumkin bo\'ladi.', reply_markup=btn)


@dp.callback_query_handler(text='2')
async def call(call:types.CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer( f'2-savolga javob: Vazirlar Mahkamasining 2021 yil 9 martdagi 125-son qarori bilan tasdiqlangan Transport vositalarini majburiy texnik ko\'rikdan o\'tkazish tartibi to\'g\'risida nizomning 5-bandining: \n'
                              f'b-kichik bandiga asosan, ishlab chiqarilganiga o\'n bir yildan o\'n to\'rt yilgacha (o\'n to\'rtinchi yili ham) bo\'lgan jismoniy shaxslarga tegishli M1 toifadagi transport vositalari (mazkur bandning “a” kichik bandida ko\'rsatilgan transport vositalaridan tashqari) — ikki yilda bir marta; \n'
                              f'v-kichik bandiga asosan, ishlab chiqarilgan vaqti aniq bo\'lmagan transport vositalari (mazkur bandning “a” kichik bandida ko\'rsatilgan transport vositalaridan tashqari), shuningdek, ishlab chiqarilganiga o\'n besh yil va undan ortiq bo\'lgan jismoniy shaxslarga tegishli M1 toifadagi transport vositalari (mazkur bandning “a” kichik bandida ko\'rsatilgan transport vositalaridan tashqari) — bir yilda bir marta.\n'
                              f'Ishlab chiqarilganiga o\'n yilgacha (o\'ninchi yili ham) bo\'lgan jismoniy shaxslarga tegishli M1 toifadagi transport vositalari (mazkur bandning “a” kichik bandida ko\'rsatilgan transport vositalaridan tashqari) texnik ko\'rikdan ixtiyoriy ravishda o‘tkaziladi.\n\n'
                               f'Quyida eng ko`p beriladigan savollarga javoblar keltirilgan 👇 Yo\'nalishlardan birini tanlash orqali savollarga javoblarni olishingiz mumkin! Agar sizning savolingizga javob topilmasa savol yozib qoldirish bo\'limida  o\'z murojaatingizni qoldirish orqali, qisqa vaqt ichida savolingizga javob olishingiz mumkin bo\'ladi.', reply_markup=btn)



@dp.callback_query_handler(text='3')
async def call(call:types.CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer(f'3-savolga javob: Vazirlar Mahkamasining 2015 yil 15 noyabrdagi 326-son qarori bilan tasdiqlangan Siqilgan tabiiy gazda, suyultirilgan neft gazida yoki dizel va gazsimon yoqilg\'i aralashmasida ishlaydigan transport vositalarining xavfsizligi to\'g\'risida umumiy texnik reglamentning 77-bandiga asosan avtomobillarga o\'rnatilgan siqilgan tabiiy gaz (metan) ballon xar uch yilda bir marta texnik sinovdan o\'tkaziladi.\n\n'
                              f'Quyida eng ko`p beriladigan savollarga javoblar keltirilgan 👇 Yo\'nalishlardan birini tanlash orqali savollarga javoblarni olishingiz mumkin! Agar sizning savolingizga javob topilmasa savol yozib qoldirish bo\'limida  o\'z murojaatingizni qoldirish orqali, qisqa vaqt ichida savolingizga javob olishingiz mumkin bo\'ladi.', reply_markup=btn)


# Texnik ko`rik end


# Haydovchilik guvohnomasi start



@dp.callback_query_handler(text='prava')
async def call(call:types.CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer(f'Savollar bilan tanishib chiqing. O\'zingizni qiziqtirgan savol raqamini tanlash orqali unga javob olishingiz mumkin.\n'
                              f'Haydovchilik guvohnomasiga oid savollar.\n'
                               f'1. Savol: Eski namunadagi haydovchilik guvohnomalarini almashtirish muddatlari qachongacha qilib belgilangan? \n'
                               f'2. Savol: O\'zbekiston Respublikasi fuqarosining xorijda olgan haydovchilik guvohnomasi respublika hududida avtomobil boshqarish huquqini beradimi? \n'
                               f'3. Savol: Eski namunadagi haydovchilik guvohnomalarini almashtirish tartibi qanaqa? Belgilangan vaqtda almashtirmagan haydovchilik guvohnomalarini almashtirishga murojaat qilinganda jarima to\'lanadimi? \n'
                               f'4. Savol: Haydovchilik huquqidan mahrum etilgan shaxslarning haydovchilik guvohnomalarini olish tartibi qanaqa? \n'
                               f'5. Savol: Yo\'qolgan haydovchilik guvohnomalarini qayta tiklash qanday tartibda amalga oshiriladi? \n', reply_markup=btn3)



@dp.callback_query_handler(text='4')
async def call(call:types.CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer(f' 1-savolga javob: O\'zbekiston Respublikasi Vazirlar Mahkamasining 2022 yil 12 apreldagi 178-son Qarorida eski namunadagi haydovchilik guvohnomalarini almashtirish muddatlari belgilangan. Jumladan: \n'
                               f'2010 yilgacha bo‘lgan davrda berilganlari — 2023 yil 31 martga qadar; \n'
                               f'2010 — 2012 yillarda berilganlari — 2023 yil 30 iyunga qadar; \n'
                               f'2013 — 2015 yillarda berilganlari — 2023 yil 30 sentyabrga qadar; \n'
                               f'2015 yildan keyin berilganlari — 2023 yil 31 dekabrga qadar muddatlarda majburiy tartibda amalga oshiriladi; \n\n'
                              f'Quyida eng ko`p beriladigan savollarga javoblar keltirilgan 👇 Yo\'nalishlardan birini tanlash orqali savollarga javoblarni olishingiz mumkin! Agar sizning savolingizga javob topilmasa savol yozib qoldirish bo\'limida  o\'z murojaatingizni qoldirish orqali, qisqa vaqt ichida savolingizga javob olishingiz mumkin bo\'ladi.', reply_markup=btn)


@dp.callback_query_handler(text='5')
async def call(call:types.CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer( f'2-savolga javob O\'zbekiston Respublikasi Vazirlar Mahkamasining 2018 yil 31 maydagi 408-sonli qarori talablariga asosan (2-ilova, 74-bandi), xalqaro haydovchilik guvohnomalari O\'zbekiston Respublikasi hududida avtomototransport vositalarini boshqarish uchun haqiqiy hisoblanadi. \n'
                               f'O\'zbekiston Respublikasi fuqarolari uchun O\'zbekiston Respublikasi hududida faqat O\'zbekiston Respublikasining milliy haydovchilik guvohnomasi avtomototransport vositalarini boshqarish uchun haqiqiy hisoblanadi. \n'
                               f'Shuningdek, (2-ilova, 76-bandi) boshqa xorijiy fuqarolar va fuqaroligi bo\'lmagan shaxslarning hamda O\'zbekiston Respublikasi fuqarolarining xorijiy davlatlarda olgan haydovchilik guvohnomalarini O\'zbekiston Respublikasining milliy haydovchilik guvohnomalariga almashtirishdan oldin ular YHXX orqali Tashqi ishlar vazirligida tekshiriladi va tekshirish natijasida haydovchilik guvohnomalari tasdiqlangan shaxslarning haydovchilik guvohnomasi, ular tibbiy ko\'rikdan o\'tib, nazariy va amaliy imtihonlarni topshirganlaridan so\'ng, O\'zbekiston Respublikasining milliy haydovchilik guvohnomalariga almashtiriladi. \n\n'
                              f'Quyida eng ko`p beriladigan savollarga javoblar keltirilgan 👇 Yo\'nalishlardan birini tanlash orqali savollarga javoblarni olishingiz mumkin! Agar sizning savolingizga javob topilmasa savol yozib qoldirish bo\'limida  o\'z murojaatingizni qoldirish orqali, qisqa vaqt ichida savolingizga javob olishingiz mumkin bo\'ladi.', reply_markup=btn)



@dp.callback_query_handler(text='6')
async def call(call:types.CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer( f'3-savolga javob: Eski namunadagi milliy haydovchilik guvohnomalari yangisiga almashtirish “Davlat xizmatlari markazi” yoki hududiy DYXXX orqali fuqarolik pasporti (yoki shaxsini tasdiqlovchi boshqa hujjat) va eski namunadagi haydovchilik guvohnomasi va ogohlantirish talonini taqdim etadi va belgilangan BHMning 70 foizi miqdorida (231 ming so‘m) to\'lovni amalga oshiradi. \n'
                               f'Davlat xizmatlari markazi tomonidan fuqarolarga qulay shart-sharoitlar yaratish maqsadida murojaatni elektron tarzda yo\'llash va tayyor xujjatni fuqarolarning yashash manziliga yetkazib berish axborot dasturi amaliyoti joriy etilib, hozirgi vaqtda to\'liq ishga tushirilgan bo\'lib, ushbu amaliyot xududiy davlat xizmatlari markazi orqali amalga oshiriladi, yaʼni murojaat qilayotgan shaxsga uning yashash manzili bo\'yicha xizmat ko\'rsatuvchi DHM xodimi tomonidan qo\'shimcha to\'lov evaziga yangi namunadagi haydovchilik guvohnomasi olib borib beriladi va shaxsan uning egasiga topshiriladi. \n'
                               f'Haydovchi belgilangan muddatlarda almashtirmagan eski namunadagi haydovchilik guvohnomasi bilan avtomobil boshqarsa O\'zbekiston Respublikasi  MJtKning 135-moddasiga asosan maʼmuriy javobgarlikka tortishga asos bo\'ladi, lekin muddati o\'tgan haydovchilik guvohnomasini almashtirishga jarima solinish ko\'zda tutilmagan.\n\n'
                              f'Quyida eng ko`p beriladigan savollarga javoblar keltirilgan 👇 Yo\'nalishlardan birini tanlash orqali savollarga javoblarni olishingiz mumkin! Agar sizning savolingizga javob topilmasa savol yozib qoldirish bo\'limida  o\'z murojaatingizni qoldirish orqali, qisqa vaqt ichida savolingizga javob olishingiz mumkin bo\'ladi.', reply_markup=btn)



@dp.callback_query_handler(text='7')
async def call(call:types.CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer(f' 4-savolga javob: O\'zbekiston Respublikasi Vazirlar Mahkamasining 2018 yil 31 maydagi 408-son qarorida avtomototransport vositalarini mast holda boshqarganligi uchun boshqarish huquqidan mahrum qilingan shaxslar, milliy haydovchilik guvohnomasini qayta olishlari uchun uchun, mahrum qilish muddatidan qatʼi nazar, maʼmuriy jazo muddati nihoyasiga yetgach, majburiy tibbiy ko\'rikdan o\'tishlari, malaka oshirish kurslarida taʼlim olishlari va nazariy hamda amaliy imtihonlarni topshirishlari shartligi belgilab berilgan. \n\n'
                              f'Quyida eng ko`p beriladigan savollarga javoblar keltirilgan 👇 Yo\'nalishlardan birini tanlash orqali savollarga javoblarni olishingiz mumkin! Agar sizning savolingizga javob topilmasa savol yozib qoldirish bo\'limida  o\'z murojaatingizni qoldirish orqali, qisqa vaqt ichida savolingizga javob olishingiz mumkin bo\'ladi.', reply_markup=btn)



@dp.callback_query_handler(text='8')
async def call(call:types.CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer(f'5-savolga javob: O\'zbekiston Respublikasi Vazirlar Mahkamasining 2018 yil 31 maydagi 408-sonli qaroriga muvofiq yo\'qolgan haydovchilik guvohnomalarini tiklash haydovchining arizasi, imtihon varaqasi, tegishli toifalardagi avtomototransport vositalarini boshqarishga yaroqliligi to\'g\'risidagi tibbiy maʼlumotnoma, imtihon varaqasi mavjud bo\'lmagan hollarda hududiy YHXBning RO\'vaIOBlarining tasdiqnomasi hamda BHMning 1 baravari miqdorida to\'lov to\'langanligini tasdiqlovchi kvitansiya asosida almashtirib beriladi.\n\n'
                              f'Quyida eng ko`p beriladigan savollarga javoblar keltirilgan 👇 Yo\'nalishlardan birini tanlash orqali savollarga javoblarni olishingiz mumkin! Agar sizning savolingizga javob topilmasa savol yozib qoldirish bo\'limida  o\'z murojaatingizni qoldirish orqali, qisqa vaqt ichida savolingizga javob olishingiz mumkin bo\'ladi.', reply_markup=btn)






# Haydovchilik guvohnomasi end




# Texpasport start




@dp.callback_query_handler(text='texpasport')
async def call(call:types.CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer(f'Savollar bilan tanishib chiqing. O\'zingizni qiziqtirgan savol raqamini tanlash orqali unga javob olishingiz mumkin.')
    await call.message.answer(f'Avtomototransport vositalarini ro\'yxatdan o\'tkazishga oid savollar. \n'
                              f'1. Savol: O\'zimni doimiy yashash joyim boshqa hududda. Lekin o\'zim Toshkent shahrida ishlayman va yashayman, Toshkent shahridan yangi avtomashina sotib oldim, Toshkent shahar IIBB YHXBdan davlat raqami olsam bo\'ladimi?\n'
                              f'2. Savol: DYHXX organlarida qanday turdagi transport vositalari ro\'yxatdan o\'tkaziladi? \n',  reply_markup=btn4)



@dp.callback_query_handler(text='9')
async def call(call:types.CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer( f'1-savolga javob: O\'zbekiston Respublikasi Vazirlar Mahkamasining 2021 yil 4 maydagi 271-son qaroriga muvofiq sotib olgan avtomototransport vositangizni xohlagan hududingizdan davlat ro\'yxatidan o\'tkazishingiz mumkin. Bunda Siz avtomashinangizga doimiy ro\'yxatga turgan hududingiz bo\'yicha belgilangan seriyali davlat raqami bilan ro\'yxatdan o\'tkazishingiz mumkin.  \n\n'
                              f'Quyida eng ko`p beriladigan savollarga javoblar keltirilgan 👇 Yo\'nalishlardan birini tanlash orqali savollarga javoblarni olishingiz mumkin! Agar sizning savolingizga javob topilmasa savol yozib qoldirish bo\'limida  o\'z murojaatingizni qoldirish orqali, qisqa vaqt ichida savolingizga javob olishingiz mumkin bo\'ladi.', reply_markup=btn)



@dp.callback_query_handler(text='10')
async def call(call:types.CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer(f'2-savolga javob: DYHXX organlarida dvigateli 50 va undan ortiq kub.sm ish hajmiga ega bo\'lgan yoki konstruksiyaviy tezligi soatiga 50 va undan ortiq kilometr bo\'lgan avtomototransport vositalari, elektrodvigatelining quvvati 4 kVt va undan ortiq yoki soatiga 40 va undan yuqori tezlikka ega bo\'lgan elektromobillar (elektromototsikllar, elektroskuterlar va boshqalar), shuningdek, tirkama va yarim tirkamalar\n\n'
                              f'Quyida eng ko`p beriladigan savollarga javoblar keltirilgan 👇 Yo\'nalishlardan birini tanlash orqali savollarga javoblarni olishingiz mumkin! Agar sizning savolingizga javob topilmasa savol yozib qoldirish bo\'limida  o\'z murojaatingizni qoldirish orqali, qisqa vaqt ichida savolingizga javob olishingiz mumkin bo\'ladi.', reply_markup=btn)





# Texpasport end




# Qayta jihoz start




@dp.callback_query_handler(text='qaytajihoz')
async def call(call:types.CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer(f'Savollar bilan tanishib chiqing. O\'zingizni qiziqtirgan savol raqamini tanlash orqali unga javob olishingiz mumkin.')
    await call.message.answer(f'Avtomototransport vositalarini qayta jihozlashga oid savollar. \n'
                              f'1. Savol: Yengil toifadagi avtotransport vositalarini oynalarini tusini o\'zgartirish (qoraytirish)  uchun bazaviy hisoblash miqdorining necha baravarida to\'lov amalga oshiriladi? \n'
                              f'2. Savol: Ishlab chiqarilganiga necha yil bo\'lgan avtomototransport vositalari qayta jixozlanishiga ruxsat etiladi? \n'
                              f'3. Savol: Avtotransport vositalarini qayta jihozlash tartibini tushuntiring? \n', reply_markup=btn5)



@dp.callback_query_handler(text='11')
async def call(call:types.CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer( f'1-savolga javob: O\'zbekiston Respublikasi Vazirlar Mahkamasining 2017 yil 1 sentyabrdagi 547-son qaroriga muvofiq, Yengil toifadagi  avtotransport vositalarini orqa va orqa yon oynalarini yorug\'lik o‘tkazuvchanligi cheklanmagan darajada o\'zgartirish (qoraytirish) ruxsatnomasiz, old yon oynalarining tusini yorug\'lik o\'tkazuvchanligi-30 foizdan kam bo\'lmagan darajada o\'zgartirish (qoraytirish) tasdiqlangan davlat standarti bo\'yicha, bazaviy hisoblash miqdorining sakkiz baravari miqdorida to\'lovni amalga oshirish lozim bo\'ladi.\n\n'
                              f'Quyida eng ko`p beriladigan savollarga javoblar keltirilgan 👇 Yo\'nalishlardan birini tanlash orqali savollarga javoblarni olishingiz mumkin! Agar sizning savolingizga javob topilmasa savol yozib qoldirish bo\'limida  o\'z murojaatingizni qoldirish orqali, qisqa vaqt ichida savolingizga javob olishingiz mumkin bo\'ladi.', reply_markup=btn)


@dp.callback_query_handler(text='12')
async def call(call:types.CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer( f'2-savolga javob: O\'zbekiston Respublikasi Vazirlar Mahkamasining  2020 yil 30 noyabrdagi 758-son qarori talablariga asosan ishlab chiqarilganiga 20 yil va undan ko\'p muddat bo\'lmagan avtomototransport vositalariga belgilangan tartibda ruxsat etiladi. \n\n'
                              f'Quyida eng ko`p beriladigan savollarga javoblar keltirilgan 👇 Yo\'nalishlardan birini tanlash orqali savollarga javoblarni olishingiz mumkin! Agar sizning savolingizga javob topilmasa savol yozib qoldirish bo\'limida  o\'z murojaatingizni qoldirish orqali, qisqa vaqt ichida savolingizga javob olishingiz mumkin bo\'ladi.', reply_markup=btn)



@dp.callback_query_handler(text='13')
async def call(call:types.CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer( f'3-savolga javob: O\'zbekiston Respublikasi Vazirlar Mahkamasining 2022-yil 22-fevral kunidagi 86-son (26-ilovasi) qaroriga muvofiq jismoniy va yuridik shaxslar tomonidan ruxsat etish xususiyatiga ega hujjatni olish uchun ariza berish “license.gov.uz” axborot tizimi, O\'zbekiston Respublikasi Yagona interaktiv davlat xizmatlari portali yoki Davlat xizmatlari markazlari orqali davlat boji (BHMning 30% foizi miqdorida) undirilgan holda yuborilishi belgilangan.  Qaror talablariga asosan 15 ish kuni mobaynida elektron shakldagi javob xatini (ruxsatnoma yoki rad etilganligi to\'g\'risida) olishingiz mumkin. Shuningdek, mazkur qaror bilan ishlab chiqarilganiga 20 yil va undan ortiq muddat o\'tgan (avtotransport vositasining ishlab chiqarilgan yilidan qatʼiy nazar, uning dvigateli va kuzovini xuddi shu rusumli avtomobilniki bilan almashtirish bundan mustasno)  avtomototransport vositalarini qayta jihozlashga yo\'l qo\'yilmasligi belgilangan. \n\n'
                              f'Quyida eng ko`p beriladigan savollarga javoblar keltirilgan 👇 Yo\'nalishlardan birini tanlash orqali savollarga javoblarni olishingiz mumkin! Agar sizning savolingizga javob topilmasa savol yozib qoldirish bo\'limida  o\'z murojaatingizni qoldirish orqali, qisqa vaqt ichida savolingizga javob olishingiz mumkin bo\'ladi.', reply_markup=btn)


# Qayta jihoz end





# Yo`l infratuzilmasi start

@dp.callback_query_handler(text='yolinfratuzilmasi')
async def call(call:types.CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer(f'Savollar bilan tanishib chiqing. O\'zingizni qiziqtirgan savol raqamini tanlash orqali unga javob olishingiz mumkin.')
    await call.message.answer(f'Yo\'l infratuzilmasini nazorat qilishga oid savollarga javoblar. \n'
                              f'1. Savol: Mahallamiz hududidan o\'tuvchi avtomobil yo\'lida svetofor  o\'rnatish uchun kimga murojaat qilishim kerak. Svetofor o\'rnatish tartibi to\'g\'risida maʼlumot bering? \n'
                              f'2. Savol: Avtomobil yo\'lini taʼmirlash va yo\'ldagi nosozliklarni bartaraf qilish uchun kimga va qayerga murojaat qilishim kerak? \n'
                              f'3. Savol: Avtomobil yo\'lida qayrilib olish joyini ochish qaysi meʼyoriy hujjat asosida amalga oshiriladi? \n'
                              f'4. Savol: Mahallamiz hududidan transport vositalari yuqori tezlikda harakatlanishi uchun mo\'ljallangan tranzit avtomobillar harakatlanadigan 6 tasmali serqatnov avtomobil yo\'li o\'tgan. Mazkur avtomobil yo\'lida piyodalar o\'tish joyi tashkil qilsa bo\'ladimi? \n'
                              f'5. Savol: Yuk avtomobillarida “Qamchiq” dovoni orqali harakatlanishim mumkinmi? \n'
                              f'6. Savol: Avtomobil yo\'llari va ko\'chalarda transport vositalari harakat tezligi pasaytirish uchun o\'rnatiladigan “Sunʼiy notekislik”lar qachon o\'rnatiladi. “Sunʼiy notekislik” o\'rnatish uchun kimga murojaat qilsam bo\'ladi? \n'
                              f'7. Savol: Katta avtomobil yo\'lida o\'rnatilgan piyodalar svetoforidan piyodalar yo\'lni kesib o\'tishga ulgurmasdan piyodalar uchun mo\'ljallangan svetofor yashil ishorasi o\'chib qizil ishorasi yonadi. Svetofor rejimlarni o\'zgartish uchun kimga murojaat qilish kerak? \n'
                              f'8. Savol: Xavfli yuklarni avtomobil transportida tashish yo\'nalishlari kimlar bilan kelishiladi? \n'
                              f'9. Savol: Bizni mahallamizdan transport vositalar yuqori tezlikda harakatlanadi. Tezlikni pasaytiruvchi yo\'l belgilarini o\'rnatish tartibi to\'g\'risida tushunchalar bering? \n'
                              f'10. Savol: Katta hajmli va og\'ir vaznli yuklarni tashish uchun qaysi tashkilot ruxsatnoma beradi? \n', reply_markup=btn6)



@dp.callback_query_handler(text='14')
async def call(call:types.CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer(f'1-savolga javob: O\'zbekiston Respublikasining “Yo\'l harakati xavfsizligi to\'g\'risida”gi Qonunining 13-moddasi 3-xatboshida yo\'llarini saqlashda ularning holati yo\'l harakati xavfsizligi sohasidagi normativ hujjatlar talablariga muvofiqligini taʼminlash bo\'yicha majburiyat mazkur yo\'llar qaysi yuridik va jismoniy shaxslar tasarrufida bo\'lsa, shu yuridik va jismoniy shaxslar zimmasiga yuklatilishi belgilab qo\'yilgan.\n\n'
                              f'Quyida eng ko`p beriladigan savollarga javoblar keltirilgan 👇 Yo\'nalishlardan birini tanlash orqali savollarga javoblarni olishingiz mumkin! Agar sizning savolingizga javob topilmasa savol yozib qoldirish bo\'limida  o\'z murojaatingizni qoldirish orqali, qisqa vaqt ichida savolingizga javob olishingiz mumkin bo\'ladi.', reply_markup=btn)

@dp.callback_query_handler(text='15')
async def call(call:types.CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer(f'2-savolga javob: O\'zbekiston Respublikasining “Avtomobil yo\'llari to\'g\'risida”gi Qonunining 15-moddasida avtomobil yo\'llarini taʼmirlash va saqlash (xizmat ko\'rsatish) mazkur yo\'llar qaysi yuridik va jismoniy shaxslar ixtiyorida bo\'lsa, o\'sha yuridik va jismoniy shaxslar tomonidan taʼminlanishi, shuningdek 16-moddasida yo\'l tashkilotlari avtomobil yo\'llarining soz holatda bo\'lishini, ulardan transport vositalari muttasil va xavfsiz o\'tishini taʼminlashi shartligi belgilab qo\'yilgan. \n'
                              f'O\'zbekiston Respublikasining “Yo\'l harakati xavfsizligi to\'g\'risida”gi Qonunining 13-moddasi 3-xatboshida yo\'llarini saqlashda ularning holati yo\'l harakati xavfsizligi sohasidagi normativ hujjatlar talablariga muvofiqligini taʼminlash bo\'yicha majburiyat mazkur yo\'llar qaysi yuridik va jismoniy shaxslar tasarrufida bo\'lsa, shu yuridik va jismoniy shaxslar zimmasiga yuklatilishi belgilab qo\'yilgan.\n\n'
                              f'Quyida eng ko`p beriladigan savollarga javoblar keltirilgan 👇 Yo\'nalishlardan birini tanlash orqali savollarga javoblarni olishingiz mumkin! Agar sizning savolingizga javob topilmasa savol yozib qoldirish bo\'limida  o\'z murojaatingizni qoldirish orqali, qisqa vaqt ichida savolingizga javob olishingiz mumkin bo\'ladi.', reply_markup=btn)

@dp.callback_query_handler(text='16')
async def call(call:types.CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer(f'3-savolga javob: O\'zbekiston Davlat arxitektura va qurilish qo\'mitasi tomonidan tasdiqlangan Avtomobil yo\'llari SHNQ 2.05.02-07 talablari asosida qayrilib olish joylari loyihalanadi va tashkil etiladi.\n\n'
                              f'Quyida eng ko`p beriladigan savollarga javoblar keltirilgan 👇 Yo\'nalishlardan birini tanlash orqali savollarga javoblarni olishingiz mumkin! Agar sizning savolingizga javob topilmasa savol yozib qoldirish bo\'limida  o\'z murojaatingizni qoldirish orqali, qisqa vaqt ichida savolingizga javob olishingiz mumkin bo\'ladi.', reply_markup=btn)

@dp.callback_query_handler(text='17')
async def call(call:types.CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer(f'4-savolga javob: O\'zbekiston Davlat arxitektura va qurilish qo\'mitasi tomonidan tasdiqlangan Avtomobil yo\'llari SHNQ 2.05.02-07 talablari asosida transport vositalari yuqori tezlikda harakatlanishi uchun mo\'ljallangan tranzit avtomobillar harakatlanadigan I va II toifali avtomobil yo\'llarda piyodalar o\'tish joylarini tashkil etishda avtomobil yo\'llari bilan bir sathda kesib o\'tilishiga yo\'l qo\'yilmadi. Ushbu joylarda piyodalar harakati jadalligiga qarab turli sathlardagi piyodalar yo\'lkalari (yer ostki va ustki) tashkil qilinadi.\n\n'
                              f'Quyida eng ko`p beriladigan savollarga javoblar keltirilgan 👇 Yo\'nalishlardan birini tanlash orqali savollarga javoblarni olishingiz mumkin! Agar sizning savolingizga javob topilmasa savol yozib qoldirish bo\'limida  o\'z murojaatingizni qoldirish orqali, qisqa vaqt ichida savolingizga javob olishingiz mumkin bo\'ladi.', reply_markup=btn)


@dp.callback_query_handler(text='18')
async def call(call:types.CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer(f'5-savolga javob: O\'zbekiston Respublikasi Vazirlar Mahkamasining 2018 yil 06 apreldagi “Qamchiq davoni orqali avtomobil transportida yuk tashishni yanada tartibga solish chora-tadbirlari to\'g\'risida” 268-sonli qarori bilan “Qamchiq” dovonida ishlab chiqarilganiga               20 yildan  oshgan yuk avtomobillari va avtomobil tirkamalarida yuk tashish taqiqlanadi.\n\n'
                              f'Quyida eng ko`p beriladigan savollarga javoblar keltirilgan 👇 Yo\'nalishlardan birini tanlash orqali savollarga javoblarni olishingiz mumkin! Agar sizning savolingizga javob topilmasa savol yozib qoldirish bo\'limida  o\'z murojaatingizni qoldirish orqali, qisqa vaqt ichida savolingizga javob olishingiz mumkin bo\'ladi.', reply_markup=btn)


@dp.callback_query_handler(text='19')
async def call(call:types.CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer(f'6-savolga javob:  “Sunʼiy notekisliklar. Umumiy texnik talablar. Qo\'llash tartibi” deb nomlangan O\'zDst 3403 O\'zbekiston Respublikasi davlat standarti ishlab chiqilgan. Shuningdek, O\'zbekiston Respublikasi Vazirlar Mahkamasining 2022 yil 12 apreldagi “Yo\'l harakati qoidalarini tasdiqlash to\'g\'risidagi” 172-sonli qarorida “Sunʼiy yo\'l notekisligi” yo\'l belgisi amaldagi yo\'l harakati qoidalariga kiritilgan. \n'
                              f'Mazkur Davlat standarti asosida sunʼiy yo\'l notekisliklari bolalar va yoshlar taʼlim-tarbiya muassasalari yonida tartibga solinmagan yer usti piyodalar yo\'lakchalaridan 10-15 metr oldinroq, avariyaviylik sabablari tahliliga ko\'ra yo\'llarning maʼlum qismlarida, ayniqsa bolalar va yoshlar taʼlim-tarbiya muassasalari oldidagi xavfli hududlar boshida, bolalar maydonchasi, jamoat dam olish joylarida, stadionlar, vokzallar, do\'kon va piyodalar jamlanadigan boshqa obyektlar oldida o\'rnatilish belgilangan. \n'
                              f'O\'zbekiston Respublikasi “Avtomobil yo\'llari to\'g\'risida”gi qonunining 10-moddasi 2-xatboshisida “Shaharlar va boshqa aholi punktlarining ko\'chalari davlat mulki bo\'lib, mahalliy davlat hokimiyati organlari ixtiyorida bo\'ladi”, 15-moddasida “Avtomobil yo\'llarini taʼmirlash va saqlash mazkur yo\'llar qaysi yuridik va jismoniy shaxslar ixtiyorida bo\'lsa, o\'sha yuridik va jismoniy shaxslar tomonidan taʼminlanishi”, shuningdek 16-moddasida “Yo\'l tashkilotlari avtomobil yo\'llarining soz holatda bo\'lishini, ulardan transport vositalari muttasil va xavfsiz o\'tishini taʼminlashi shart”-deb belgilab qo\'yilgan.  \n'
                              f'O\'zbekiston Respublikasining “Yo\'l harakati xavfsizligi to\'g\'risidagi”gi Qonunining 13-moddasi 3-xatboshida yo\'llarini saqlashda ularning holati yo\'l harakati xavfsizligi sohasidagi normativ hujjatlar talablariga muvofiqligini taʼminlash bo\'yicha majburiyat mazkur yo\'llar qaysi yuridik va jismoniy shaxslar tasarrufida bo\'lsa, shu yuridik va jismoniy shaxslar zimmasiga yuklatilishi belgilab qo‘yilgan. \n'
                              f'Ushbu qonunlar va davlat standarti talablari asosida yo\'lga egalik qiluvchi tashkilot (mahalliy hokimliklar, avtomobil yo\'llari korxona)lar tomonidan “sunʼiy notekisliklar” o\'rnatiladi hamda hududiy DYHXX bilan kelishiladi.\n\n'
                              f'Quyida eng ko`p beriladigan savollarga javoblar keltirilgan 👇 Yo\'nalishlardan birini tanlash orqali savollarga javoblarni olishingiz mumkin! Agar sizning savolingizga javob topilmasa savol yozib qoldirish bo\'limida  o\'z murojaatingizni qoldirish orqali, qisqa vaqt ichida savolingizga javob olishingiz mumkin bo\'ladi.', reply_markup=btn)


@dp.callback_query_handler(text='20')
async def call(call:types.CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer(f'7-savolga javob: O\'zbekiston Respublikasining “Yo\'l harakati xavfsizligi to\'g\'risidagi”gi Qonunining 13-moddasi 3-xatboshida yo\'llarini saqlashda ularning holati yo\'l harakati xavfsizligi sohasidagi normativ hujjatlar talablariga muvofiqligini taʼminlash bo\'yicha majburiyat mazkur yo\'llar qaysi yuridik va jismoniy shaxslar tasarrufida bo\'lsa, shu yuridik va jismoniy shaxslar zimmasiga yuklatilishi belgilab qo\'yilgan. \n'
                              f'Ushbu qonun talablari asosida yo\'lga egalik qiluvchi tashkilotga hamda hududiy DYHXXga murojaat qilinadi. Murojaatda svetofor o\'rnatish manzili va joyi(lokatsiyasi) ko\'rsatiladi. Masʼul xodimlar tomonidan svetofor rejimlari qo\'shimcha o\'rganilib, davlat standarti talablariga muvofiq yoki muvofiq emasligi bo\'yicha chiqarilgan xulosalar asosida svetofor rejimi o\'zgartiriladi.\n\n'
                              f'Quyida eng ko`p beriladigan savollarga javoblar keltirilgan 👇 Yo\'nalishlardan birini tanlash orqali savollarga javoblarni olishingiz mumkin! Agar sizning savolingizga javob topilmasa savol yozib qoldirish bo\'limida  o\'z murojaatingizni qoldirish orqali, qisqa vaqt ichida savolingizga javob olishingiz mumkin bo\'ladi.', reply_markup=btn)


@dp.callback_query_handler(text='21')
async def call(call:types.CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer(f'8-savolga javob: O\'zbekiston Respublikasi Vazirlar Mahkamasining 35-sonli qarori 56-bandida Xavfli yuklarni transportda tashish yo\'nalishlarini kelishish uchun yukni tashuvchi tashish boshlanishidan kamida o\'n kun oldin hududi bo\'ylab xavfli yukni tashish mo\'ljallanayotgan hududiy yo\'l harakati xavfsizligi boshqarmasiga quyidagi hujjatlarni taqdim etishi shartligi belgilangan: \n'
                              f'a) belgilangan shakl bo\'yicha tashishning ishlab chiqilgan yo\'nalishi uch nusxada; \n'
                              f'b) avtotransport vositasini xavfli yuklarni tashishga qo\'yish to\'g\'risidagi guvohnoma; \n'
                              f'v) alohida xavfli yuklar uchun qo\'shimcha ravishda yukni jo\'natuvchi (yukni oluvchi) tomonidan taqdim etilgan xavfli yukni tashishga maxsus yo\'riqnoma;\n'
                              f'g) O\'zbekiston Respublikasi Sanoat xavfsizligi davlat qo\'mitasining xavfli yuklarni tashish uchun sig\'im (konteynerlar, sisternalar, konteyner-sisternalar va hokazolar)ning yaroqliligi to\'g\'risidagi xulosasi; \b'
                              f'd) avtotransport haydovchisi xavfli yuklarni tashishga qo\'yilishi to\'g\'risidagi guvohnoma; \n'
                              f'Mazkur hujjatlar asosida xalqaro yo\'nalishlarda xavfli yuklarni tashish O\'zbekiston Respublikasi  IIV JXD YHXX bilan mahalliy yo\'nalishlarda Qoraqalpog\'iston Respublikasi Ichki ishlar vazirligi, Toshkent shahri va Toshkent viloyati ichki ishlar bosh boshqarmalari, viloyatlar ichki ishlar boshqarmalarining Jamoat xavfsizligi xizmati Yo\'l harakati xavfsizligi boshqarmalari bilan yo\'nalish sxemalari kelishiladi.\n\n'
                              f'Quyida eng ko`p beriladigan savollarga javoblar keltirilgan 👇 Yo\'nalishlardan birini tanlash orqali savollarga javoblarni olishingiz mumkin! Agar sizning savolingizga javob topilmasa savol yozib qoldirish bo\'limida  o\'z murojaatingizni qoldirish orqali, qisqa vaqt ichida savolingizga javob olishingiz mumkin bo\'ladi.', reply_markup=btn)

@dp.callback_query_handler(text='22')
async def call(call:types.CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer(f'9-savolga javob: O\'zbekiston Respublikasi Vazirlar Mahkamasining 2022 yil 12 apreldagi 172-son qarorining 78-bandida “Aholi punktlarida transport vositalarining tezligini soatiga 70 kilometrdan, tegishli yo\'l belgilari o\'rnatilgan maktab va maktabgacha taʼlim tashkilotlariga yetmasdan va o\'tib ketib 300 metrdan kam masofada soatiga 30 kilometrdan, turar joy dahalari va yondosh hududlarda (uy-joy binolari orasidagi yer uchastkasida) esa soatiga 20 kilometrdan oshirmasdan harakatlanishga ruxsat etiladi. Nukus va Toshkent shaharlarida, viloyatlar va tumanlarning markazlarida, shuningdek shaharlar hududlarida transport vositalarining tezligini soatiga 60 kilometrdan oshirmasdan harakatlanishga ruxsat etiladi.”, 80-bandi 5-xatboshida “Qoraqalpog\'iston Respublikasi Vazirlar Kengashi, Toshkent shahar va viloyatlar hokimliklari DYHXX bilan kelishilgan holda, yo\'l sharoitlari yuqori va kichik tezlikda xavfsiz harakatlanishni taʼminlaydigan hollarda, yo\'llarning ayrim qismlari yoki harakatlanish tasmalarida harakatlanish tezligini oshirishga yoki kamaytirishga (tegishli yo\'l belgilari o\'rnatib) ruxsat beradi.”-deb belgilab berilgan.\n\n'
                              f'Quyida eng ko`p beriladigan savollarga javoblar keltirilgan 👇 Yo\'nalishlardan birini tanlash orqali savollarga javoblarni olishingiz mumkin! Agar sizning savolingizga javob topilmasa savol yozib qoldirish bo\'limida  o\'z murojaatingizni qoldirish orqali, qisqa vaqt ichida savolingizga javob olishingiz mumkin bo\'ladi.', reply_markup=btn)

@dp.callback_query_handler(text='23')
async def call(call:types.CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer(f'10-savolga javob: O\'zbekiston Respublikasi Vazirlar Mahkamasining 2011 yil 26 dekabrdagi 342-son qaroriga 2-ilova «Katta hajmli va og\'ir vaznli yuklarni avtomobil transportida tashishda harakat xavfsizligini taʼminlash qoidalari»ning 9-bandi asosida “Yuk tashuvchi yoki yuk jo\'natuvchi jismoniy yoki yuridik shaxs (yoki ularning vakillari) maxsus ruxsatnoma va yo\'nalish chizmasini olish uchun yo\'lga egalik qiluvchi yuridik shaxslarga tashuvni amalga oshirishdan oldin transport vositasining rusumi, turi, davlat raqami belgilari va yukning o\'lchamlari, haydovchi va yuk tashishga masʼul bo\'lgan xodimlarning ismi, familiyasi, otasining ismi ko\'rsatilgan maʼlumotlarni my.gov.uz portali orqali murojaat qoldiradi. “Amaldagi meʼyoriy hujjatlardagi talablarga muvofiq yo\'lga egalik qiluvchi yuridik shaxslar tomonidan yuk tashishga maxsus ruxsatnoma va harakatlanish yo\'nalishi aniq belgilangan yo\'nalish chizmasi beriladi. \n'
                              f'Mazkur hujjatlar asosida xalqaro yo\'nalishlarda katta va og\'ir vaznli yuklarni tashish O\'zbekiston Respublikasi  IIV JXD YHXX tomonidan  mahalliy yo\'nalishlarda Qoraqalpog\'iston Respublikasi Ichki ishlar vazirligi, Toshkent shahri va Toshkent viloyati ichki ishlar bosh boshqarmalari, viloyatlar ichki ishlar boshqarmalarining Jamoat xavfsizligi xizmati Yo\'l harakati xavfsizligi boshqarmalari tomonidan yo\'nalish sxemalari kelishiladi.\n\n'
                              f'Quyida eng ko`p beriladigan savollarga javoblar keltirilgan 👇 Yo\'nalishlardan birini tanlash orqali savollarga javoblarni olishingiz mumkin! Agar sizning savolingizga javob topilmasa savol yozib qoldirish bo\'limida  o\'z murojaatingizni qoldirish orqali, qisqa vaqt ichida savolingizga javob olishingiz mumkin bo\'ladi.', reply_markup=btn)



# Yo`l infratuzilmasi end




# Qidruv start



@dp.callback_query_handler(text='qidiruv')
async def call(call:types.CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer(f'Savollar bilan tanishib chiqing. O\'zingizni qiziqtirgan savol raqamini tanlash orqali unga javob olishingiz mumkin.')
    await call.message.answer(f'Transport vositalariga nisbatan qidiruv eʼlon qilishga oid savollar. \n'
                              f'Savol: Transport vositalariga qanday hollarda qidiruv eʼlon qilinadi. \n', reply_markup=btn7)




@dp.callback_query_handler(text='24')
async def call(call:types.CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer(f'Savollar bilan tanishib chiqing. O\'zingizni qiziqtirgan savol raqamini tanlash orqali unga javob olishingiz mumkin.')
    await call.message.answer(f'1-savolga javob: Transport vositasini boshqargan haydovchi tomonidan qoidabuzarlik sodir etilgan holati YPX xodimi tomonidan aniqlanganda, maʼmuriy javobgarlik to\'g\'risidagi kodeksning tegishli moddalariga asosan bayonnoma rasmiylashtirilib avtomashina jarima maydoniga joylashtiriladi, boshqa holatlarda O\'zbekiston Respublikasi amaldagi qonunchiligi talablari asosida transport vositalariga nisbatan qidiruv eʼlon qilish, ushlash va jarima maydoniga joylashtirish vakolatli organlarining alohida topshiriqlari hamda sud idoralarining qaror, ajrim, hukmlari asosida amalga oshiriladi.\n\n'
                              f'Quyida eng ko`p beriladigan savollarga javoblar keltirilgan 👇 Yo\'nalishlardan birini tanlash orqali savollarga javoblarni olishingiz mumkin! Agar sizning savolingizga javob topilmasa savol yozib qoldirish bo\'limida  o\'z murojaatingizni qoldirish orqali, qisqa vaqt ichida savolingizga javob olishingiz mumkin bo\'ladi.', reply_markup=btn)


# Qidruv end



# Jarimalar start

@dp.callback_query_handler(text='jarimalar')
async def call(call:types.CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer(f'Transport vositalariga nisbatan belgilanadigan jarimalarga oid savollarga javoblar. \n'
                              f'1. Savol: Transport vositamda tezlikni meʼyoridan oshirgan holda harakatlanganligim uchun menga 1.650.000 so\'m miqdordagi jarima keldi, biroq jarimani to\'lashga imkonim yo\'q 4 nafar voyaga yetmagan farzandim bor, Sizdan jarima miqdorini kamaytirib berishda amaliy yordam berishingizni so\'rayman. \n'
                              f'2. Savol: Chiqarilgan jarima qarori xususida shikoyat berish muddati qanday? \n'
                              f'3. Savol: Men transport  vositamni notarial idora orqali oldi-sotdi qilayotgan vaqtimda, transport vositamda qarzdorlik borligini bildim, lekin bunga qadar menga pochta orqali yashash manzilimga hech qanday jarima qarori kelmagan, agarda men jarima qarorini olganimda jarima imtiyozli to\'lov davrida to\'lab yuborgan bo\'lar edim, ushbu holatda jarima qarori yuzasidan imtiyozli davr muddati qayta tiklanadimi?   \n'
                              f'4. Savol: Men otamga tegishli transport vositasida tezlikni meʼyoridan oshirgan holda harakatlanganligim uchun maxsus avtomatlashtirilgan foto va video qayd etish moslamalari orqali  otamning nomiga jarima kelgan. Ushbu jarimani qanday qilib meni nomimga qayta rasmiylashtirish mumkin? \n'
                              f'5. Savol: Men chorrahada svetoforning qizil ishorasiga bo\'ysungan holda to\'xtab turgan vaqtimda, ortimdan  maxsus xizmat avtomashinasi (tez tibbiy yordam transport vositasi) yo\'l berishimni talab qildi, men transport vositasiga yo\'l berish maqsadida sidirg\'a chiziqni bosib o\'ng tomonga harakatlanishga majbur bo\'ldim, ushbu holatda menga jarima kelsa men jarimani to\'lashdan ozod etilishim mumkinmi? \n', reply_markup=btn8)

@dp.callback_query_handler(text='25')
async def call(call:types.CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer(f'1-savolga javob: O\'zbekiston Respublikasi MJtKning 321-moddasi 1-qismi 4 bandida jazo chorasini kuchaytirmagan holda uni maʼmuriy huquqbuzarlik uchun javobgarlik to\'g\'risidagi normativ hujjatda nazarda tutilgan doirada o\'zgartirish sud organlarining vakolat doirasiga kirishligi sababli jarima miqdorini kamaytirish yuzasidan hududiy Jinoyat ishlari bo\'yicha sudlarga murojaat etishingiz tavsiya etiladi.\n\n'
                              f'Quyida eng ko`p beriladigan savollarga javoblar keltirilgan 👇 Yo\'nalishlardan birini tanlash orqali savollarga javoblarni olishingiz mumkin! Agar sizning savolingizga javob topilmasa savol yozib qoldirish bo\'limida  o\'z murojaatingizni qoldirish orqali, qisqa vaqt ichida savolingizga javob olishingiz mumkin bo\'ladi.', reply_markup=btn)


@dp.callback_query_handler(text='26')
async def call(call:types.CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer(f'2-savolga javob: Chiqarilgan qaror xususida shikoyat berish tartibi O\'zbekiston Respublikasi MJtKning 316-moddasida ko\'rsatilgan bo\'lib, unda “Maʼmuriy huquqbuzarlik to\'g\'risidagi ish yuzasidan chiqarilgan qaror xususida shu qarorning nusxasi olingan kundan eʼtiboran o\'n kun ichida shikoyat berilishi mumkin, bundan sud qarori mustasno. Mazkur muddat uzrli sabablar bilan o\'tkazilib yuborilgan taqdirda, bu muddat shikoyatni ko\'rib chiqishga vakolatli organ (mansabdor shaxs) tomonidan qayta tiklanishi mumkin” deb ko\'rsatib o\'tilgan.\n\n'
                              f'Quyida eng ko`p beriladigan savollarga javoblar keltirilgan 👇 Yo\'nalishlardan birini tanlash orqali savollarga javoblarni olishingiz mumkin! Agar sizning savolingizga javob topilmasa savol yozib qoldirish bo\'limida  o\'z murojaatingizni qoldirish orqali, qisqa vaqt ichida savolingizga javob olishingiz mumkin bo\'ladi.', reply_markup=btn)

@dp.callback_query_handler(text='27')
async def call(call:types.CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer(f'3-savolga javob: Hurmatli fuqaro sizni bu mavzuda berayotgan savolingiz o\'rinli va dolzarb, sizga agarda jarima qarori o\'z vaqtida pochta orqali yetkazilmagan bo\'lsa, yashash manzilingiz bo\'yicha hududiy pochta tarmog\'iga murojaat qilib, nima sababdan jarimani yetkazib berilmaganligi yuzasidan maʼlumot olish lozim bo\'ladi misol uchun: uyingizda hech kim bo\'lmaganligi, siz ushbu manzildan boshqa hududga ko\'chib o\'tganligingiz yoki shunga o\'xshash boshqa holatlar bo\'yicha maʼlumotnoma taqdim qilingandan so\'ng, ushbu maʼlumotnoma bilan yashash manzilingiz bo\'yicha O\'zbekiston Respublikasi MJtKning 315-moddasida “Maʼmuriy huquqbuzarlik to\'g\'risidagi ish yuzasidan qaror ustidan yuqori turuvchi organga (mansabdor shaxsga) yoki jinoyat ishlari bo\'yicha tuman (shahar) sudiga, jinoyat ishlari bo\'yicha tuman (shahar) sudining qarori ustidan esa apellyatsiya instansiyasi sudiga shikoyat berilishi mumkin. Iqtisodiy sudning qarori ustidan O\'zbekiston Respublikasining Iqtisodiy protsessual kodeksida belgilangan tartibda, fuqarolik ishlari bo\'yicha sudning qarori ustidan esa O\'zbekiston Respublikasining Fuqarolik protsessual kodeksida belgilangan tartibda shikoyat berilishi mumkin.” ko\'rsatib o\'tilgan talablardan kelib chiqib, Jinoyat ishlari bo\'yicha sudlarga murojaat qilishingiz mumkin,shuningdek MJtKning 3091-moddasida “Jarima solish to\'g\'risidagi qarorning ko\'chirma nusxasi maxsus avtomatlashtirilgan foto va video qayd etish texnika vositalari qo\'llanilgan holda olingan materiallar ilova qilinib, elektron hujjatni qog\'ozdagi hujjatga aylantirish yo\'li bilan tayyorlanadi hamda mazkur qaror chiqarilgan kundan eʼtiboran uch kun ichida buyurtma pochta jo\'natmasi tarzida huquqbuzarga yuboriladi” deb ko\'rsatib o\'tilgan.\n\n'
                              f'Quyida eng ko`p beriladigan savollarga javoblar keltirilgan 👇 Yo\'nalishlardan birini tanlash orqali savollarga javoblarni olishingiz mumkin! Agar sizning savolingizga javob topilmasa savol yozib qoldirish bo\'limida  o\'z murojaatingizni qoldirish orqali, qisqa vaqt ichida savolingizga javob olishingiz mumkin bo\'ladi.', reply_markup=btn)

@dp.callback_query_handler(text='28')
async def call(call:types.CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer(f'4-savolga javob: Agarda siz (o\'zingiz tegishli bo\'lmagan )  transport vositasini boshqarib qoidabuzarlik sodir etgan bo\'lsangiz, O\'zbekiston Respublikasi MJtKning 315-moddasi tartibida hududiy YHXBga murojaat qilishingiz mumkin, agarda shikoyat qilish muddati uzrli sabablarga ko\ra o\'tib ketgan bo\'lsa, yashash manzilingiz bo\'yicha Jinoyat ishlari bo\'yicha sudlarga murojaat qilib, shikoyat qilish muddati tiklanishi yoki murojaat qilgan sud idorasi orqali qarorni qayta qaratish mumkin.\n\n'
                              f'Quyida eng ko`p beriladigan savollarga javoblar keltirilgan 👇 Yo\'nalishlardan birini tanlash orqali savollarga javoblarni olishingiz mumkin! Agar sizning savolingizga javob topilmasa savol yozib qoldirish bo\'limida  o\'z murojaatingizni qoldirish orqali, qisqa vaqt ichida savolingizga javob olishingiz mumkin bo\'ladi.', reply_markup=btn)
@dp.callback_query_handler(text='29')
async def call(call:types.CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer(f'5-savolga javob: O\'zbekiston Respublikasi MJtKning 171-moddasining 6-qismida  “Tezkor va maxsus xizmatlarning ko\'k yoki qizil yoxud ko\'k va qizil rangli yaltiroq mayoqchani yoqqan holda hamda maxsus tovushli signallar bilan yaqinlashib kelayotgan transport vositalariga ularning to\'siqsiz o\'tib ketishi uchun yo\'l bergan transport vositalari haydovchilari tomonidan sodir etilgan maʼmuriy huquqbuzarliklar foto va video qayd etishning maxsus avtomatlashtirilgan texnik vositalari orqali qayd etilgan taqdirda, haydovchilarning maʼmuriy huquqbuzarligi oxirgi zarurat holatlarda sodir etilgan deb topiladi va maʼmuriy ish ushbu Kodeksning 271-moddasiga muvofiq tugatiladi” deb ko\'rsatib o\'tilganligi sababli mazkur holatda jarima belgilangan tartibda bekor qilinadi.\n\n'
                              f'Quyida eng ko`p beriladigan savollarga javoblar keltirilgan 👇 Yo\'nalishlardan birini tanlash orqali savollarga javoblarni olishingiz mumkin! Agar sizning savolingizga javob topilmasa savol yozib qoldirish bo\'limida  o\'z murojaatingizni qoldirish orqali, qisqa vaqt ichida savolingizga javob olishingiz mumkin bo\'ladi.', reply_markup=btn)


# Jarimalar end



# Ypx Hodimi start
@dp.callback_query_handler(text='ypxhodimi')
async def call(call:types.CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer(f'Savollar bilan tanishib chiqing. O\'zingizni qiziqtirgan savol raqamini tanlash orqali unga javob olishingiz mumkin.')
    await call.message.answer(f'Yo\' harakati xavfsizligi xizmati inspektori bilan bo\'ladigan xolatlarga oid savollarga javoblar. \n'
                              f'1. Savol: Transport vositamni YPX inspektori o\'zi boshqarib jarima maydoniga olib borishi mumkinmi ? \n'
                              f'2. Savol: Transport vositalarining yorituvchi chiroqlariga, yaʼni faralariga “LED” lampochkalar o\'rnatgan bo\'lsa YPX xodimi maʼmuriy bayonnoma rasmiylashtirishga haqqi bormi ?\n'
                              f'3. Savol: YPX xodimi haydovchiga kuch ishlatib avtomashinasiga mindirishi mumkinmi? \n'
                              f'4. Savol: YPX xodimini bodi-kamerasi bo\'lmasa to\'xtatishga haqqi bormi? \n'
                              f'5. Savol: YPX xodimiga to\'xtamagan haydovchilarni quvishga haqqi bormi? \n'
                              f'6. Saovl: YPX xodimi haydovchilarni qaysi hollarda to\'xtatishi mumkin? \n'
                              f'7. Savol: Haydovchining ID-kartasi yoki biometrik pasportini taqdim etganida, uning hujjatlari YPX inspektorining planshetida ko\'rinmasa bayonnoma tuzishga haqqi bormi?\n'
                              f'8. Savol: Haydovchi mast holda bo\'a turib, tibbiy tekshiruvdan yoki alkotesterdan o\'tishdan bosh tortgan taqdirda YPX xodimi unga bayonnoma tuzishi mumkinmi? \n', reply_markup=btn9)

@dp.callback_query_handler(text='30')
async def call(call:types.CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer(f'1-savolga javob: O\'zbekiston Respublikasining 2016-yil 16-sentyabrdagi “Ichki ishlar organlari to\'g\'risida”gi O\'RQ-407-son Qonunning 3-bob (Ichki ishlar organlarining majburiyatlari va huquqlari), 17-moddasi, 25-26-xatboshilari (zarur bo\'lgan hollarda, transport vositalarini to\'xtatish hamda uni boshqarish va undan foydalanish huquqini beruvchi hujjatlarni, transport vositasiga, shuningdek tashilayotgan yuklarga oid hujjatlarni tekshirish, haydovchi yoki yukni kuzatib borayotgan shaxs bilan birgalikda transport vositasini va yuklarni tashqi ko\'zdan kechirish; qonun hujjatlarida nazarda tutilgan hollarda va tartibda transport vositalarini va shaxslarni ushlashni, ko\'rikdan o\'tkazishni amalga oshirish, shaxslarni transport vositasini boshqarishdan chetlashtirish, transport vositasini boshqarish huquqini beruvchi hujjatlarni olib qo\'yish, shuningdek transport vositalarini saqlab turiladigan joyga qo\'yish uchun olib borish;)- huquqiga ega ekanligi ko\'rsatib o\'tilgan. Shuningdek, amaldagi “Yo\'l harakati qoidalari”ning 7-bandi talablari asosida transport vositasini boshqarishi mumkinligini maʼlum qilamiz.\n\n'
                              f'Quyida eng ko`p beriladigan savollarga javoblar keltirilgan 👇 Yo\'nalishlardan birini tanlash orqali savollarga javoblarni olishingiz mumkin! Agar sizning savolingizga javob topilmasa savol yozib qoldirish bo\'limida  o\'z murojaatingizni qoldirish orqali, qisqa vaqt ichida savolingizga javob olishingiz mumkin bo\'ladi.', reply_markup=btn)


@dp.callback_query_handler(text='31')
async def call(call:types.CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer(f'2-savolga javob: O\'zbekiston Respublikasi Vazirlar Mahkamasining 2022 yil 12 apreldagi 172-son qaroriga 3-ilova, 3.4-bandi (Yoritish asboblarida nur sochuvchisi bo\'lmasa yoxud tegishli yorug\'lik asboblari turiga mos bo\'lmagan nur sochuvchi va ishlab chiqaruvchi korxona tomonidan ko\'zda tutilmagan lampalardan foydalanilgan bo\'lsa)da hamda O\'zbekiston Respublikasi MJtKning 127-moddasi (Transport vositalarining tovush chiqaruvchi, yorituvchi va boshqa qurilmalaridan foydalanish, ularni o\'rnatish qoidalarini buzish)da nazarda tutilgan huquqbuzarlik yuzasidan haydovchilarga nisbatan belgilangan tartibda maʼmuriy choralar ko\'riladi.\n\n'
                              f'Quyida eng ko`p beriladigan savollarga javoblar keltirilgan 👇 Yo\'nalishlardan birini tanlash orqali savollarga javoblarni olishingiz mumkin! Agar sizning savolingizga javob topilmasa savol yozib qoldirish bo\'limida  o\'z murojaatingizni qoldirish orqali, qisqa vaqt ichida savolingizga javob olishingiz mumkin bo\'ladi.', reply_markup=btn)

@dp.callback_query_handler(text='32')
async def call(call:types.CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer(f'3-savolga javob: O\'zbekiston Respublikasi Vazirlar Mahkamasining  2018 yil 1 dekabrdagi 975-son qarorining 12-bandi “ YPX xodimi o\'z xizmat vazifalarini bajarishda qonun hujjatlarida nazarda tutilgan asoslar mavjud bo‘lganda, jismoniy kuch ishlatish, maxsus vositalarni va o\'qotar qurolni qo\'llash huquqlarga ega” talablari asosida haydovchi va fuqarolarga kuch ishlatishi va maxsus vositalardan foydalanishi mumkin.\n\n'
                              f'Quyida eng ko`p beriladigan savollarga javoblar keltirilgan 👇 Yo\'nalishlardan birini tanlash orqali savollarga javoblarni olishingiz mumkin! Agar sizning savolingizga javob topilmasa savol yozib qoldirish bo\'limida  o\'z murojaatingizni qoldirish orqali, qisqa vaqt ichida savolingizga javob olishingiz mumkin bo\'ladi.', reply_markup=btn)


@dp.callback_query_handler(text='33')
async def call(call:types.CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer(f'4-savolga javob: O\'zbekiston Respublikasi Vazirlar Mahkamasining 2018 yil 1 dekabrdagi 975-son qarorining 14-bandida “YPX xodimi o\'z xizmat vazifalarini bajarishda mobil videokameradan foydalangan holda oshkora olib borishi” talablariga asosan xizmatini bodi-kamera orqali olib borishi kerak.\n\n'
                              f'Quyida eng ko`p beriladigan savollarga javoblar keltirilgan 👇 Yo\'nalishlardan birini tanlash orqali savollarga javoblarni olishingiz mumkin! Agar sizning savolingizga javob topilmasa savol yozib qoldirish bo\'limida  o\'z murojaatingizni qoldirish orqali, qisqa vaqt ichida savolingizga javob olishingiz mumkin bo\'ladi.', reply_markup=btn)


@dp.callback_query_handler(text='34')
async def call(call:types.CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer(f'5-savolga javob: O\'zbekiston Respublikasi Vazirlar Mahkamasining 2018 yil 1 dekabrdagi 975-son qarorining 2-bandi “Maʼmuriy huquqbuzarlik sodir etgan shaxslar o\'z harakatlari bilan boshqa harakat qatnashchilari hayoti (sog\'lig\'i)ga xavf solayotgan transport vositasi haydovchisi YPX xodimining to\'xtash to\'g\'risidagi qonuniy talabini bajarmaganda to\'xtatish maqsadida orqasidan borish” talablari asosida YPX xodimi transport vositalarini orqasidan kuzatib borishi mumkin.\n\n'
                              f'Quyida eng ko`p beriladigan savollarga javoblar keltirilgan 👇 Yo\'nalishlardan birini tanlash orqali savollarga javoblarni olishingiz mumkin! Agar sizning savolingizga javob topilmasa savol yozib qoldirish bo\'limida  o\'z murojaatingizni qoldirish orqali, qisqa vaqt ichida savolingizga javob olishingiz mumkin bo\'ladi.', reply_markup=btn)


@dp.callback_query_handler(text='35')
async def call(call:types.CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer(f'6-savolga javob: O\'zbekiston Respublikasi Vazirlar Mahkamasining 2018 yil 1 dekabrdagi 975-son qarorining 6-bandi “Haydovchi tomonidan yo\'l harakati qoidalarining buzilishi vizual kuzatuvda aniqlanganda yoki maxsus moslama yordamida qayd qilinganda” talablari asosida to\'xtatishi mumkin.\n\n'
                              f'Quyida eng ko`p beriladigan savollarga javoblar keltirilgan 👇 Yo\'nalishlardan birini tanlash orqali savollarga javoblarni olishingiz mumkin! Agar sizning savolingizga javob topilmasa savol yozib qoldirish bo\'limida  o\'z murojaatingizni qoldirish orqali, qisqa vaqt ichida savolingizga javob olishingiz mumkin bo\'ladi.', reply_markup=btn)

@dp.callback_query_handler(text='36')
async def call(call:types.CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer(f'7-savolga javob: O\'zbekiston Respublikasi Vazirlar Mahkamasining 2022 yil 12 apreldagi 172-son “Yo\'l harakati qoidalari to\'g\'risida”gi qarorning 7-bandi (O\'zbekiston Respublikasi ichki ishlar organlari yoxud konsullik muassasalari tomonidan berilgan biometrik pasporti yoki identifikatsiyalovchi ID-kartasi yonida bo\'gan haydovchilarning, haydovchilik guvohnomasi, transport vositasini ro\'yxatdan o\'tkazganlik to\'g\'risidagi guvohnomasi,transport vositasiga egalik qilish, egasi yo\'qligida undan foydalanish yoki uni tasarruf etish huquqini tasdiqlovchi hujjatlari, avtotransport vositasi oynalarining tusini o\'zgartirishga (qoraytirishga) ruxsatnomasi, transport vositasining texnik ko\'rikdan o\'tganligi to\'g\'risidagi maʼlumotni, transport vositalari egalarining fuqarolik javobgarligini majburiy sug\'urta qilish bo\'yicha sug‘urta polisi planshet orqali tekshiriladi (planshetda aniqlash imkoni bo\'lmagan hamda favqulodda holatlar bundan mustasno)da DYHXX xodimlari tomonidan planshet orqali tekshiriladi deb belgilangan.\n\n'
                              f'Quyida eng ko`p beriladigan savollarga javoblar keltirilgan 👇 Yo\'nalishlardan birini tanlash orqali savollarga javoblarni olishingiz mumkin! Agar sizning savolingizga javob topilmasa savol yozib qoldirish bo\'limida  o\'z murojaatingizni qoldirish orqali, qisqa vaqt ichida savolingizga javob olishingiz mumkin bo\'ladi.', reply_markup=btn)

@dp.callback_query_handler(text='37')
async def call(call:types.CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer(f'8-savolga javob: O\'zbekiston Respublikasi Vazirlar Mahkamasining  2018 yil 1 dekabrdagi 975-son qarorining 14-bandi “Haydovchini mast holda deb hisoblashga asoslar mavjud bo\'lgan taqdirda, uni transport vositasini boshqarishdan chetlatish, mastlik holatini aniqlash uchun belgilangan tartibda tekshiruvdan o\'tkazish, haydovchi mastligi yoki mast emasligini aniqlash uchun tekshiruv o\'tkazilishidan bo\'yin tovlagan taqdirda MJtKning 136-moddasida nazarda tutilgan huquqbuzarlik uchun maʼmuriy bayonnoma rasmiylashtirish” talablari asosida mast holda transport vositasini boshqargan haydovchi tibbiy tekshiruvdan o\'tishdan bosh tortgan taqdirda MJtKning 136-moddasi tartibida maʼmuriy bayonnoma rasmiylashtiradi.\n\n'
                              f'Quyida eng ko`p beriladigan savollarga javoblar keltirilgan 👇 Yo\'nalishlardan birini tanlash orqali savollarga javoblarni olishingiz mumkin! Agar sizning savolingizga javob topilmasa savol yozib qoldirish bo\'limida  o\'z murojaatingizni qoldirish orqali, qisqa vaqt ichida savolingizga javob olishingiz mumkin bo\'ladi.', reply_markup=btn)




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)



