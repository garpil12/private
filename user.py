from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CommandHandler

# ================= MENU COMMAND =================

def menu_cmd(update, context):
    text = """
╭━━━━━━━━━━━━━━━━━━━━━━━╮
   ⚡ 𝗛𝗘𝗟𝗣 & 𝗙𝗜𝗧𝗨𝗥 𝗕𝗢𝗧 ⚡
╰━━━━━━━━━━━━━━━━━━━━━━━╯

👋 Selamat datang di bot!

Berikut penjelasan fitur yang tersedia 👇

━━━━━━━━━━━━━━━━━━━━━━━

👤 USER FEATURES

🏷️ /tagall
➜ Untuk menandai semua member di group

⏰ /absen
➜ Absen otomatis 24 jam (sistem kehadiran)

📊 /rekab [nama]
➜ Rekap jobdast TMO
Contoh:
/rekab HYPERION https://t.me/officialhyperion

📄 /getjobdast
➜ Menampilkan pilihan Jobdesk TMO
(Admin bisa isi jobdesk dengan mudah)

━━━━━━━━━━━━━━━━━━━━━━━

👑 OWNER FEATURES

📢 /bc
➜ Broadcast pesan ke semua user / group

👤 /addpj & /delpj
➜ Mengatur PJ (Penanggung Jawab)

🖼️ /addpict & /delpict
➜ Mengatur gambar/menu bot

🤝 /listpartner
➜ Melihat daftar partner

➕ /addpartner
➜ Menambah partner baru

➖ /delpartner
➜ Menghapus partner

🔘 /addbuttontag
➜ Menambah tombol tag custom

━━━━━━━━━━━━━━━━━━━━━━━

💡 Gunakan bot dengan bijak!
"""

    keyboard = [
        [InlineKeyboardButton("🛒 STORE - @storegarf", url="https://t.me/storegarf")]
    ]

    update.message.reply_photo(
        photo="https://i.ibb.co/rf5pNpck/file-00000000d14c71fa9909f192b1de2818.png",
        caption=text,
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

# ================= REGISTER =================

def register_menu(dp):
    dp.add_handler(CommandHandler("menu", menu_cmd))
