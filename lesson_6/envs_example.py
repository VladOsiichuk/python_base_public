from dotenv import load_dotenv
import os
from environs import Env



def main():
    env = Env()
    env.read_env()
    arr = env.list("ARR")
    print(len(arr))
    print(arr)
    print([type(var) for var in arr])
    print([type(var) for var in env("ARR")])


if __name__ == "__main__":
    main()
