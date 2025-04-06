from motor_encoder import read_encoder


def gotomax(max_features: list):
    max_turns, max_angle = max_features
    target_turns, target_angle = read_encoder(port="COM5", baudrate=38400, mode="carry")
    print(target_angle, target_turns)
    delta = (target_turns - max_turns) * 360 + (target_angle - max_angle)  # 误差总角度
    print(delta)


def calculate_step(max_features: list):
    '''
    预计是读取编码器中电机参数，此处偷懒使用固定参数
    '''
    max_turns, max_angle = max_features
    target_turns, target_angle = read_encoder(port="COM5", baudrate=38400, mode="carry")
    delta = (target_turns - max_turns) * 360 + (target_angle - max_angle)  # 误差总角度
    step = int(delta/360*6400)
    print(f"需要的脉冲数为{step}")



if __name__ =="__main__":
    calculate_step([4300,30])
