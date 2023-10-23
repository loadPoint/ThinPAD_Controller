from pynput.mouse import Controller, Button
from time import sleep
from config import Config

class ThinPadController:
    def __init__(self):
        cfg = Config()

        self.controller = Controller()
        self.delay = cfg.clickGapTime
        self.dip_switch_pos = []
        for i in range(4):
            for j in range(8):
                self.dip_switch_pos.append(
                    (cfg.dip_switch_x_base[i]-j*cfg.dip_switch_x_gap, cfg.dip_switch_y)
                )
        self.button_pos = []
        for i in range(4):
            self.button_pos.append(
                (cfg.button_x[i], cfg.button_y)
            )
        self.clk_pos = cfg.clk_pos
        self.rst_pos = cfg.rst_pos

        self.dip_status = []
        for i in range(32):
            self.dip_status.append(False)

    
    def debugFindPositon(self, seconds):
        for i in range(seconds):
            print(self.controller.position)
            sleep(1)


    def debugDisplayConfig(self):
        for i in range(4):
            self.clickButton(i)
        self.clickCLK()
        self.clickRST()
        for i in range(32):
            self.__clickDipSwitch__(i)


    def __clickDipSwitch__(self, index):
        sleep(self.delay/32)
        if 0 <= index < 32:
            self.dip_status[index] = not self.dip_status[index]
            self.controller.position = self.dip_switch_pos[index]
            self.controller.click(Button.left, 1)
        else:
            raise Exception(f"Error dip index #{index}")
        
    
    def setDipSwToValue(self, value: str):
        def judgeNeed(dst: str, status: bool):
            if dst == '0' and status == True:
                return True
            elif dst == '1' and status == False:
                return True
            else:
                return False
        sleep(self.delay)
        if len(value) != 32:
            raise Exception(f"Value length must be 32, but found {len(value)}")
        
        for i in range(32):
            if judgeNeed(value[i],self.dip_status[i]):
                self.__clickDipSwitch__(i)
            
    def resetDipSwitch(self):
        self.setDipSwToValue("00000000000000000000000000000000")

    def clickButton(self, index):
        sleep(self.delay)
        if 0 <= index < 4:
            self.controller.position = self.button_pos[index]
            self.controller.click(Button.left, 1)
        else:
            raise Exception(f"Error dip index #{index}")
        

    def clickCLK(self):
        sleep(self.delay)
        self.controller.position = self.clk_pos
        self.controller.click(Button.left, 1)


    def clickRST(self):
        sleep(self.delay)
        self.controller.position = self.rst_pos
        self.controller.click(Button.left, 1)


if __name__ == "__main__":
    tc = ThinPadController()
    tc.debugDisplayConfig()
