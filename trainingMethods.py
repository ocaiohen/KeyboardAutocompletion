import phraseMethods
import re

def clean_message(message):
    # Remover links (http:// ou https://)
    message = re.sub(r'https?://\S+|www\.\S+', '', message)

    # Remover <Mídia oculta> e <Mensagem editada>
    message = re.sub(r'<(Mídia oculta|Mensagem editada)>', '', message, flags=re.IGNORECASE)

    # Remover contatos @numerosbla
    message = re.sub(r'@\d{8,15}', '', message)

    # Remover emojis (intervalos de emojis Unicode)
    message = re.sub(r'[\U0001F600-\U0001F64F'
                     r'\U0001F300-\U0001F5FF'
                     r'\U0001F680-\U0001F6FF'
                     r'\U0001F1E0-\U0001F1FF'
                     r'\u2600-\u26FF\u2700-\u27BF'
                     r'\U0001F900-\U0001F9FF]+', '', message)
    
    message = re.sub(r'\s+', ' ', message).strip()

    return message

def learn_from_whatsapp_chat_file(file_path, person = "all"):
    #pegar apenas as mensagens de um contato especifico
    #pegar do travessão ao segundo ":"
    with open(file_path, "r", encoding="utf-8") as file:
        #apenas por curiosidade, desabilitar se quiser
        # n_of_messages_learnt = 0
        # n_of_words_typed = 0
        for line in file:

            #algumas linhas para ignorar linhas que não são mensagens
            #como: 08/09/2023 14:27 - Você criou este grupo
            if "-" not in line:
                continue

            parts = line.split("-", 1)
            if len(parts) < 2:
                continue

            contact_and_message = parts[1].strip()

            if ":" not in contact_and_message:
                continue

            contact, message = contact_and_message.split(":", 1)
            contact = contact.strip()
            message = message.strip()

            if person == "all" or contact == person:
                message = clean_message(message)
                message = phraseMethods.basic_input_treatment(message)
                message = phraseMethods.remove_forbidden_characters(message)
                phraseMethods.learn_phrase(message)

                #apenas por curiosidade, desativar se quiser
                # words_list = message.split()
                # n_of_words_typed += len(words_list)
                # n_of_messages_learnt += 1

        #apenas por curiosidade, desativar se quiser
        # print(f"Total de mensagens aprendidas: {n_of_messages_learnt}")
        # print(f"Total de palavras aprendíveis digitadas no grupo: {n_of_words_typed}")


#Exemplo de linha
# 07/03/2025 11:34 - Caio Henrique: @5584123456789, eu estou enlouquecendo <Mensagem editada>

# Padrões para remover:
# - Remover todo link (http ou https)
# - Remover todo <Mídia oculta>
# - Remover contatos e números (ex.: @558499929525)
# - Remover emojis
# - Remover todo <Mensagem editada>