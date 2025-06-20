import cv2

img = cv2.imread('cat.jpg')
if img is None:
    print("Nie znaleziono obrazu")
    exit()

h, w = img.shape[:2]

# 1. ROI 100x100 w lewym górnym rogu
roi1 = img[0:100, 0:100]
cv2.imshow("ROI 100x100 lewy gorny", roi1)

# 2. Dolna polowa
bottom_half = img[h//2:h, 0:w]
cv2.imshow("Dolna polowa", bottom_half)

# 3. Prawa polowa
right_half = img[0:h, w//2:w]
cv2.imshow("Prawa polowa", right_half)

# 4. Dynamiczny wybór ROI
startX = int(input("startX: "))
endX = int(input("endX: "))
startY = int(input("startY: "))
endY = int(input("endY: "))
roi_dyn = img[startY:endY, startX:endX]
cv2.imshow("Dynamiczne ROI", roi_dyn)

# 5. Kadrowanie twarzy (tu przykład z ustalonym ROI, podmień wg potrzeb)
face_roi = img[50:250, 100:300]
cv2.imshow("Twarz", face_roi)

# 6. Kopiowanie i wklejanie fragmentu
fragment = img[0:100, 0:100].copy()
img[150:250, 150:250] = fragment
cv2.imshow("Wklejony fragment", img)

# 7. Podzial na 3x3
cell_h, cell_w = h//3, w//3
for i in range(3):
    for j in range(3):
        part = img[i*cell_h:(i+1)*cell_h, j*cell_w:(j+1)*cell_w]
        cv2.imshow(f"Cell {i}_{j}", part)

# 8. Animacja przesuwajacego sie ROI poziomo co 10 px
x = 0
while x + 100 <= w:
    roi_anim = img[0:100, x:x+100]
    cv2.imshow("Animacja ROI", roi_anim)
    key = cv2.waitKey(0)
    if key == 27:  # ESC konczy
        break
    x += 10

# 9. Przyciecie 300x300 i zapis
cropped = img[0:300, 0:300]
cv2.imwrite("cropped_image.jpg", cropped)
cv2.imshow("Cropped 300x300", cropped)

cv2.waitKey(0)
cv2.destroyAllWindows()
