import cv2

names =  [ 
         "이승은1.mp4", "이승은2.mp4", "이승은3.mp4", "이승은4.mp4", "이승은5.mp4", "이승은6.mp4", 
         "정창균1.mp4", "정창균2.mp4", "정창균3.mp4", "정창균4.mp4", "정창균5.mp4", "정창균6.mp4", 
        

        ]

for idx,n in enumerate(names):

    capture = cv2.VideoCapture("video/{}".format(n))
    cnt_scene = 10000
    while True:
        if(capture.get(cv2.CAP_PROP_POS_FRAMES) == capture.get(cv2.CAP_PROP_FRAME_COUNT)):
            break
    
        ret, frame = capture.read()
        cv2.imshow("VideoFrame", frame)
        img_32 = cv2.resize(frame,(64,64))
        cv2.imwrite("image/{}_{}.png".format(idx,cnt_scene), img_32)
        
        cnt_scene+=1
        if cv2.waitKey(33) > 0: break
    
    capture.release()
    cv2.destroyAllWindows()
