"""
2026 Basic Daily Planner Generator
Part 2: Shapes and Loop Example
生成包含圖形和迴圈的範例
1. reportlab 生成直線、矩形、圓形
2. 使用迴圈生成方格基底
3. 使用迴圈生成多頁重複內容
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
output_path = os.path.join("output", "part_02_shapes_and_loop.pdf")

pdfmetrics.registerFont(TTFont('NotoSansTC', './assets/NotoSansTC-Regular.ttf'))

c = canvas.Canvas(output_path, pagesize=A4)

c.setFont("NotoSansTC", 12)
c.drawString(100, 800, "直線")
c.line(100, 790, 300, 790)  # x1, y1, x2, y2
c.showPage()

c.setFont("NotoSansTC", 12)
c.drawString(100, 800, "矩形")
c.rect(100, 700, 200, 50, stroke=1, fill=0)  # x, y, width, height
c.showPage()

c.setFont("NotoSansTC", 12)
c.drawString(100, 800, "圓形")
c.circle(200, 700, 40, stroke=1, fill=0)  # x_center, y_center, radius
c.showPage()

c.setFont("NotoSansTC", 12)
c.drawString(100, 800, "方格基底 - 方格")
grid_size = 20
for x in range(100, 400, grid_size):
    for y in range(600, 800, grid_size):
        c.setFillColor(HexColor("#999999"))
        c.setDash(1, 2)
        c.setLineWidth(0.5)
        c.rect(x, y, grid_size, grid_size, stroke=1, fill=0)
c.showPage()

c.setFont("NotoSansTC", 12)
c.drawString(100, 800, "方格基底 - 線條")
grid_size = 20
for x in range(100, 400, grid_size):
    c.setFillColor(HexColor("#999999"))
    c.setDash(1, 2)
    c.setLineWidth(0.5)
    c.line(x+grid_size, 600, x + grid_size, 800)
for y in range(600, 800, grid_size):
    c.setFillColor(HexColor("#999999"))
    c.setDash(1, 2)
    c.setLineWidth(0.5)
    c.line(100, y+grid_size, 400, y + grid_size)
c.showPage()

for i in range(10):
    c.setFont("NotoSansTC", 12)
    c.drawString(100, 800, f"重複頁面範例 - 第 {i+1} 頁")
    c.showPage()

c.save()

print("=" * 60)
print("生成完成！")
print(f"檔案位置: {output_path}")
print("=" * 60)