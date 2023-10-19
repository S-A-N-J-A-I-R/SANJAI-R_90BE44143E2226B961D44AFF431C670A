def linear_search_product(products: list, target_product: str) -> list:
  indices = []
  for i in range(len(products)):
      if products[i] == target_product:
          indices.append(i)
  return indices

# Define a list of products
products = ["apple", "banana", "orange", "banana", "grape"]

# Search for "banana" in the list of products
indices = linear_search_product(products, "banana")

# Print the indices of all occurrences of "banana"
print(indices)