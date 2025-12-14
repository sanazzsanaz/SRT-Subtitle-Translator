import os
import time
from deep_translator import GoogleTranslator

# همین فولدری که srt.py داخلشه
base_dir = os.path.dirname(os.path.abspath(__file__))

input_name = "harry.srt"      # ورودی
output_name = "harrynew.txt"  # خروجی (همونی که می‌خوای)

input_path = os.path.join(base_dir, input_name)
output_path = os.path.join(base_dir, output_name)

print("ورودی:", input_path)
print("خروجی:", output_path)

# اگر harry.srt نیست، اصلاً ادامه ندیم
if not os.path.exists(input_path):
    print("❌ فایل harry.srt کنار srt.py پیدا نشد.")
    raise SystemExit

translator = GoogleTranslator(source='en', target='fa')

# خوندن زیرنویس اصلی
with open(input_path, encoding="utf-8") as f:
    sub_lines = f.readlines()

# نوشتن زیرنویس جدید
with open(output_path, "w", encoding="utf-8") as f:
    for line in sub_lines:
        stripped = line.strip()

        # ۱) شمارهٔ زیرنویس (فقط عدد)
        if stripped.isdigit():
            f.write(line)

        # ۲) تایم‌کد (شامل -->)
        elif "-->" in line:
            f.write(line)

        # ۳) خط خالی
        elif stripped == "":
            f.write("\n")

        # ۴) متن برای ترجمه
        else:
            try:
                print("EN:", stripped)
                fa = translator.translate(stripped)
                print("FA:", fa)
                f.write(fa + "\n")
                time.sleep(0.3)  # مکث کوچیک که شبیه اسپم دیده نشه
            except Exception as e:
                print("⚠️ خطا در ترجمه این خط:", stripped)
                print("جزئیات:", e)
                # اگر ترجمه خورد به خطا، متن انگلیسی رو می‌نویسیم که فایل خالی نشه
                f.write(line)
