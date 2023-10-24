# ThinPAD_Controller
清华大学 ThinPAD实验平台 自动点击器

使用方法: 

1. 首先执行 Controller.debugFindPositon(10) (或者别的数字)手动校准，把读到的数据写到 config.py 里面
2. 之后需要新建一个 main.py 文件，写入以下的东西:

```python
from thinpad_controller import ThinPadController as Controller
from instr import *

if __name__ == "__main__":
    tc = Controller()
    tc.clickRST()
    sleep(1)
    # Write your operations

    # Finish your operations
    tc.resetDipSwitch()
    print("Finished !")
```

运行 `python main.py` 以使用