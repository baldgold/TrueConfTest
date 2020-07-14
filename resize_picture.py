import cv2

image_address = input('Введите адрес изображения, которое желаете масштабировать в 2 раза:\n>>>')

src = cv2.imread(image_address, cv2.IMREAD_UNCHANGED)

if src is None:
    print('Изображение не найдено!')
else:
    # процент, на который измениться размер изображения
    scale_percent = 200

    # расчитываем 200% от исходного размера
    width = int(src.shape[1] * scale_percent / 100)
    height = int(src.shape[0] * scale_percent / 100)

    # устанавливаем желаемый размер для изображения
    new_size = (width, height)

    output = cv2.resize(src, new_size)

    # записываем вывод cv2.resize в локальный файл изображения
    cv2.imwrite('new_image_2x.png', output)
    print('Дело сделано!')
