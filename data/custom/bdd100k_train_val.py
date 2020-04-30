#此代码位于darknet根目录下
import glob

def generate_train_and_val(image_path, txt_file):
    with open(txt_file, 'w') as tf:
        i=1
        for jpg_file in glob.glob(image_path + '*.jpg'):
            print("processing {}".format(i))
            tf.write(jpg_file + '\n')
            i += 1


def main(path, dstpath):
    generate_train_and_val(path, dstpath)


if __name__ == '__main__':
    #srcpath = 'bbdd100k_data/val_images/'
    #dstpath = 'bbdd100k_data/val.txt'
    srcpath = 'E:/LZY/soft_cup2020/darknet-master/build/darknet/x64/data/新建文件夹/'
    dstpath = 'E:/LZY/soft_cup2020/darknet-master/build/darknet/x64/data/新建文件夹/val.txt'
    main(srcpath, dstpath)
