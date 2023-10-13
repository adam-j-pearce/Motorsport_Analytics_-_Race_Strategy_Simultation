import irsdk
import time

class State:
        # sets default calue of status to false
        ir_connected = False

def check_iracing():
    if state.ir_connected and not (ir.is_initialized and ir.is_connected):
        state.ir_connected = False
        ir.shutdown()
        print('irsdk disconnected')
    elif not state.ir_connected and ir.startup() and ir.is_initialized and ir.is_connected:
        state.ir_connected = True
        print('irsdk connected')

def loop():
    ir.freeze_var_buffer_latest()

if __name__ == '__main__':
    # initializing ir and state
    ir = irsdk.IRSDK()
    state = State()

    try:
        while True:
            # check if connected to iracing
            check_iracing()
            # if yes then run loop function
            if state.ir_connected:
                loop()
            # max rate is 1/60 due to iRacing refresh rate
            time.sleep(0.02)
    except KeyboardInterrupt:
        # press ctrl+c to manually exit
        pass