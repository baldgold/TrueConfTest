import cv2
import wx.lib.imagebrowser as imagebrowser
import wx


if __name__ == "__main__":

    app = wx.App(False)
    dialog = imagebrowser.ImageDialog(None)
    if dialog.ShowModal() == wx.ID_OK:
        image_address = dialog.GetFile()
        print("Вы выбрали файл: " + image_address)
    dialog.Destroy()

    src = cv2.imread(image_address, cv2.IMREAD_UNCHANGED)

    if src is None:
        wx.MessageBox('Вы выбрали НЕ изображение\nПопробуйте ещё раз.', 'Проблема с изображением', wx.OK | wx.ICON_WARNING)
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
        cv2.imwrite('new_image_x2.png', output)
        print('Дело сделано!')
