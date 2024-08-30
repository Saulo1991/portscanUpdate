import time
import schedule
import pyscreenshot as ImageGrab
from datetime import datetime
import os

def take_screenshot():
    print('Tirando a captura de tela...')
    
    timestamp = str(datetime.now()).replace(':', '-')
    image_name = f'Screenshot-{timestamp}'
    filepath = f'./screenshots/{image_name}.png'
    
    if not os.path.exists(os.path.dirname(filepath)):
        os.makedirs(os.path.dirname(filepath))
    
    screenshot = ImageGrab.grab()
    screenshot.save(filepath)
    
    print(f'Captura de tela salva em {filepath}!')
    
    return filepath    

def main():
    schedule.every(5).seconds.do(take_screenshot)
    
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == '__main__':
    main()
