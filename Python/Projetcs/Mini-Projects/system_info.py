from psutil import boot_time, disk_partitions, disk_usage, virtual_memory, cpu_count, cpu_freq, cpu_percent
from datetime import datetime
from platform import uname
from wmi import WMI
from GPUtil import getGPUs
from subprocess import run


class System_Informationer:

    @staticmethod
    def __get_size(bytes, suffix='B'):
        """
        Scale bytes to its proper format
        e.g:
            1253656 => '1.20MB'
            1253656678 => '1.17GB'
        """
        factor = 1024
        for unit in ["", "K", "M", "G", "T", "P"]:
            if bytes < factor:
                return f"{bytes:.2f}{unit}{suffix}"
            bytes /= factor

    def last_booted(self):
        boot_time_timestamp = boot_time()
        return datetime.fromtimestamp(boot_time_timestamp)

    def internet_speed(self):
        out = run("speedtest-cli --simple --timeout 5", shell=True, capture_output=True, text=True)
        return [x.lstrip() for x in out.stdout.split('\n')][:-1]

    def disk_info(self):
        partitions = disk_partitions()
        partitions_info = []
        for partition in partitions:
            partition_info = {}
            partition_info["device"] = partition.device[0]
            partition_info["mountpoint"] = partition.device
            partition_info["file_system_type"] = partition.fstype
            try:
                partition_usage = disk_usage(partition.mountpoint)
            except PermissionError:
                # this can be catched due to the disk that isn't ready
                continue

            partition_info["total_size"] = self.__get_size(partition_usage.total)
            partition_info["space_used"] = self.__get_size(partition_usage.used)
            partition_info["free_space"] = self.__get_size(partition_usage.free)
            partition_info["percentage(%)"] = partition_usage.percent
        
            partitions_info.append(partition_info)

        return partitions_info

    def system_info(self):
        my_system = uname()
        comp = WMI()   
        system = comp.Win32_ComputerSystem()[0]
        info = {}

        info["os"] = my_system.system
        info["name"] = my_system.node
        info["version"] = my_system.version
        info["manufacturer"] = system.Manufacturer
        info["model"] = system. Model
        info["type"] = system.SystemType

        return info

    def ram_info(self):
        ram_obj = virtual_memory()
        info = {}

        info["total"] = self.__get_size(ram_obj.total)
        info["available"] = self.__get_size(ram_obj.available)
        info["used"] = self.__get_size(ram_obj.used)
        info["percentage(%)"] = ram_obj.percent

        return info

    def cpu_info(self):
        my_system = uname()
        cpufreq = cpu_freq()
        info = {}

        info["total_cores"] = cpu_count(logical=True)
        info["name"] = my_system.processor
        info["max_frec(Mhz)"] = cpufreq.max
        info["min_frec(Mhz)"] = cpufreq.min
        info["current_frec(Mhz)"] = cpufreq.current
        info["usage(%)"] = cpu_percent()

        return info

    def gpu_info(self):
        gpus = getGPUs()
        total_info = []

        for gpu in gpus:
            info = {}

            info["id"] = gpu.id
            info["name"] = gpu.name
            info["percentage"] = f"{gpu.load*100}%"
            info["free_memory"] = f"{gpu.memoryFree}MB"
            info["used_memory"] = f"{gpu.memoryUsed}MB"
            info["total_memory"] = f"{gpu.memoryTotal}MB"
            info["temperature"] = f"{gpu.temperature} °C"
            info["uuid"] = gpu.uuid

            total_info.append(info)

        return total_info


