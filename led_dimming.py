import time
import pigpio

pi = pigpio.pi()
pi.set_mode(13, pigpio.OUTPUT)
pi.hardware_PWM(13, 5000, 0)

def led_pwm(val, tout):

    i=int((pi.get_PWM_dutycycle(13))/10000)
    print(i)
    if (int(val)>i):
        while (i<val):
            i=i+1
            pi.hardware_PWM(13, 1000, i*10000)
            time.sleep(0.005)
            
    if (int(val)<i):
        while (i>val):
            i=i-1
            pi.hardware_PWM(13, 1000, i*10000)
            time.sleep(tout/100)#fadeout parametrizavel
