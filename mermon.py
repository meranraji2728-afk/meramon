print("Welcome to AI Legal Advice Chatbot")
print("Type 'exit' to end the chat\n")

while True:
    user_input = input("Ask your legal question: ").lower()

    if user_input == "exit":
        print("Thank you for using the Legal Advice Chatbot.")
        break

    elif "theft" in user_input:
        print("Theft is a punishable offense under IPC Section 378.")
        print("Punishment may include imprisonment or fine.")

    elif "divorce" in user_input:
        print("Divorce laws depend on religion in India.")
        print("You can file divorce in family court with valid reasons.")

    elif "property" in user_input:
        print("Property disputes can be resolved through civil courts.")
        print("Legal documents like sale deed are important.")

    elif "harassment" in user_input:
        print("Harassment is a crime.")
        print("You can file a complaint at the nearest police station.")

    elif "cyber crime" in user_input:
        print("Cyber crimes include hacking, online fraud, and identity theft.")
        print("You can report cyber crime at cybercrime.gov.in")

    else:
        print("Sorry, I can provide only basic legal information.")
        print("Please consult a legal professional for detailed advice.")
