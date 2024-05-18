import cv2

def scan_qr_code(cap):
  while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    qr_detector = cv2.QRCodeDetector()

    data, bbox, _ = qr_detector.detectAndDecode(gray)

    if bbox is not None:
      if data:
        cap.release()
        cv2.destroyAllWindows()
        return data
    cv2.imshow('QR Code Scanner', frame)
    # Exit if 'q' key is pressed
    if cv2.waitKey(1) == ord('q'):
      break

  # Release capture
  cap.release()
  cv2.destroyAllWindows()

