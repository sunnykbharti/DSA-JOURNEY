def printSubsequences(index, current, s):
    # BASE CASE: We have considered all characters
    if index == len(s):
        print(f"'{current}'")
        return

    # RECURSIVE STEP 1: TAKE the current character
    # We add s[index] to our current string
    printSubsequences(index + 1, current + s[index], s)

    # RECURSIVE STEP 2: LEAVE the current character
    # We do NOT add anything, just move index forward
    printSubsequences(index + 1, current, s)

# --- Test ---
original_str = "abc2333"
print("All Subsequences:")
printSubsequences(0, "", original_str)