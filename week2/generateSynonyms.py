import fasttext

model_path = r'/workspace/datasets/fasttext/title_model.bin'
top_words_path = r'/workspace/datasets/fasttext/top_words.txt'
output_path = r'/workspace/datasets/fasttext/synonyms.csv'

threshold = 0.75

model = fasttext.load_model(model_path)

input = open(top_words_path, 'r')
lines = input.readlines()

with open(output_path, 'w') as f:
    for line in lines:
        line = line.strip()
        nns = filter(lambda x: x[0] >= threshold, model.get_nearest_neighbors(line))
        words = map(lambda x: x[1], nns)
        f.write(f"{line},{','.join(words)}\n")
