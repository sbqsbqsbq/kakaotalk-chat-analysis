
date_list = []
participant_list = []
exit_list = []
text_list = []
message_list = []


def main():
    # 원하는 채팅방 내보내기 내용 txt 파일을 넣어줌.
    with open("group.txt", "r", encoding="utf8") as file:
        texts = file.readlines()
        for text in texts:
            text.replace("\n", "")
            if text[0] == "-" and "년" in text:
                date = text.replace("\n", "").replace("-", "").strip()
                date_list.append(date)
            elif "나갔습니다" in text:
                exit = text.split("님이")[0]
                exit_list.append(exit)
            elif text[0] == "[":
                try:
                    participant = text.split("]")[0].replace("[", "").replace("]", "")

                    data = {
                        "participant": participant,
                    }

                    participant_list.append(participant)
                    message_list.append(data)
                except Exception as e:
                    print(e)

        for participant in list(set(participant_list)):
            print("채팅 참가자: " + participant)

        for exit in exit_list:
            print("나간 사람: " + exit)

        chat_dict = {x: participant_list.count(x) for x in participant_list}

        for key, value in chat_dict.items():
            print(key + "님의 대화 횟수: " + str(value))


if __name__ == '__main__':
    main()