import tools

def main():
    global mainVar
    mainVar = 20 #區域變數  
    print("主程式")
    print(f"pi={tools.PI}")
    

if __name__ == "__main__":
    mainVar = 10 #全域變數
    main()
    print(f"mainVar={mainVar}")
    