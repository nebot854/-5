import cv2  
# Загрузка изображений
background = cv2.imread('fggfg.png')  # Фоновое изображение
overlay = cv2.imread('mamma.png')        # Изображение для наложения

# Преобразование размера наложенного изображения (если необходимо)
overlay = cv2.resize(overlay, (background.shape[1], background.shape[0]))

# Наложение изображения
# Здесь мы используем альфа-канал для создания полупрозрачного эффекта
alpha = 0.5  # Коэффициент смешивания (от 0 до 1)
combined = cv2.addWeighted(background, 1 - alpha, overlay, alpha, 0)

# Сохранение результата
cv2.imwrite('result.jpg', combined)

# Отображение результата
cv2.imshow('Combined Image', combined)
cv2.waitKey(0)
cv2.destroyAllWindows()

         
  
# Отображаем результат  
#cv2.imshow('Результат', result)  
#cv2.waitKey(0)  
#cv2.destroyAllWindows()  
  
# Читаем первое изображение  
#img1 = cv2.imread('mamma.png')  
  
# Читаем второе изображение  
#img2 = cv2.imread('fggfg.png')  
  
# Проверяем, что изображения успешно загружены  
#if img1 is None or img2 is None:  
    #print("Ошибка: не удалось загрузить изображения")  
    #exit()  
  
# Определяем размеры изображений  
##height2, width2 = img2.shape[:2]  
  
# Склеиваем изображения горизонтально  
#result_horizontal = cv2.hconcat([img1, img2])  
  
# Склеиваем изображения вертик
  
# Сохраняем результаты  
#cv2.imwrite('result_horizontal.jpg', result_horizontal)  
