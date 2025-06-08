import machine
import neopixel
import time
import math

NUM_PIXELS = 30
NEOPIXEL_PIN = 18
I2C_SDA = 21
I2C_SCL = 23
MPU_ADDR = 0x68
LOOP_DELAY = 0.025
SCALE_FACTOR = 100.0

_REG_PWR_MGMT1 = 0x6B
_REG_ACCEL_XOUT_H = 0x3B
_REG_GYRO_XOUT_H = 0x43

def hsv_to_rgb(h, s, v):
    c = v * s
    x = c * (1 - abs((h / 60.0) % 2 - 1))
    m = v - c
    if h < 60:
        rp, gp, bp = c, x, 0
    elif h < 120:
        rp, gp, bp = x, c, 0
    elif h < 180:
        rp, gp, bp = 0, c, x
    elif h < 240:
        rp, gp, bp = 0, x, c
    elif h < 300:
        rp, gp, bp = x, 0, c
    else:
        rp, gp, bp = c, 0, x
    r = int((rp + m) * 255)
    g = int((gp + m) * 255)
    b = int((bp + m) * 255)
    return r, g, b

class MPU6050:
    def __init__(self, i2c, addr=0x68):
        self.i2c = i2c
        self.addr = addr
        self.i2c.writeto_mem(self.addr, _REG_PWR_MGMT1, b'\x00')
        time.sleep_ms(10)

    def read_raw_accel(self):
        data = self.i2c.readfrom_mem(self.addr, _REG_ACCEL_XOUT_H, 6)
        ax = (data[0] << 8) | data[1]
        ay = (data[2] << 8) | data[3]
        az = (data[4] << 8) | data[5]
        if ax & 0x8000: ax -= 0x10000
        if ay & 0x8000: ay -= 0x10000
        if az & 0x8000: az -= 0x10000
        return ax, ay, az

    def read_raw_gyro(self):
        data = self.i2c.readfrom_mem(self.addr, _REG_GYRO_XOUT_H, 6)
        gx = (data[0] << 8) | data[1]
        gy = (data[2] << 8) | data[3]
        gz = (data[4] << 8) | data[5]
        if gx & 0x8000: gx -= 0x10000
        if gy & 0x8000: gy -= 0x10000
        if gz & 0x8000: gz -= 0x10000
        return gx, gy, gz

    def get_accel_g(self):
        raw = self.read_raw_accel()
        return raw[0] / 16384.0, raw[1] / 16384.0, raw[2] / 16384.0

    def get_gyro_dps(self):
        raw = self.read_raw_gyro()
        return raw[0] / 131.0, raw[1] / 131.0, raw[2] / 131.0

i2c = machine.I2C(0, scl=machine.Pin(I2C_SCL), sda=machine.Pin(I2C_SDA), freq=400000)
time.sleep_ms(20)
mpu = MPU6050(i2c, MPU_ADDR)

np_pin = machine.Pin(NEOPIXEL_PIN, machine.Pin.OUT)
strip = neopixel.NeoPixel(np_pin, NUM_PIXELS)
BRIGHTNESS = 0.8

for i in range(NUM_PIXELS):
    strip[i] = (0, 0, 0)
strip.write()

while True:
    ax, ay, az = mpu.get_accel_g()
    gx, gy, gz = mpu.get_gyro_dps()
    accel_mag = math.sqrt(ax*ax + ay*ay + az*az)
    accel_motion = abs(accel_mag - 1.0)
    gyro_mag = math.sqrt(gx*gx + gy*gy + gz*gz) / 250.0
    motion = accel_motion + gyro_mag

    if motion < 0.02:
        t = motion / 0.02
        r1, g1, b1 = 100, 0, 0
        R = int(r1 + t * (255 - r1))
        G = int(g1 + t * (64 - g1))
        B = int(b1 + t * (32 - b1))
    else:
        hue = (motion * SCALE_FACTOR) % 360.0
        R, G, B = hsv_to_rgb(hue, 1.0, 1.0)
        R = int(R + (255 - R) * 0.5)
        G = int(G * 0.4)
        B = int(B * 0.2)

    R = int(R * BRIGHTNESS)
    G = int(G * BRIGHTNESS)
    B = int(B * BRIGHTNESS)

    for i in range(NUM_PIXELS):
        strip[i] = (R, G, B)
    strip.write()
    time.sleep(LOOP_DELAY)
