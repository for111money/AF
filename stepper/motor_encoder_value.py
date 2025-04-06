import serial
import time

def calc_crc(cmd_bytes):
    """计算 8bit 和校验"""
    return sum(cmd_bytes) & 0xFF

def build_command(command_code):
    """构建发送命令"""
    cmd = [0xFA, 0x01, command_code]
    crc = calc_crc(cmd)
    cmd.append(crc)
    return bytes(cmd)

def parse_response(data):
    """解析 MT6816 返回的多圈数据（高32位圈数 + 低16位角度）"""
    if len(data) != 10 or data[0] != 0xFB:
        print("返回数据格式错误")
        return None

    # 圈数（高 4 字节）
    turns = (data[3] << 24) | (data[4] << 16) | (data[5] << 8) | data[6]

    # 角度（低 2 字节），范围 0x0000 ~ 0x4000（0~16384）
    raw_angle = (data[7] << 8) | data[8]
    angle_deg = (raw_angle / 0x4000) * 360  # 映射到 0~360°

    return [turns, angle_deg]

def read_encoder(port="COM3", baudrate=9600, mode="carry"):
    """读取编码器值（mode 支持 'carry'=0x30 或 'accum'=0x31）"""
    command_code = 0x30 if mode == "carry" else 0x31
    cmd = build_command(command_code)

    with serial.Serial(port, baudrate, timeout=0.5) as ser:
        ser.write(cmd)
        time.sleep(0.05)
        response = ser.read(10)

    if len(response) != 10:
        print("读取超时或响应错误")
        return None

    result = parse_response(response)
    if result:
        turns, angle = result
        print(f"圈数: {turns}, 当前角度: {angle:.2f}°")
        print(response)
        return turns, angle
    return None


if __name__ == "__main__":
    read_encoder(port="COM5", baudrate=38400, mode="carry")  # Windows 示例
    # read_encoder(port="/dev/ttyUSB0", baudrate=9600, mode="accum")  # Linux 示例

