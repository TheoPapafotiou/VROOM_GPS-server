import cv2
import numpy as np

class objectTracking:

    def objectTracking(self, frame1, frame2):
        diff = cv2.absdiff(frame1, frame2)
        gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (5,5), 0)
        _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
        dilated = cv2.dilate(thresh, None, iterations=3)
        contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        for contour in contours:
            (x, y, w, h) = cv2.boundingRect(contour)

            if cv2.contourArea(contour) < 800 or cv2.contourArea(contour) > 1000:
                continue
            cv2.rectangle(frame2, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(frame2, "Status: {}".format('Movement'), (10, 20), cv2.FONT_HERSHEY_SIMPLEX,
                        1, (0, 0, 255), 3)
            center_x = x + w/2
            center_y = y + h/2
            return frame2, center_x, center_y
        #cv2.drawContours(frame1, contours, -1, (0, 255, 0), 2)

        return frame2, 0, 0