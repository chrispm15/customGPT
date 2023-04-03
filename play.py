import openai
##########################
## ENTER YOUR API KEY HERE
##
API_KEY = ''
##        ^^
###########################




openai.api_key = API_KEY

system = input("System Prompt -- Give GPT all the information and context it needs for the following conversation (ie. You are ScientistGPT, you are designed to answer all science-related questions to the best of your ability):  ")
user = input('\n\nUser Prompt:  ')

def conversation(initial_system, initial_user):
    convo = ''
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": initial_system},
            {"role": "user", "content": initial_user}
        ]
    )
    output = response['choices'][0]['message']['content']
    convo = convo + ' ' + output
    print(f"\nOutput: {output}")

    while True:
        prompt_system = f'You are mid-convo. Here is your System Prompt: [{initial_system}]. The conversation so far is as follows: [{convo}].'
        prompt_user = input('\n\nUser Prompt:  ')
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": prompt_system},
                {"role": "user", "content": prompt_user}
            ]
        )
        output = response['choices'][0]['message']['content']
        convo = convo + ' ' + output
        print(f"\nOutput: {output}")

conversation(system, user)
