import tools

def main():
    mainVar = 20 #區域變數  
    print("主程式")
    print(f"pi={tools.PI}")
    print(f"mainVar={mainVar}")

if __name__ == "__main__":
    mainVar = 10 #全域變數
    main()
    