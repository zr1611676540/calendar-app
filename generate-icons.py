#!/usr/bin/env python3
"""生成 PWA 图标（需要 Pillow 库）"""

from PIL import Image, ImageDraw
import os

def create_icon(size, filename):
    img = Image.new('RGB', (size, size), '#4A90D9')
    draw = ImageDraw.Draw(img)
    
    # 圆角矩形背景
    margin = size // 8
    draw.rounded_rectangle(
        [margin, margin, size - margin, size - margin],
        radius=size // 16,
        fill='white'
    )
    
    # 顶部蓝色条
    top_height = size // 5
    draw.rounded_rectangle(
        [margin, margin, size - margin, margin + top_height * 2],
        radius=size // 16,
        fill='#4A90D9'
    )
    
    # 小圆点表示任务
    dot_radius = size // 16
    row1_y = margin + top_height * 2 + size // 8
    row2_y = row1_y + size // 6
    
    colors = ['#4A90D9', '#9B59B6', '#27AE60', '#F39C12']
    for i, color in enumerate(colors[:3]):
        x = margin + size // 6 + (i * size // 6)
        draw.ellipse([x - dot_radius, row1_y - dot_radius, 
                      x + dot_radius, row1_y + dot_radius], fill=color)
    
    for i, color in enumerate(colors):
        x = margin + size // 6 + (i * size // 6)
        draw.ellipse([x - dot_radius, row2_y - dot_radius, 
                      x + dot_radius, row2_y + dot_radius], fill=color)
    
    img.save(filename, 'PNG')
    print(f'✓ 生成 {filename}')

if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    create_icon(192, 'icon-192.png')
    create_icon(512, 'icon-512.png')
    print('图标生成完成！')
