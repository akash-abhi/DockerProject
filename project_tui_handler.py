import os

while True:
    os.system("clear")
    os.system("tput setaf 1")
    print("\n****************************************")
    print("      Docker Project TUI Handler")
    print("****************************************")

    os.system("tput setaf 2")
    print("""
    1. Check Status of Infrastructure
    2. Launch Infrastructure
    3. Start Infrasturcture
    4. Stop Infrastructure
    5. Destroy Infrastructure
    6. Stop Firewall
    7. Exit
    """)

    os.system("tput setaf 7")
    print("\n Enter your choice (1-7) : ",end="")
    ch = input()

    if int(ch) == 1:
        os.system("docker-compose ps")
    elif int(ch) == 2:
        print("docker-compose up -d")
    elif int(ch) == 3:
        os.system("docker-compose start")
    elif int(ch) == 4:
        os.system("docker-compose stop")
    elif int(ch) == 5:
        os.system("docker-compose rm -f")
    elif int(ch) == 6:
        os.system("systemctl stop firewalld")
    elif int(ch) == 7:
        exit(0)
    
    os.system("tput setaf 3")
    input("\nPress any key to continue...")
    os.system("tput setaf 7")
