import cv2
import glob

# img = cv2.imread('image8/11.jpg')
# cv2.imshow("r", img)


# img = img[ 20: 660, 220: 860]
# cv2.imshow("crop", img)
# cv2.waitKey(0)
count = 0
# import the opencv library

for img_path in glob.glob('image10/'+'/*.jpg'):
    img = cv2.imread(img_path)
    
    # cv2.rectangle(img,(520,20), (1260,660), color=(0,0,255), thickness=2)
    # cv2.imwrite('image9/bg.jpg' , img)

    img = img[ 20: 660, 520: 1260]

    cv2.imwrite('image9/%d.jpg' % count, img)
    count += 1
    print(count)

