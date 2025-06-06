HELLO = (
    "<b>👋 Salom! Men sizning barcha do'stlaringizning sirlarini saqlayman.</b>\n\n"
    "🤫 Men ularning sirlarini baham ko'rishim mumkin. Tugmasini bosing 👇"
)

COMPATIBILITY_TEST_NOT_CREATED = (
    "<b>😉 Salom! "
    "Bu yerda sizning do'stlaringiz, "
    "sizni qanchalik yaxshi bilishini bilib olishingiz uchun o'z testingizni yaratishingiz mumkin.</b>\n\n"
    "«Testingizni yarating» tugmasini bosing va ko'rsatmalarga amal qiling."
)

COMPATIBILITY_TEST_CREATED = (
    "<b>😁 Sizda allaqachon tayyor test bor. "
    "</b>Endi siz faqat test natijalarini ko'rishingiz yoki uni o'chirishingiz mumkin. "
    "E'tibor bering, agar siz testni o'chirib tashlasangiz, "
    "butun reyting qayta o'rnatiladi va havola endi ishlamaydi.\n\n"
    "<b>Test havolasi: https://t.me/{bot_username}?start=s_{id}</b>\n\n"
    "<b>Sinov havolasini do'stlaringizga yuboring yoki Instagram hikoyalarida joylashtiring.</b>"
)

USER_HAS_NO_TEST_CREATED = (
    "<b>Sen hali do'stlikni tekshirish uchun test yaratmagansan!</b>\n\n"
    """Shunchaki "Test yaratish" tugmasini bosing va ko'rsatmalarga rioya qiling."""
)

USER_HAS_TEST_CREATED = (
    '<b>❗️ Sizda shunday test bormi.</b>\n\n'
    """<i>Agar uni qayta yaratmoqchi bo'lsangiz, /start → Testni o'chirish 🗑 tugmasini toping.</i>"""
)

START_CREATING_TEST = (
    "Yaxshi. Savollar ostidagi tugmalar yordamida quyidagi 10 ta savolga javob bering. "
    "Halol javob bering, aks holda do'stlaringiz to'g'ri javob bera olmaydi."
)

START_PROCESS_TEST = (
    "<b>Mayli, endi boshlaylik. Yigitingiz/qiz do'stingiz haqida quyida keltirilgan 15 ta savolga javob bering.</b>\n\n"
    "<b>Hech qanday variant mos kelmasa, eng yaqinini tanlang, garchi u aniq bo'lmasa ham.</b>"
)

TEST_CREATED = (
    "<b>🎉 Tabriklaymiz! Siz testingizni yaratdingiz.</b>\n\n"
    "Test havolasi: https://t.me/{bot_username}?start=s_{id}\n\n"
    "<b>Uni barcha ijtimoiy tarmoqlarda tarqating va barcha do'stlaringiz va tanishlaringiz bilan baham ko'ring. "
    "Keling, ular sizni qanchalik yaxshi bilishlarini ko'ramiz 😉</b>"
)

TEST_STATS = (
    'Natijalar 📊\n\n'
    "Hammasi o'tdi: {count}\n\n"
    "Sizni taxminan: {average_percentage}%\n\n"
    "Do'stlar ro'yxati:\n\n{list_of_results}"
)

CREATION_TEST_STOP = (
    "To'xtatildi. Asosiy menyuga o'tish uchun /start tugmasini bosing."
)

PROCCESS_TEST_STOP = (
    "To'xtatildi. Asosiy menyuga o'tish uchun /start tugmasini bosing."
)

USER_ALREADY_HAS_TEST = (
    '<b>👍 Sizda shunday test bormi.</b>\n\n'
    "<i>Agar uni qayta yaratmoqchi bo'lsangiz, /start → Testni o'chirish 🗑 tugmasini toping.</i>"
)

TEST_YOURSELF = (
    "<b>😁 O'z testini o'tkazish ajoyib, lekin uni do'stlaringga yuborish yaxshiroq!</b>\n\n"

    '<b>🔗 Sizning havolangiz:</b> https://t.me/{bot_username}?start=s_{id}\n\n'

    "<i>📱O'z havolangizni Telegram/Instagram/TikTok va boshqa ijtimoiy tarmoqlarda e'lon qiling, shunda sizni qancha % odam tanishini ko'ring!</i>\n\n"
)