import os
import json
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from Resnet import resnet50


im_height = 224 # 输入图片的高
im_width = 224  # 输入图片的宽

def predict_fish(img_path):
    # # 打印当前工作目录
    # current_dir = os.getcwd()
    # print("Current working directory:", current_dir)
    # img_path = current_dir + img_path
    # 加载图片
    assert os.path.exists(img_path), "file: '{}' dose not exist.".format(img_path)
    img = Image.open(img_path)

    # 图片修改为 224x224
    img = img.resize((im_width, im_height))
    plt.imshow(img)

    # 归一化
    img = np.array(img) / 255.

    # 添加一个batch_size维度
    img = (np.expand_dims(img, 0))

    # 读取种类字典
    json_path = 'web/class_indices.json'
    assert os.path.exists(json_path), "file: '{}' dose not exist.".format(json_path)
    with open(json_path, "r") as f:
        class_indict = json.load(f)

    # 实例化模型
    model_name = "Resnet"
    model = resnet50(num_classes=9, include_top=True)
    weighs_path = f"web/save_weights/my{model_name}.h5"
    assert os.path.exists(img_path), "file: '{}' dose not exist.".format(weighs_path)
    model.load_weights(weighs_path, by_name=True)

    # prediction
    result = np.squeeze(model.predict(img))
    predict_class = np.argmax(result)

    # # 打印每个类别的概率
    # for i in range(len(result)):
    #     print("class: {:10}   prob: {:.3}".format(class_indict[str(i)],
    #                                                 result[i]))

    # 返回预测的类别
    result = {"class": class_indict[str(predict_class)], "prob": str(result[predict_class])}
    print(result)
    return result

# if __name__ == '__main__':
#     img_path = r"web\草鱼.jpg" # 预测的图片
#     predict_fish(img_path)


