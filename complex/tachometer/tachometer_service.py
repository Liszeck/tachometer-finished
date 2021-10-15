from typing import List
from logger import LOG
import os
import json

DATA_DIR = os.path.join(os.getcwd(), 'data')


def get_save_directory(driver: str, vehicle: str) -> str:
    if not os.path.exists(DATA_DIR):
        LOG.info(f'Create Directory {DATA_DIR}')
        os.mkdir(DATA_DIR)
    driver_dir = os.path.join(DATA_DIR, driver.replace(' ','_'))
    if not os.path.exists(driver_dir):
        LOG.info(f'Create Directory {driver_dir}')
        os.mkdir(driver_dir)
    vehicle_dir = os.path.join(driver_dir, vehicle)
    if not os.path.exists(vehicle_dir):
        LOG.info(f'Create Directory {vehicle_dir}')
        os.mkdir(vehicle_dir)
    return vehicle_dir


def record_route(driver : str, vehicle: str, start: str, speed: List[int]):
    save_dir = get_save_directory(driver, vehicle)
    LOG.debug(f'Save Directory: {save_dir}')
    save_filename = start.replace(' ','_') + '.json'
    with open(os.path.join(save_dir, save_filename), 'w') as output:
        data = {
            'driver': driver,
            'vehicle': vehicle,
            'start': start,
            'speed': speed
        }
        output.write(json.dumps(data))
    return f'Hello {driver}'

def read_drivers() -> List[str]:
   return os.listdir(DATA_DIR)

def read_vehicles_of_driver(driver: str) -> List[str]:
    return os.listdir(os.path.join(DATA_DIR, driver))