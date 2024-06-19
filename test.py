import random
import sys

start = int(sys.argv[1]) # 初めの番号
end = int(sys.argv[2])   # 最後の番号
num_questions = int(sys.argv[3])   # 出題数

# データファイルを読み込む関数
def load_words(file_path):
    words = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            parts = line.strip().split()
            num = int(parts[0])
            word = parts[1]
            meaning = meaning = ' '.join(parts[2:])  # 意味の部分が複数の単語から成る場合も考慮
            words.append((num, word, meaning))
    return words


# 間違えた問題番号を読み込む関数
def load_incorrect(file_path):
    incorrect = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            incorrect.append(int(line.strip()))
    return incorrect

# 指定した範囲から指定した問題数を選ぶ関数
def select_questions(words, start, end, num_questions, incorrect, incorrect_weight):
    selected_words = [word for word in words if start <= word[0] <= end]
    
    # 間違えた問題を優先して選ぶためのリストを作成
    weighted_words = []
    for word in selected_words:
        weight = incorrect_weight if word[0] in incorrect else 1
        weighted_words.extend([word] * weight)

    
    my_list = []
    my_list_b = []
 
    a = random.sample(weighted_words, 1)
    
    my_list = [x for x in weighted_words if x != a[0]]

    my_list = weighted_words

    for i in range(num_questions):
        a = random.sample(my_list, 1)
        my_list = [x for x in my_list if x != a[0]]
        my_list_b.append(a)

   
    flattened_list = [item for sublist in my_list_b for item in sublist]
    return flattened_list
    # return random.sample(weighted_words, min(num_questions, len(weighted_words)))

# メインの処理
def main():
    file_path = 'word.txt'  # データファイルのパス
    incorrect_path = 'incorrect.txt'  # 間違えた問題番号のファイルのパス
    incorrect_weight = 5  # 間違えた問題が出やすくなる倍率

    words = load_words(file_path)
    incorrect = load_incorrect(incorrect_path)

    selected_questions = select_questions(words, start, end, num_questions, incorrect, incorrect_weight)

    # print(selected_questions)
    # for num, word, meaning in selected_questions:
    #     print(f"{num:3d} {word}")

    with open("test.txt", 'w', encoding='utf-8') as file:
        for num, word, meaning in selected_questions:
            file.write(f"{num:3d} {word}\n")

    with open("ansewr.txt", 'w', encoding='utf-8') as file:
        for num, word, meaning in selected_questions:
            file.write(f"{num:3d} {word} {meaning}\n")

# プログラムのエントリポイント
if __name__ == '__main__':
    main()