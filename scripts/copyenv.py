from cmath import log
import os
import settings

# DATABASE_URL="postgresql://postgres:postgres@localhost:5432/codinguy?schema=public"



def create_env(base_path):
    env_path = os.path.join(base_path, settings.env_path)
    print(env_path)
    database_name = input('database name: ')
    database_url = f"postgresql://postgres:postgres@localhost:5432/{database_name}?schema=public"

    env_file = open(env_path)
    env_lines_arr = env_file.readlines()
    env_lines_arr.append(f"DATABASE_URL={database_url}\n")
    env_lines_arr.append(f"DATABASE_NAME={database_name}\n")
    
    
    return env_lines_arr

def replace_env(env_path,env_lines):
    project_env_file = open(env_path+'/.env', "w")
    print(project_env_file.writelines(env_lines))