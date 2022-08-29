import cv2

# ������ȡ��Ƶ����
capture = cv2.VideoCapture("watermark.mp4")
# �õ���Ƶ�ĸ߶�
height = capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
# �õ���Ƶ�Ŀ��
width = capture.get(cv2.CAP_PROP_FRAME_WIDTH)
# �õ���Ƶ��֡��
count = capture.get(cv2.CAP_PROP_FRAME_COUNT)
# �õ���Ƶ��֡��
fps = capture.get(cv2.CAP_PROP_FPS)


# ����Ƶ�е�ÿһ֡ͼ��������ĺ���
def process_fun(image):
    # ȥ����Ƶ��ˮӡ
    # ��Ҫע����ǵ�һ����Χ��y������ķ�Χ,�ڶ�����x������ķ�Χ
    image[380:511, 1070:1212] = image[100:231, 1070:1212]
    image[8:63, 1111:1275] = image[8:63, 800:964]
    return image


# ����MP4����Ƶ
fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
# ����д����Ƶ����
out_video = cv2.VideoWriter()
out_video.open('processed_video.mp4', fourcc, fps, (int(width), int(height)), True)
while (True):
    # ��ȡ��Ƶ�е�ÿһ֡
    ret, frame = capture.read()
    # �����֡��������в���
    if ret is True:
        # �������ÿһ֡ͼ����
        result = process_fun(frame)
        # �����Ѿ�������ÿһ֡ͼ��
        out_video.write(result)
        # cv2.imwrite("precessed.jpg",result)
    # �����֡��������ѭ������
    else:
        break
out_video.release()
