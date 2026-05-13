class Logicgate:
    def __init__(self, label):
        self.label = label
        self.output = None

    def get_label(self):
        return self.label

    def get_output(self):
        return self.perform_gate_logic()

    def perform_gate_logic(self):
        raise NotImplementedError("子类必须实现此方法")

class Binarygate(Logicgate):
    def __init__(self, label):
        super().__init__(label)
        self.pin_a = None
        self.pin_b = None

    def get_pin_a(self):
        if self.pin_a is None:
            return int(input(f"请输入{self.get_label()}pin_A的数值："))
        return self.pin_a

    def get_pin_b(self):
        if self.pin_b is None:
            return int(input(f"请输入{self.get_label()}pin_B的数值："))
        return self.pin_b

    def set_pin(self,pin_num,value):
        if pin_num == 1:
            self.pin_a = value
        elif pin_num == 2:
            self.pin_b = value
        else:
            raise ValueError("输入的引脚数值有误")

class Unarygate(Logicgate):
    def __init__(self, label):
        super().__init__(label)
        self.pin = None

    def get_pin(self):
        if self.pin == None:
            return int(input(f"请输入{self.get_label()}pin的数值："))
        return self.pin

    def set_pin(self,pin_num,value):
        if pin_num != 1:
            raise ValueError("引脚的数值应为1")
        self.pin = value

class Andgate(Binarygate):
    def __init__(self, label):
        super().__init__(label)

    def perform_gate_logic(self):
        a = self.get_pin_a()
        b = self.get_pin_b()
        if a==1 and b==1:
            return 1
        elif a == 0 or b == 0:
            return 0
        else:
            raise ValueError("请输入0或者1")

class Orgate(Binarygate):
    def __init__(self, label):
        super().__init__(label)

    def perform_gate_logic(self):
        a = self.get_pin_a()
        b = self.get_pin_b()
        if a==1 or b==1:
            return 1
        elif a==0 and b==0:
            return 0
        else:
            raise ValueError("请输入0或者1")

class Notgate(Unarygate):
    def __init__(self, label):
        super().__init__(label)

    def perform_gate_logic(self):
        a = self.get_pin()
        if a==1:
            return 0
        elif a==0:
            return 1
        else:
            raise ValueError("请输入0或者1")

class Connector:
    def __init__(self,from_gate,to_gate,to_pin):
        self.from_gate = from_gate
        self.to_gate = to_gate
        self.to_pin = to_pin
        value = from_gate.get_output()
        to_gate.set_pin(to_pin,value)

if __name__ == "__main__":
    g1 = Andgate("A1")
    g2 = Orgate("O1")
    g1.pin_a = 1
    g1.pin_b = 0
    value = g1.get_output()
    Connector(g1,g2,1)
    print(f"逻辑门电路最终输出结果为 {g2.get_output()}")
