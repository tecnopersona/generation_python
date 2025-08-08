def lucky_sevens_interactivo():
    while True:
        valor_ingresado = input("Enter a number (or type 'salir' to quit): ")
        
        if valor_ingresado.lower() == "salir":
            print("Goodbye!")
            break

        try:
            n = int(valor_ingresado)
        except ValueError:
            print("❌ Please enter a valid integer.")
            continue

        for i in range(1, n + 1):
            if i % 7 == 0 or '7' in str(i):
                print("Lucky")
            else:
                print(i)
lucky_sevens_interactivo()
