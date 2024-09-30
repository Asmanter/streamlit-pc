import svgwrite
import io
import streamlit as st
import os

# Функция для проверки среды выполнения
def is_streamlit():
    try:
        return bool(st.runtime.exists())
    except:
        return False

# Задаем длину гильзы в мм
barrel_mm = 100
cover_to_cover_mm = barrel_mm + 94
pc_mm = cover_to_cover_mm + 48

# Задаем размеры для изображений
rod_width = 1609
rod_height = 2585
front_cover_width = 2039
front_cover_height = 2585
back_cover_width = 2588
back_cover_height = 2585
barrel_height = 2585
barrel_length = (barrel_mm * 27.7787) - 27.7787
front_view_width = 1383
front_view_height = 2585

# Масштабирование
scale_factor = 0.8

# Рассчитываем размеры холста
canvas_width = (rod_width + front_cover_width + barrel_length + back_cover_width + front_view_width + 100) * scale_factor
canvas_height = max(rod_height, front_cover_height, barrel_height, back_cover_height, front_view_height) * scale_factor

# Инициализация нового чертежа
svg_file = 'pc.svg'
dwg = svgwrite.Drawing(svg_file, size=(canvas_width, canvas_height), profile='full')

# Добавляем изображения (примерно так, как в вашем коде)
rod_x, rod_y = 0, 0
front_cover_x, front_cover_y = rod_width * scale_factor, rod_y
barrel_x, barrel_y = (rod_width + front_cover_width) * scale_factor, rod_y
back_cover_x, back_cover_y = (rod_width + front_cover_width + barrel_length) * scale_factor, rod_y
front_view_x, front_view_y = (rod_width + front_cover_width + barrel_length + back_cover_width + 100) * scale_factor, rod_y

dwg.add(dwg.image('rod.svg', insert=(rod_x, rod_y), size=(rod_width * scale_factor, rod_height * scale_factor)))
dwg.add(dwg.image('front_cover.svg', insert=(front_cover_x, front_cover_y), size=(front_cover_width * scale_factor, front_cover_height * scale_factor)))
dwg.add(dwg.image('barrel.svg', insert=(barrel_x, barrel_y), size=(barrel_length * scale_factor, barrel_height * scale_factor), preserveAspectRatio="none"))
dwg.add(dwg.image('back_cover.svg', insert=(back_cover_x, back_cover_y), size=(back_cover_width * scale_factor, back_cover_height * scale_factor)))
dwg.add(dwg.image('front_view.svg', insert=(front_view_x, front_view_y), size=(front_view_width * scale_factor, front_view_height * scale_factor)))

# Проверка среды выполнения
if is_streamlit():
    # Работа в Streamlit: сохраняем в буфер и выводим как HTML
    svg_buffer = io.StringIO()
    dwg.write(svg_buffer)
    svg_data = svg_buffer.getvalue()
    
    # Выводим SVG как HTML
    st.write(f'<div>{svg_data}</div>', unsafe_allow_html=True)

else:
    # Работа на ПК: сохраняем SVG на диск
    dwg.saveas(svg_file)
    print(f"SVG файл сохранен как {svg_file}")
