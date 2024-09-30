import svgwrite
import io

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
dwg = svgwrite.Drawing(size=(canvas_width, canvas_height), profile='full')

# Координаты для изображений
rod_x = 0
rod_y = 0
front_cover_x = rod_width * scale_factor
front_cover_y = rod_y
barrel_x = (rod_width + front_cover_width) * scale_factor
barrel_y = rod_y
back_cover_x = (rod_width + front_cover_width + barrel_length) * scale_factor
back_cover_y = rod_y
front_view_offset = 100
front_view_x = (rod_width + front_cover_width + barrel_length + back_cover_width + front_view_offset) * scale_factor
front_view_y = rod_y

# Добавляем изображения
dwg.add(dwg.image('rod.svg', insert=(rod_x, rod_y), size=(rod_width * scale_factor, rod_height * scale_factor)))
dwg.add(dwg.image('front_cover.svg', insert=(front_cover_x, front_cover_y), size=(front_cover_width * scale_factor, front_cover_height * scale_factor)))
dwg.add(dwg.image('barrel.svg', insert=(barrel_x, barrel_y), size=(barrel_length * scale_factor, barrel_height * scale_factor), preserveAspectRatio="none"))
dwg.add(dwg.image('back_cover.svg', insert=(back_cover_x, back_cover_y), size=(back_cover_width * scale_factor, back_cover_height * scale_factor)))
dwg.add(dwg.image('front_view.svg', insert=(front_view_x, front_view_y), size=(front_view_width * scale_factor, front_view_height * scale_factor)))

# Добавляем текст
font_size = 123 * scale_factor
text_x = (2000 + (rod_width + 443) + rod_width + front_cover_width + barrel_length + 831) / 2 * scale_factor
text_y = 2253 * scale_factor
text_xpc = ((2000 + 728 + rod_width + front_cover_width + barrel_length + 831) / 2) * scale_factor
text_ypc = 2417 * scale_factor

dwg.add(dwg.text(f"{int(cover_to_cover_mm)}", insert=(text_x, text_y), font_size=font_size, font_family="Arial", fill="black", transform="skewX(-25)"))
dwg.add(dwg.text(f"{int(pc_mm)}", insert=(text_xpc, text_ypc), font_size=font_size, font_family="Arial", fill="black", transform="skewX(-25)"))

# Добавляем осевую линию (примерно как в вашем коде)
# ...

# Сохранение SVG файла в память
svg_memory_file = io.StringIO()
dwg.write(svg_memory_file)
svg_data = svg_memory_file.getvalue()

# Использование svg_data в приложении Streamlit
import streamlit as st

st.image(svg_data, format="svg")
