"""
2026 Basic Daily Planner Generator
Part 1: Single Content Page Example
生成單一內容頁面的範例
1. reportlab 生成電子手帳的基本流程
2. 設定文字樣式：字體、大小、顏色
3. 插入自定義字體
4. reportlab 座標系統介紹
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

# 確保輸出目錄存在
os.makedirs("output", exist_ok=True)
output_path = os.path.join("output", "part_01_single_content.pdf")

# 註冊中文字體
pdfmetrics.registerFont(TTFont('NotoSansTC', './assets/NotoSansTC-Regular.ttf'))

# 建立 PDF
c = canvas.Canvas(output_path, pagesize=A4)

c.setFont("Helvetica", 12)
c.setFillColor(HexColor("#333333"))
c.drawString(100, 800, "This is a single content page for 2026 Daily Planner.")
c.showPage()  # 完成此頁

c.setFont("NotoSansTC", 12)
c.setFillColor(HexColor("#5894D9"))
c.drawString(100, 800, "我愛阿藍～～")
c.showPage()  # 完成此頁

c.save()  # 儲存 PDF

print("=" * 60)
print("生成完成！")
print(f"檔案位置: {output_path}")
print("=" * 60)