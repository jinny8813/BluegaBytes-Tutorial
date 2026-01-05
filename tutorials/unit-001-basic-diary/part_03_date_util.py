"""
2026 Basic Daily Planner Generator
Part 3: Date Utility Functions Example
生成日期輔助函式範例
1. 日期輔助函式使用範例
2. 判斷週末，應用不同顏色
"""

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import HexColor
from datetime import datetime, timedelta
import os


print("=" * 60)
print("開始生成 2026 年日記本")
print("=" * 60)

os.makedirs("output", exist_ok=True)
output_path = os.path.join("output", "part_03_date_util.pdf")

pdfmetrics.registerFont(TTFont('NotoSansTC', './assets/NotoSansTC-Regular.ttf'))

c = canvas.Canvas(output_path, pagesize=A4)

current_date = datetime(2026, 1, 1)
end_date = datetime(2026, 12, 31)

while current_date <= end_date:
    weekday = current_date.isoweekday()  # 1=Mon, 7=Sun
    if weekday == 6:
        c.setFillColor(HexColor("#6666FF"))  # Saturday - Blue
    elif weekday == 7:
        c.setFillColor(HexColor("#FF6666"))  # Sunday - Red
    else:
        c.setFillColor(HexColor("#333333"))  # Weekdays - Dark Gray
    c.setFont("NotoSansTC", 12)
    c.drawString(100, 800, f"日期: {current_date.strftime('%Y-%m-%d')} 星期{weekday}")
    c.showPage()
    current_date += timedelta(days=1)

c.save()

print("=" * 60)
print("生成完成！")
print(f"檔案位置: {output_path}")
print("=" * 60)