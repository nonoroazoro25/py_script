import cv2

# 创建读取视频的类
capture = cv2.VideoCapture("watermark.mp4")
# 得到视频的高度
height = capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
# 得到视频的宽度
width = capture.get(cv2.CAP_PROP_FRAME_WIDTH)
# 得到视频的帧数
count = capture.get(cv2.CAP_PROP_FRAME_COUNT)
# 得到视频的帧速
fps = capture.get(cv2.CAP_PROP_FPS)


# 对视频中的每一帧图像做处理的函数
def process_fun(image):
    # 去除视频的水印
    # 需要注意的是第一个范围是y轴坐标的范围,第二个是x轴坐标的范围
    image[380:511, 1070:1212] = image[100:231, 1070:1212]
    image[8:63, 1111:1275] = image[8:63, 800:964]
    return image


# 保存MP4的视频
fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
# 创建写入视频的类
out_video = cv2.VideoWriter()
out_video.open('processed_video.mp4', fourcc, fps, (int(width), int(height)), True)
while (True):
    # 读取视频中的每一帧
    ret, frame = capture.read()
    # 如果该帧存在则进行操作
    if ret is True:
        # 对输入的每一帧图像处理
        result = process_fun(frame)
        # 保存已经处理后的每一帧图像
        out_video.write(result)
        # cv2.imwrite("precessed.jpg",result)
    # 如果该帧不存在则循环结束
    else:
        break
out_video.release()
