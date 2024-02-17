import gpt_2_simple as gpt2

def initialize_model():
    model_name = "124M"
    gpt2.download_gpt2(model_name=model_name)
    sess = gpt2.start_tf_sess()
    gpt2.load_gpt2(sess, model_name=model_name)
    return sess

def generate_response(sess, user_input):
    response = gpt2.generate(sess, model_name="124M", prefix=user_input, length=50, temperature=0.7, return_as_list=True)[0]
    return response

def main():
    sess = initialize_model()
    print("Chatbot: Hello! How can I assist you today? Type 'exit' to end the conversation.")

    while True:
        user_input = input("You: ")
        
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye! Have a great day.")
            break

        response = generate_response(sess, user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    main()
