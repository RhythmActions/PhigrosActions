import shutil
import os

cur_path = os.path.dirname(__file__)

if __name__ == "__main__":
    print("正在移动曲绘文件")
    shutil.copytree(os.path.join(cur_path, "Phigros_Extractor/Assets/Tracks"), os.path.join(cur_path, "Tracks"), ignore=shutil.ignore_patterns('*.json', '*.wav', "IllustrationBlur*"))
    print("移动完成")

    print("正在移动GameInformation")
    shutil.copytree(os.path.join(cur_path, "Phigros_Extractor/Assets/GameInformation"), os.path.join(cur_path, "GameInformation"))
    print("移动完成")

    print("正在移动定数表")
    shutil.copytree(os.path.join(cur_path, "Phigros_Extractor/Assets/ConstantTable/Generated"), os.path.join(cur_path, "ConstantTable"))
    print("移动完成")