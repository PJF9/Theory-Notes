import os
from pathlib import PurePath
from time import sleep
from threading import Thread
from subprocess import run, DEVNULL
import ctypes


def is_admin():
    try:
        admin = (os.getuid() == 0)
    except AttributeError:
        admin = (ctypes.windll.shell32.IsUserAnAdmin() != 0)

    return admin



class File_System_Operations:
    
    def get_envs(self):
        return {env_name:env_value for (env_name, env_value) in os.environ.items()}

    def get_env(self, env_name):
        try:
            return self.get_envs()[env_name]
        except KeyError:
            return None

    def set_env(self, env):
        ### Need rebot cmd
        if isinstance(env, dict):
            env_name = str([key for key in env.keys()][0])
            env_value = str([val for val in env.values()][0])

            if is_admin():
                run(f"setx {env_name} {env_value}", shell=True, stdout=DEVNULL)
                return True
            else:
                print("Need admin....")

        return False
    
    def delete_env(self, env_name):
        if is_admin():
            return_code = run(f'REG delete "HKCU\Environment" /F /V {env_name}', shell=True, stdout=DEVNULL, stderr=DEVNULL)
            return True if return_code.returncode == 0 else False
        else:
            print("Need admin...")
        return False

    def get_curr_dir(self):
        return os.getcwd()

    def change_dir(self, new_dir):
        try:
            os.chdir(str(new_dir))
        except FileNotFoundError:
            return False
        return True

    def has_access(self, file_path, mode):
        if os.path.isfile(file_path):
            if mode == 'r+':
                try:
                    with open(file_path, mode) as file:
                        file.read()
                        file.write('')
                except PermissionError:
                    return False
            elif mode == 'r':
                try:
                    with open(file_path, mode) as file:
                        file.read()
                except PermissionError:
                    return False
            elif (mode == 'w') or (mode == 'a'):
                try:
                    with open(file_path, 'a') as file:
                        file.write('')
                except PermissionError:
                    return False
            elif mode == 'x':
                if file_path.split('.')[-1] == "exe":
                    a = Thread(target=lambda: run(file_path, shell=True, stdout=DEVNULL, stderr=DEVNULL))
                    a.daemon = True
                    a.start()
                    sleep(0.06)

                    return_code = run(f"taskkill /f /im {file_path}", shell=True, stdout=DEVNULL, stderr=DEVNULL)
                    if return_code.returncode != 0:
                        return False
                else:
                    return False
            else:
                return False

            return True
        return False

    def change_file_access(self, file_path, mode, change_admin=False):
        if is_admin():
            if os.path.isfile(file_path):
                username = "jacob" if not change_admin else "Administrators"

                if mode == "f":
                    run(f"icacls {file_path} /grant {username}:F", stdout=DEVNULL, stderr=DEVNULL)
                elif mode == "n":
                    run(f"icacls {file_path} /deny {username}:F", stdout=DEVNULL, stderr=DEVNULL)
                elif mode == "x":
                    run(f"icacls {file_path} /grant {username}:RX", stdout=DEVNULL, stderr=DEVNULL)
                elif mode == "nx":
                    run(f"icacls {file_path} /deny {username}:RX", stdout=DEVNULL, stderr=DEVNULL)
                elif mode == "r":
                    run(f"icacls {file_path} /grant {username}:R", stdout=DEVNULL, stderr=DEVNULL)
                elif mode == "nr":
                    run(f"icacls {file_path} /deny {username}:R", stdout=DEVNULL, stderr=DEVNULL)
                elif mode == "w":
                    run(f"icacls {file_path} /grant {username}:W", stdout=DEVNULL, stderr=DEVNULL)
                elif mode == "nw":
                    run(f"icacls {file_path} /deny {username}:W", stdout=DEVNULL, stderr=DEVNULL)
                elif mode == "d":
                    run(f"icacls {file_path} /grant {username}:D", stdout=DEVNULL, stderr=DEVNULL)
                elif mode == "nd":
                    run(f"icacls {file_path} /deny {username}:D", stdout=DEVNULL, stderr=DEVNULL)
                else:
                    return False

                return True
        return False

    def list_directory(self, dir_path):
        if os.path.isdir(str(dir_path)):
            return os.listdir(str(dir_path))

    def create_folder(self, folder_name_path):
        try:
            folder_name_path = '\\'.join(str(folder_name_path).split('\\')[:-1] + [str(folder_name_path).split('\\')[-1].split('.')[0]])
        except IndexError:
            pass

        run(f"mkdir {folder_name_path}", shell=True, stdout=DEVNULL, stderr=DEVNULL)

    def create_file(self, file_name_path, content=''):
        try:
            with open(file_name_path, 'w') as file:
                file.write(content)
        except FileNotFoundError:
            return False
        except ValueError:
            return False
        except TypeError:
            return False

        return True
        
    def remove_folder(self, folder_name_path):
        if is_admin():
            if os.path.isdir(str(folder_name_path)):
                run(f"rmdir /s /q {str(folder_name_path)}", shell=True, stdout=DEVNULL, stderr=DEVNULL)
                return True
        return False

    def remove_file(self, file_name_path):
        if is_admin():
            if os.path.isfile(str(file_name_path)):
                run(f"del /f {str(file_name_path)}", shell=True, stdout=DEVNULL, stderr=DEVNULL)
                return True
        return False

    def rename_folder_or_file(self, old_name_path, new_name):
        if is_admin():
            if os.path.isdir(str(old_name_path)) or os.path.isfile(str(old_name_path)):
                run(f"ren {str(old_name_path)} {str(new_name)}", shell=True, stdout=DEVNULL, stderr=DEVNULL)
                return True
        return False

    def is_file(self, path):
        return os.path.isfile(str(path))
    
    def is_folder(self, path):
        return os.path.isdir(str(path))

    def exists(self, path):
        return os.path.exists(str(path))

    def split_path(self, path):
        return PurePath(path).parts

    def get_drive(self, path):
        return PurePath(path).drive

    def get_file_exname(self, file_name_path):
        if os.path.isfile(file_name_path):
            return PurePath(file_name_path).name

    def get_file_name(self, file_name_path):
        if os.path.isfile(file_name_path):
            return PurePath(file_name_path).stem

    def get_parent_directory(self, file_name_path):
        if os.path.isfile(file_name_path):
            return PurePath(file_name_path).parent

    def get_file_suffixes(self, file_name_path):
        if os.path.isfile(file_name_path):
            return PurePath(file_name_path).suffixes
