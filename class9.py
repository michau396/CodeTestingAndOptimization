import cv2
import numpy as np

img = cv2.imread('dog.jpeg')
if img is None:
    print("Nie znaleziono obrazu")
    exit()

# 1. Dodanie 50 jasnosci: numpy vs cv2.add
np_added = np.clip(img + 50, 0, 255).astype(np.uint8)
cv_added = cv2.add(img, 50)
cv2.imshow("Numpy +50", np_added)
cv2.imshow("OpenCV add +50", cv_added)

# 2. "Przepalenie" numpy +150 vs cv2.add +150
np_over = np.clip(img + 150, 0, 255).astype(np.uint8)
cv_over = cv2.add(img, 150)
cv2.imshow("Numpy +150", np_over)
cv2.imshow("OpenCV add +150", cv_over)

# 3. Przyciemnianie o 80: numpy vs cv2.add (dodajemy -80, czyli odejmujemy)
np_dark = np.clip(img - 80, 0, 255).astype(np.uint8)
cv_dark = cv2.add(img, -80)  # uwaga: cv2.add nie przyjmuje wartosci ujemnych, wiec dziala inaczej
# zamiast cv2.add do przyciemniania uzyjemy cv2.subtract
cv_dark = cv2.subtract(img, 80)
cv2.imshow("Numpy -80", np_dark)
cv2.imshow("OpenCV subtract 80", cv_dark)

# 4. Filtr Instagram: R+30, G-20, B+10
filtered = img.copy()
b, g, r = cv2.split(filtered)
r = cv2.add(r, 30)
g = cv2.subtract(g, 20)
b = cv2.add(b, 10)
filtered = cv2.merge([b, g, r])
cv2.imshow("Instagram filter", filtered)

# 5. Detekcja zmian - wczytaj dwa obrazy
img2 = cv2.imread('cat.jpeg')
if img2 is None:
    print("Nie znaleziono drugiego obrazu")
else:
    diff = cv2.absdiff(img, img2)
    cv2.imshow("Roznica", diff)

cv2.waitKey(0)
cv2.destroyAllWindows()
