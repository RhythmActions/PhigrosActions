import shutil
import os
import json
import datetime 
from datetime import datetime
from datetime import timezone
from datetime import timedelta

cur_path = os.path.dirname(__file__)

if __name__ == "__main__":
    with open(os.path.join(cur_path, "Phigros_Extractor/config.json"), 'r', encoding='utf-8') as f:
        config = json.load(f)
    ver = config["version"]
    
    if "updated" not in config:
        print(json.dumps(config, indent=4, ensure_ascii=False))
        config["updated"] = True
        
    if config["updated"] == True:
        try:
            shutil.rmtree(os.path.join(cur_path, "Tracks"))
            shutil.rmtree(os.path.join(cur_path, "GameInformation"))
            shutil.rmtree(os.path.join(cur_path, "ConstantTable"))
            shutil.rmtree(os.path.join(cur_path, "Avatar"))
            shutil.rmtree(os.path.join(cur_path, "PrehandledIllu"))
        except:
            pass

        print("正在移动曲绘文件")
        shutil.copytree(os.path.join(cur_path, "Phigros_Extractor/Assets/Tracks"), os.path.join(cur_path, "Tracks"), ignore=shutil.ignore_patterns('*.wav', "IllustrationBlur*"))
        print("移动完成")

        print("正在移动GameInformation")
        shutil.copytree(os.path.join(cur_path, "Phigros_Extractor/Assets/GameInformation"), os.path.join(cur_path, "GameInformation"))
        print("移动完成")

        print("正在移动定数表")
        shutil.copytree(os.path.join(cur_path, "Phigros_Extractor/Assets/ConstantTable/Generated"), os.path.join(cur_path, "ConstantTable"))
        print("移动完成")
        
        print("正在移动头像")
        shutil.copytree(os.path.join(cur_path, "Phigros_Extractor/Assets/avatar"), os.path.join(cur_path, "Avatar"))
        print("移动完成")
        
        print("正在移动裁切后曲绘")
        shutil.copytree(os.path.join(cur_path, "Phigros_Extractor/prehandle"), os.path.join(cur_path, "PrehandledIllu"))
        print("移动完成")

    t = datetime.utcnow().replace(tzinfo=timezone.utc)
    SHA_TZ = timezone(
        timedelta(hours=8),
        name='Asia/Shanghai',
    )
    beijing_now = t.astimezone(SHA_TZ)
    beijing_now = beijing_now.strftime("%Y-%m-%d %H:%M:%S") 

    status = {"version": ver, "updateTime": beijing_now}
    with open(os.path.join(cur_path, "status.json"), 'w', encoding='utf8') as f:
        json.dump(status, f, indent=4, ensure_ascii=False)