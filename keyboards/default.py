from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='📢 Tanlovda ishtirok etish ☑️'),
            KeyboardButton(text="📔 Darsliklar 📚")
        ],
        [
            KeyboardButton(text='🎁 Sovg\'alar'),
            KeyboardButton(text='👤 Ma\'lumotlar')
        ],
        [
            KeyboardButton(text='💡 Shartlar'),
            KeyboardButton(text='📊 Reyting')
        ]
    ],resize_keyboard=True
)

darsliklar = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='IELTS'),
            KeyboardButton(text='MULTILEVEL')
        ],
        [
            KeyboardButton(text='⬅️ Ortga')
        ]
    ],resize_keyboard=True
)


numbers = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Raqamni yuborish 📞',request_contact=True)
        ]
    ],resize_keyboard=True
)
