from collections import Counter

input_path = r'/workspace/datasets/fasttext/labeled_products.txt'
output_path = r'/workspace/datasets/fasttext/pruned_labeled_products.txt'

input = open(input_path, 'r')
lines = input.readlines()

MIN_PRODUCTS = 500

products = []
pruned_products = []
for line in lines:
    product = line.split(' ', 1)
    products.append(product)

counter = Counter(product[0] for product in products)

for product in products:
    label = product[0]
    if counter[label] >= MIN_PRODUCTS:
        pruned_products.append(product)

print(f"Pre-prune: {len(products)}, Post-prune: {len(pruned_products)}")

with open(output_path, 'w') as f:
    for product in pruned_products:
        f.write(' '.join(product))
