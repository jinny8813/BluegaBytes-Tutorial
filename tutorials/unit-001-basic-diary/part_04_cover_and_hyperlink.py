"""
2026 Basic Daily Planner Generator
Part 4: Cover and Hyperlinks Example
生成日期輔助函式範例
1. reportlab 插入圖片
2. 建立書籤與超連結
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
output_path = os.path.join("output", "part_04_cover_and_hyperlink.pdf")

pdfmetrics.registerFont(TTFont('NotoSansTC', './assets/NotoSansTC-Regular.ttf'))

c = canvas.Canvas(output_path, pagesize=A4)

current_date = datetime(2026, 1, 1)
end_date = datetime(2026, 12, 31)

img_path = "./assets/cover.png"
c.setFillAlpha(0.6)
c.drawImage(img_path, 0, 0, width=A4[0], height=A4[1])
c.setFont("NotoSansTC", 24)
c.setFillColor(HexColor("#333333"))
c.drawCentredString(A4[0]/2, A4[1]/2 + 50, "2026 年日記本")
c.bookmarkPage("CoverPage")
c.showPage()

while current_date <= end_date:
    weekday = current_date.isoweekday()
    if weekday == 6:
        c.setFillColor(HexColor("#6666FF"))
    elif weekday == 7:
        c.setFillColor(HexColor("#FF6666"))
    else:
        c.setFillColor(HexColor("#333333"))

    c.setFont("NotoSansTC", 12)
    c.drawString(100, 800, f"日期: {current_date.strftime('%Y-%m-%d')} 星期{weekday}")

    c.drawString(50, 50, "回到封面")
    c.linkAbsolute("回到封面", "CoverPage", Rect=(50, 50, 100, 70))

    c.showPage()
    current_date += timedelta(days=1)

c.save()

print("=" * 60)
print("生成完成！")
print(f"檔案位置: {output_path}")
print("=" * 60)