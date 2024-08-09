def merge_sort(arr):
    """
    Sorts an array using the merge sort algorithm.
    
    Parameters:
    arr (list): The list of elements to be sorted.
    
    Returns:
    list: A new list containing all elements from the original list in sorted order.
    """
    if len(arr) <= 1:
        return arr

    # Split the array into two halves
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    # Merge the sorted halves
    return merge(left_half, right_half)

def merge(left, right):
    """
    Merges two sorted lists into a single sorted list.
    
    Parameters:
    left (list): A sorted list of elements.
    right (list): Another sorted list of elements.
    
    Returns:
    list: A single sorted list containing all elements from the input lists.
    """
    merged_list = []
    left_index = 0
    right_index = 0

    # Compare elements from both halves and merge them in sorted order
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged_list.append(left[left_index])
            left_index += 1
        else:
            merged_list.append(right[right_index])
            right_index += 1

    # Append any remaining elements from the left list
    while left_index < len(left):
        merged_list.append(left[left_index])
        left_index += 1

    # Append any remaining elements from the right list
    while right_index < len(right):
        merged_list.append(right[right_index])
        right_index += 1

    return merged_list

def debug_merge_sort(arr, depth=0):
    """
    Sorts an array using merge sort with debugging information.
    
    Parameters:
    arr (list): The list of elements to be sorted.
    depth (int): The current depth in the recursion tree.
    
    Returns:
    list: A new list containing all elements from the original list in sorted order.
    """
    indent = "  " * depth
    print(f"{indent}Sorting: {arr}")

    if len(arr) <= 1:
        print(f"{indent}Base case reached with: {arr}")
        return arr

    mid = len(arr) // 2
    left_half = debug_merge_sort(arr[:mid], depth + 1)
    right_half = debug_merge_sort(arr[mid:], depth + 1)

    merged = merge(left_half, right_half)
    print(f"{indent}Merged {left_half} and {right_half} into {merged}")
    return merged

# Example usage
if __name__ == "__main__":
    unsorted_list = [38, 27, 43, 3, 9, 82, 10]
    sorted_list = debug_merge_sort(unsorted_list)
    print("Sorted list:", sorted_list)
